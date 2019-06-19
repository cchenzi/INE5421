# description: "Projeto da disciplina de Linguagens Formais 2019.1"
# authors:
#     "Arthur Mesquita Pickcius",
#     "Francisco Luiz Vicenzi",
#     "Joao Fellipe Uller"
# Copyright 2019
import copy

class ContextFreeGrammar:
    def __init__(self, nonterminals, terminals, productions, start_symbol):
        self.nonterminals = nonterminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol
        self.first = self.calc_firsts()
        self.follow = self.calc_follows()

    def rec_first(self, symbol: str, ttl: int) -> set:
        if ttl == 0:
            print("WARNING (ContextFreeGrammar First): loop detected")
            return set()
        ttl -= 1

        if symbol in self.terminals or symbol == "&":
            return set(symbol)

        first = set()
        if symbol in self.nonterminals:
            for production in self.productions[symbol]:
                for symb in production:
                    s_first = self.rec_first(symb, ttl)
                    first.update(s_first)
                    if "&" not in s_first:
                        break
            return first
        else:
            raise Exception("ERROR (ContextFreeGrammar First): unexpected symbol")

    # If x is a terminal, then FIRST(x) = { ‘x’ }
    # If x-> Є, is a production rule, then add Є to FIRST(x).
    # If X->Y1 Y2 Y3….Yn is a production,
    #     FIRST(X) = FIRST(Y1)
    #     If FIRST(Y1) contains Є then FIRST(X) = { FIRST(Y1) – Є } U { FIRST(Y2) }
    #     If FIRST (Yi) contains Є for all i = 1 to n, then add Є to FIRST(X).

    def calc_firsts(self):
        first = {}
        last_first = {}

        def production_first(production, pos, first):
            p_first = {"&"}
            while pos != len(production):
                p_first.update(first[production[pos]])
                if "&" not in first[production[pos]]:
                    p_first.discard("&")
                    break
                pos += 1
            return p_first

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
                    if production == '&':
                        first[non_terminal].add(production)
                    else:
                        for pos, symbol in enumerate(production):
                            if symbol in self.terminals:
                                first[symbol] = [symbol]
                                first[non_terminal].add(symbol)
                                break
                            elif symbol in self.nonterminals:
                                first[non_terminal].update(
                                    production_first(production, pos, first)
                                )
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

    def calc_follows(self):
        def production_first(production, pos):
            first = {"&"}
            while pos != len(production):
                first.update(self.first[production[pos]])
                if "&" not in self.first[production[pos]]:
                    first.discard("&")
                    break
                pos += 1
            return first

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
                                    production_first(production, pos + 1)
                                )
                                follow[symbol].discard("&")
                                if "&" in production_first(production, pos + 1):
                                    if symbol == "k":
                                        pass
                                    follow[symbol].update(follow[non_terminal])

        # to list
        follow_list = {}
        for symbol, nt_follow in follow.items():
            follow_list[symbol] = list(nt_follow)
        return follow_list
