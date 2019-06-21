# description: "Projeto da disciplina de Linguagens Formais 2019.1"
# authors:
#     "Arthur Mesquita Pickcius",
#     "Francisco Luiz Vicenzi",
#     "Joao Fellipe Uller"
# Copyright 2019
import copy


class ContextFreeGrammar:
    # constructor
    def __init__(self, nonterminals, terminals, productions, start_symbol):
        self.nonterminals = nonterminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol
        self.first = self.calc_firsts()
        self.follow = self.calc_follows()


    def production_first(self, production, pos, first):
        p_first = {"&"}

        if production == "&":
            return p_first

        while pos != len(production):
            p_first.update(first[production[pos]])
            if "&" not in first[production[pos]]:
                p_first.discard("&")
                break
            pos += 1
        return p_first


    # calculates all symbols firsts of the grammar
    def calc_firsts(self):
        first = {}
        last_first = {}

        for non_terminal in self.nonterminals:
            first[non_terminal] = set()
            last_first[non_terminal] = set()
        for terminal in self.terminals:
            first[terminal] = {terminal}

        ttl = 128

        while last_first != first:
            if ttl == 0:
                print("WARNING (ContextFreeGrammar First): loop detected")
                break
            ttl -= 1

            last_first = copy.deepcopy(first)

            for non_terminal in self.nonterminals:
                for production in self.productions[non_terminal]:
                    if production == "&":
                        first[non_terminal].add(production)
                    else:
                        for pos, symbol in enumerate(production):
                            if symbol in self.terminals:
                                first[symbol] = [symbol]
                                first[non_terminal].add(symbol)
                                break
                            elif symbol in self.nonterminals:
                                production_first = self.production_first(production, pos, first)
                                first[non_terminal].update(production_first)
                                if '&' not in production_first:
                                    break
                            else:
                                raise Exception(
                                    """
                                        ERROR (ContextFreeGrammar First):
                                        unexpected symbol
                                    """
                                )

        # to list
        first_list = {}
        for symbol, nt_first in first.items():
            first_list[symbol] = list(nt_first)
        return first_list


    # calculates all symbols follows of the grammar
    def calc_follows(self):
        follow = {}
        last_follow = {}

        for non_terminal in self.nonterminals:
            follow[non_terminal] = set()
            last_follow[non_terminal] = set()

        follow[self.start_symbol].add("$")

        ttl = 128

        while last_follow != follow:
            if ttl == 0:
                print("WARNING (ContextFreeGrammar Follow): loop detected")
                break
            ttl -= 1

            last_follow = copy.deepcopy(follow)

            for non_terminal in self.nonterminals:
                for production in self.productions[non_terminal]:
                    for pos, symbol in enumerate(production):
                        if symbol in self.nonterminals:
                            if pos == len(production) - 1:
                                follow[symbol].update(follow[non_terminal])
                            else:
                                follow[symbol].update(
                                    self.production_first(
                                        production, pos + 1, self.first
                                    )
                                )
                                follow[symbol].discard("&")
                                if "&" in self.production_first(
                                    production, pos + 1, self.first
                                ):
                                    if symbol == "k":
                                        pass
                                    follow[symbol].update(follow[non_terminal])

        # to list
        follow_list = {}
        for symbol, nt_follow in follow.items():
            follow_list[symbol] = list(nt_follow)
        return follow_list


    # returns the LL(1) parse table of the grammar
    def ll_one_table(self):
        error_message = """
                            ERROR (ContextFreeGrammar ll(1)):
                            multiple entries on same cell
                        """

        table = {}
        for non_terminal in self.nonterminals:
            table[non_terminal] = {}

        for non_terminal in self.nonterminals:
            for production in self.productions[non_terminal]:
                first_alpha = self.production_first(production, 0, self.first)
                for b in first_alpha:
                    if b != "&":
                        if b in table[non_terminal]:
                            raise Exception(error_message)
                        table[non_terminal][b] = production
                if "&" in first_alpha:
                    for c in self.follow[non_terminal]:
                        if c in table[non_terminal]:
                            raise Exception(error_message)
                        table[non_terminal][c] = production
        return table

    def remove_unit_rules(self):
        productions = copy.deepcopy(self.productions)

        for non_terminal in self.nonterminals:
            for production in self.productions[non_terminal]:

                if production in self.nonterminals:
                    productions[non_terminal].remove(production)

                    for prod in self.productions[production]:
                        if prod not in productions[non_terminal]:
                            productions[non_terminal].append(prod)
        return productions

    def remove_unreachable_rules(self):
        reachable = {self.start_symbol}
        last_reachable = set()

        while reachable != last_reachable:
            last_reachable = reachable.copy()
            for non_terminal in self.nonterminals:
                if non_terminal in reachable:
                    for production in self.productions[non_terminal]:

                        for symbol in production:
                            if symbol in self.nonterminals:
                                reachable.add(symbol)

        unreachable = set(self.nonterminals).difference(reachable)
        for nonterminal in unreachable:
            self.productions.pop(nonterminal)
        self.nonterminals = list(reachable)

    def remove_improductive_rules(self):
        last_productive = set(':3')
        productive = set()

        while last_productive != productive:
            last_productive = productive.copy()
            for non_terminal in self.nonterminals:
                for production in self.productions[non_terminal]:
                    for symbol in production:
                        if symbol in self.terminals or symbol in productive:
                            productive.add(non_terminal)

        if self.start_symbol not in productive:
            raise Exception("ERROR: start symbol is DEAD!")
            self.init_state = ''
        dead_states = set(self.nonterminals).difference(productive)
        for dead_state in dead_states:
            self.productions.pop(dead_state)
        self.nonterminals = list(productive)

    # SENTENCE RECOGNITION FUNCTIONS
    # evaluates if a sentence is recognized or not by the grammar simulating a pushdown automaton (GLC cannot have left recursion)
    def pa_sentence_recognition(self, sentence):
        sentence += "$"
        sentence = list(sentence)
        stack = []
        stack.append('$')
        stack.append(self.start_symbol)

        return self.pa_make_transition(sentence, stack)


    # makes a transition in the pushdown automaton
    def pa_make_transition(self, sentence, stack):
        while stack[-1] != '$' and stack[-1] == sentence[0]:
            stack.pop()
            sentence.pop(0)

        if stack[-1] == '$' or not(stack[-1] in self.nonterminals):
            if sentence[0] == stack[-1]: return True
            else: return False

        else:
            symbol = stack.pop()
            for production in self.productions[symbol]:
                new_stack = copy.copy(stack)
                sentence_aux = copy.copy(sentence)
                if production != '&':
                    for i in range(1, len(production)+1):
                        new_stack.append(production[-i])

                if self.pa_make_transition(sentence_aux, new_stack): return True

            return False
