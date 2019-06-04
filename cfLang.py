# description: "Projeto da disciplina de Linguagens Formais 2019.1"
# authors:
#     "Arthur Mesquita Pickcius",
#     "Francisco Luiz Vicenzi",
#     "Joao Fellipe Uller"
# Copyright 2019


class ContextFreeGrammar:
    def __init__(self, nonterminals, terminals, productions, start_symbol, accepted_symbol="X"):
        self.nonterminals = nonterminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol
        self.accepted_symbol = accepted_symbol
