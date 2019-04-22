import copy


class RegularGrammar:
    def __init__(self, nonterminals, terminals, productions, start_symbol,
                 accepted_symbol='X'):
        self.nonterminals = nonterminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol
        self.accepted_symbol = accepted_symbol

    def toNFA(self):
        nt = copy.deepcopy(self.nonterminals)
        nt.append(self.accepted_symbol)
        nfaD = {k: {} for k in nt}
        for k, x in self.procutions.items():
            trD = {k: [] for k in self.terminals}
            for y in x:
                trD[y[0]].append(self.accepted_symbol) if y in self.terminals else trD[y[0]].append(y[1])
            nfaD[k] = trD
        nfaD[self.accepted_symbol] = {k: [] for k in self.terminals}
        [y.append('qdead') for x in nfaD.values() for y in x.values() if not y]
        return nfaD
