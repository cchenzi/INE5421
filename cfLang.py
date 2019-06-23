# description: "Projeto da disciplina de Linguagens Formais 2019.1"
# authors:
#     "Arthur Mesquita Pickcius",
#     "Francisco Luiz Vicenzi",
#     "Joao Fellipe Uller"
# Copyright 2019

import copy
import random


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


    # removes unitary productions from the grammar
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


    # remove dead productions from the grammar
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


    # remove improductive production from the grammar
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


    # Chomsky Normal Form
    def create_terminals_transitions(self, letters):
        count = 0
        new_t = []
        while (count != len(self.terminals)):
            rd = random.randint(0,len(letters) - 1)
            random_letter = letters[rd]
            if (random_letter not in self.nonterminals):
                new_t.append(random_letter)
                count += 1
                letters.remove(random_letter)
        terminals_transitions = dict(zip(self.terminals, new_t))
        real_transitions = dict(zip(new_t, self.terminals))
        return terminals_transitions, real_transitions, letters

    def check_len_productions(self):
        for nt, prods in self.productions.items():
            for symbols in prods:
                if(len(symbols) > 2):
                    return True
        return False

    def change_terminal_productions(self, terminals_transitions):
        for nt, prods in self.productions.items():
            prod_aux = []
            for symbols in prods:
                if(len(symbols) > 1):
                    aux = ''
                    print(symbols)
                    for x in symbols:
                        if x in self.terminals:
                            aux = aux + terminals_transitions[x]
                        else:
                            aux = aux + x
                    print(symbols, '-> ', aux)
                    prod_aux.append(aux)
                else:
                    prod_aux.append(symbols)
                self.productions[nt] = prod_aux
        return self.productions

    def check_epsilon_productions(self):
        productions_epsilon = []
        for nt, prods in self.productions.items():
            for symbols in prods:
                if symbols == '&':
                    print(f'Epsilon found in {nt}!')
                    productions_epsilon.append(nt)
        return productions_epsilon

    def remove_epsilon_productions(self):
        letters = [chr(x) for x in range(ord('A'), ord('A')+26)]
        epsilons = self.check_epsilon_productions()
        grr = False
        while epsilons != []:
            aux_aux = []
            for nt in self.nonterminals:
                to_add = []
                for x in epsilons:
                    for symbols in self.productions[nt]:
                        if x in symbols:
                            indexes = [pos for pos, char in enumerate(symbols) if char == x]
                            for y in indexes:
                                aux = list(symbols)
                                aux.pop(y)
                                aux = ''.join(aux)
                                to_add.append(aux)
                    for y in to_add:
                        print(nt, y)
                        if y == '':
                            self.productions[nt].append('&')
                            aux_aux.append(nt)
                        else:
                            if y not in self.productions[nt]:
                                self.productions[nt].append(y)
                    if '&' in self.productions[nt]:
                        self.productions[nt].remove('&')
            for x in aux_aux:
                self.productions[x].append('&')
                if x == self.start_symbol:
                    grr = True
            print(self.productions)
            epsilons = self.check_epsilon_productions()

        if grr:
            rd = self.get_new_nonterminal(letters)
            letters.remove(rd)
            self.nonterminals.append(rd)
            self.productions[rd] = [self.start_symbol, '&']
            self.start_symbol = rd
        print('Without epsilon: ', self.productions)

    # Main function that controls the process of chomsky normalization
    def to_normal_form(self):
        self.remove_improductive_rules()
        self.remove_unreachable_rules()
        self.remove_epsilon_productions()
        self.remove_left_recursion()
        self.remove_unit_rules()

        print('Starting naive transformation to Chomsky Normal Form')
        full_alphabet = [chr(x) for x in range(ord('A'), ord('A')+26)]
        new_productions = {}
        terminals_transitions, real_transitions, full_alphabet = self.create_terminals_transitions(full_alphabet)
        print('Terminal transitions: ', terminals_transitions)
        self.productions = {**self.productions, **real_transitions}
        print('Before change: ', self.productions)
        self.productions = self.change_terminal_productions(terminals_transitions)

        print('Changed: ', self.productions)
        keep_processing = self.check_len_productions()
        while (keep_processing):
            for nt, prod in self.productions.items():
                for symbols in prod:
                    if(len(symbols) > 2):
                        print('Key: ', nt, 'Symbols:', symbols)
                        random_letter = self.get_new_nonterminal(full_alphabet)
                        self.nonterminals.append(random_letter)
                        full_alphabet.remove(random_letter)
                        new_prod = symbols[0] + random_letter
                        aux = symbols[1:]
                        prod.remove(symbols)
                        prod.append(new_prod)
                        print('Updated: ', self.productions[nt])
                        if random_letter not in list(new_productions):
                            new_productions[random_letter] = []
                            new_productions[random_letter].append(aux)
                        else:
                            new_productions[random_letter].append(aux)
            self.productions = {**self.productions, **new_productions}
            keep_processing = self.check_len_productions()

        print('Final:', self.productions)

    def get_new_nonterminal(self, letters):
        while True:
            rd = random.randint(0,len(letters) - 1)
            random_letter = letters[rd]
            if (random_letter not in self.nonterminals):
                return random_letter

    def check_indirect_recursion(self, nt):
        dd = {}
        for prod in self.productions[nt]:
            if prod[0] != nt:
                if prod[0] in list(self.productions):
                    aux = self.productions[prod[0]]
                    for y in aux:
                        if y[0] == nt:
                            if prod[0] not in list(dd):
                                dd[prod[0]] = []
                            dd[prod[0]].append(y)
                            print(f'Indirect in {prod} with {y}! ({nt}, {prod[0]})')
        return dd

    def remove_indirect_recursion(self, dd, nt):
        print('Indirect recursions: ', dd)
        for k, v in dd.items():
            new_prods = []
            to_remove = []
            for x in v:
                to_remove.append(x)
                for master_productions in self.productions[nt]:
                    new_prods.append(master_productions+x[1:])
            print(f'To remove: {to_remove}, New prods became: {new_prods}')
            for x in to_remove:
                self.productions[k].remove(x)
            for x in new_prods:
                self.productions[k].append(x)

    def check_left_recursion(self):
        to_remove = {}
        to_help = {}
        aux = False
        for nt, prods in self.productions.items():
            to_remove[nt] = []
            to_help[nt] = []
            for symbols in prods:
                if symbols[0] == nt:
                    to_remove[nt].append(symbols)
                    aux = True
                    print('LEFT HERE: ', symbols)
                else:
                    to_help[nt].append(symbols)
        return aux, to_remove, to_help

    def remove_left_recursion(self):
        checkage, to_remove, to_help = self.check_left_recursion()
        letters = [chr(x) for x in range(ord('A'), ord('A')+26)]
        print('ANTES: ', checkage, to_remove, to_help)
        count = 0
        while checkage:
            for nt, prods in to_remove.items():
                if prods != []:
                    new_nt = self.get_new_nonterminal(letters)
                    self.nonterminals.append(new_nt)
                    letters.remove(new_nt)
                    self.productions[new_nt] = []
                    prodsx = to_remove[nt]  # MAIOR GAMBIARRA DO UNIVERSO KKKKKKKKKKKKKKKKKK
                    print('For ', nt, ': ', prodsx)
                    for symbols in prodsx:
                        aux = symbols[1:]
                        self.productions[nt].remove(symbols)
                        for helper in to_help[nt]:
                            if helper in self.productions[nt]:
                                self.productions[nt].remove(helper)
                            aux1 = helper+new_nt
                            aux2 = aux+new_nt
                            if aux1 not in self.productions[nt]:
                                self.productions[nt].append(aux1)
                            if aux2 not in self.productions[new_nt]:
                                self.productions[new_nt].append(aux2)
                        if '&' not in self.productions[new_nt]:
                            self.productions[new_nt].append('&')
                    print(f'Productions before indirect checkage: {self.productions}')

                indirect_recursions = self.check_indirect_recursion(nt)
                self.remove_indirect_recursion(indirect_recursions, nt)
                checkage, to_remove, to_help = self.check_left_recursion()
            count += 1

        print(self.productions)

    def scan(self, s1, s2, dd, combination):
        len_aux = len(s2) if len(s1) > len(s2) else len(s1)
        total = ''
        print(f'Scanning {s1}, {s2}...')
        f1 = s1[0]
        f2 = s2[0]
        for i in range(0, len_aux):
            lt = s1[i]
            if lt == s2[i]:
                total += lt
                if f1 not in combination:
                    combination[f1] = set()
                if total not in dd:
                    dd[total] = set()
                dd[total].add(s1)
                dd[total].add(s2)
                combination[f1].add(total)
            else:
                break
        return dd, combination

    def get_max_prefixes(self, d1, c1):
        prefixes = []
        for k, v in c1.items():
            max_v = 0  # maior numero de valores em um conjunto
            max_cb = 0  # maior tamanho da combinação
            nt = ''
            for x in v:
                aux = len(d1[x])
                aux2 = len(x)
                if aux == max_v and aux2 > max_cb:
                    nt = x
                    max_v = aux
                    max_cb = aux2
                if aux > max_v and aux2 > max_cb:
                    nt = x
                    max_v = aux
                    max_cb = aux2
            prefixes.append(nt)
        return prefixes

    def get_factored_transitions(self, prefixes, d1, len_nt):
        count = 0
        new_transitions = {}
        for prefix in prefixes:
            to_change = d1[prefix]
            print(len_nt+count, self.nonterminals)
            new_nt = self.nonterminals[len_nt+count]
            qr = []
            qr.append(prefix+new_nt)  # novo simbolo
            new_transitions[prefix] = qr
            print(to_change)
            for s in to_change:
                new_symbols = s[len(prefix):]
                new_symbols = s[len(prefix):] if s[len(prefix):] != '' else '&'
                print(f'INTERNO: {s}, {new_symbols}')
                if new_nt not in new_transitions:
                    new_transitions[new_nt] = []
                new_transitions[new_nt].append(new_symbols)
            count += 1
        return new_transitions

    def check_left_factoring(self, aux, key):
        count = 1
        dd = {}
        combination = {}
        for x in aux:
            for y in aux[count:]:
                dd, combination = self.scan(x, y, dd, combination)
            count += 1
        return key, dd, combination

    def check_all_factoring(self, prod):
        to_left_factor = []
        for key in list(prod):
            result = self.check_left_factoring(prod[key], key)
            if result[1] != {}:
                to_left_factor.append(result[0])
        return to_left_factor

    def do_left_factoring(self):
        letters = [chr(x) for x in range(ord('A'), ord('A')+26)]
        to_left_factor = self.check_all_factoring(self.productions)
        while to_left_factor != []:
            print(f'Remove from {to_left_factor}')
            for key in to_left_factor:
                print(f'Doing for {key}...')
                ignore, d1, c1 = self.check_left_factoring(self.productions[key], key)
                if d1 != {}:
                    prefixes = self.get_max_prefixes(d1, c1)

                    len_nt = len(self.nonterminals)
                    for x in range(0, len(prefixes)):
                        letter = self.get_new_nonterminal(letters)
                        self.nonterminals.append(letter)
                        letters.remove(letter)
                    print('PREFIXES: ', prefixes)

                    new_transitions = self.get_factored_transitions(prefixes, d1, len_nt)
                    prod_aux = copy.deepcopy(self.productions[key])
                    for x in prod_aux:
                        for y in prefixes:
                            print(f'Checking {x} to prefix {y}...')
                            if x[0:len(y)] == y:
                                self.productions[key].remove(x)
                    print(f'Prod after checkage: {self.productions[key]}')
                    for x in prefixes:
                        self.productions[key].append(new_transitions[x][0])
                        new_transitions.pop(x)

                    for k, x in new_transitions.items():
                        self.productions[k] = x
                to_left_factor.remove(key)
                print(f'Now left {to_left_factor}...')
                print(f'Prod now: {self.productions}!')
            to_left_factor = self.check_all_factoring(self.productions)
            print(f'Updated: {to_left_factor}')
        print(self.productions)

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
