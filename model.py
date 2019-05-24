# description: "Projeto da disciplina de Linguagens Formais 2019.1"
# authors:
#     "Arthur Mesquita Pickcius",
#     "Francisco Luiz Vicenzi",
#     "Joao Fellipe Uller"
# Copyright 2019
import copy


class NFA:
    def __init__(
        self, states, alphabet, init_state, final_states, transitions, has_epsilon
    ):
        self.states = states
        self.alphabet = alphabet
        self.final_states = final_states
        self.transitions = transitions
        self.init_state = init_state
        self.current_state = init_state
        self.epsilonEnabled = has_epsilon
        self.dead_state = "qdead"
        self.determinized = None
        self.epsilon_closure = dict.fromkeys(transitions)

    def make_transition(self, symbol):
        print(f"Current state before: {self.current_state} | Symbol: {symbol}")
        aux = self.transitions[self.current_state][symbol]
        self.current_state = self.dead_state if aux == "" else aux
        print(f"Current state after: {self.current_state}")

    def reset_init_state(self):
        self.current_state = self.init_state

    def is_word_input_valid(self, word_input):
        if not (self.determinized):
            self.determinized = self.determinize()
        return self.determinized.is_word_input_valid(word_input)

    def compute_epsilon_closure(self):
        for k, tr in self.transitions.items():
            if ("&" in tr) and (tr["&"] != []):
                aux = []
                aux.append(k)
                for state in tr["&"]:
                    if state not in aux and state in self.states:
                        aux.append(state)
                    for y in aux:
                        if y in self.states:
                            for epsilon_states in self.transitions[y]["&"]:
                                if (
                                    epsilon_states not in aux
                                    and epsilon_states in self.states
                                ):
                                    aux.append(epsilon_states)
                # print(aux)
                self.epsilon_closure[k] = sorted(list(set(aux)))
            elif k in self.states:
                self.epsilon_closure[k] = [k]
            else:
                self.epsilon_closure = []

    def determinize(self):
        self.compute_epsilon_closure()
        print(f"\nepsilon closure: {self.epsilon_closure}")
        index = 0
        new_states = {}
        state_queue = [self.epsilon_closure[self.init_state]]
        new_transitions = {}

        # enquanto houverem estados para serem avaliados
        while bool(state_queue):
            new_states[f"q{index}"] = state_queue.pop()
            new_transitions[f"q{index}"] = {}

            # inicializa a lista de transições
            for symbol_sa in self.alphabet:
                new_transitions[f"q{index}"][symbol_sa] = set()

            # pega cada estado do novo estado sendo avaliado
            for state in new_states[f"q{index}"]:
                if state in self.states:
                    # pega o fecho desse estado
                    for cls in self.epsilon_closure[state]:

                        # pega o simbolo e os estados-alvo de cada transicao
                        for symbol, t_state in self.transitions[cls].items():
                            if symbol in self.alphabet:
                                # junta os estados que farao parte do
                                # novo estado determinizado
                                closure = set()

                                # pega o fecho de cada estado na lista de
                                # estados-alvo da transicao
                                for cs in t_state:
                                    if cs in self.states:
                                        closure.update(self.epsilon_closure[cs])
                                new_transitions[f"q{index}"][symbol].update(closure)
                                nt = new_transitions[f"q{index}"][symbol]

                                # coloca a lista de estados que se tornarao
                                # um novo estado na fila
                                if (
                                    bool(nt)
                                    and not any(
                                        nt == set(nsv) for nsv in new_states.values()
                                    )
                                    and not any(nt == set(sq) for sq in state_queue)
                                ):
                                    state_queue.append(sorted(list(nt)))
                                    # print(f'state_queue: {state_queue}')
            index += 1

        print(f"new_states: {new_states}")
        # update states and set final states
        final_states = set()
        for state, old_states in new_states.items():
            if any(os in self.final_states for os in old_states):
                final_states.add(state)
            for symbol in self.alphabet:
                for new_s, old_s in new_states.items():
                    if new_transitions[state][symbol] == old_s:
                        new_transitions[state][symbol] = sorted(list(new_s))

        # troca as listas de estados pelo nome dos novos estados
        new_tr = {}
        aux = []
        for x in new_states.values():
            aux.append(str(sorted(x)))
        states_dict = dict(zip(aux, new_states.keys()))

        for state, transition in new_transitions.items():
            new_tr[state] = {}
            for symbol in transition:
                aux_tr = sorted(list(new_transitions[state][symbol]))
                if aux_tr != []:
                    new_tr[state][symbol] = states_dict[str(aux_tr)]
                else:
                    new_tr[state][symbol] = "-"

        # coloca os estados no formato da saida
        states = []
        for s in new_states:
            states.append(s)

        print(f"final states: {sorted(list(final_states))}")
        print(f"states: {states}")
        print(f"\ntransitions: {new_tr}\n")
        return DFA(states, self.alphabet, "q0", sorted(list(final_states)), new_tr)


class DFA:
    def __init__(self, states, alphabet, init_state, final_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.final_states = final_states
        self.transitions = transitions
        self.init_state = init_state
        self.current_state = init_state
        self.dead_state = "qdead"

    def make_transition(self, symbol):
        print("Current state before: ", self.current_state, "| Symbol: ", symbol)
        if symbol not in list(self.transitions[self.init_state].keys()):
            self.current_state = self.dead_state
        else:
            aux = self.transitions[self.current_state][symbol]
            self.current_state = self.dead_state if aux == "" else aux
        print("Current state after: ", self.current_state)

    def reset_init_state(self):
        self.current_state = self.init_state

    def is_word_input_valid(self, word_input):
        self.reset_init_state()
        print("\nStarting to check if", word_input, "is valid...")
        for x in word_input:
            self.make_transition(x)
            if self.current_state == self.dead_state:
                break
        print("End state: ", self.current_state)
        return True if self.current_state in self.final_states else False

    def to_grammar(self):
        productions = {k: {} for k in self.states}
        for k, x in self.transitions.items():
            aux = []
            for q, t in x.items():
                aux.append(q + t)
                if t in self.final_states:
                    aux.append(q)
            productions[k] = aux
        return RegularGrammar(
            list(self.transitions.keys()), self.alphabet, productions, self.init_state
        )

    def minimize(self):
        self.discard_dead()
        self.discard_unreachable()

    def discard_dead(self):
        alive_states = set(self.final_states)

        for start_state in self.states:
            if start_state not in alive_states:
                for state in self.states:
                    if alive_states.intersection(set(self.transitions[state].values())):
                        alive_states.add(state)

        self.states = list(alive_states)

    def discard_unreachable(self):
        reachable = set()

        def recursive_reachable(current_state):
            for state in self.transitions[current_state].values():
                if state not in reachable:
                    reachable.add(state)
                    recursive_reachable(state)

        recursive_reachable(self.init_state)
        self.states = list(reachable)


class RegularGrammar:
    def __init__(
        self, nonterminals, terminals, productions, start_symbol, accepted_symbol="X"
    ):
        self.nonterminals = nonterminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol
        self.accepted_symbol = accepted_symbol

    def toNFA(self):
        nt = copy.deepcopy(self.nonterminals)
        nt.append(self.accepted_symbol)
        nfaD = {k: {} for k in nt}
        for k, x in self.productions.items():
            trD = {k: [] for k in self.terminals}
            for y in x:
                trD[y[0]].append(self.accepted_symbol) if y in self.terminals else trD[
                    y[0]
                ].append(y[1])
            nfaD[k] = trD
        nfaD[self.accepted_symbol] = {k: [] for k in self.terminals}
        # [y.append('qdead') for x in nfaD.values() for y in x.values() if not y]
        return NFA(
            list(nfaD.keys()),
            self.terminals,
            self.start_symbol,
            list(self.accepted_symbol),
            nfaD,
            False,
        )


def test_minimization_alives():
    states = ["S", "A", "B"]
    alphabet = ["a", "b"]
    final_states = ["B"]
    transitions = {
        "S": {"a": "A", "b": "S"},
        "A": {"a": "S", "b": "A"},
        "B": {"a": "A", "b": "B"}
    }

    init_state = "S"
    dfa = DFA(states, alphabet, init_state, final_states, transitions)
    dfa.discard_dead()
    if set(dfa.states) == {"B"}:
        print("Alive yay!!! 1")

    transitions = {
        "S": {"a": "B", "b": "S"},
        "A": {"a": "A", "b": "A"},
        "B": {"a": "A", "b": "B"}
    }
    dfa = DFA(states, alphabet, init_state, final_states, transitions)
    dfa.discard_dead()
    if set(dfa.states) == {"S", "B"}:
        print("Alive yay!!! 2")


def test_minimization_reachables():
    states = ["S", "A", "B"]
    alphabet = ["a", "b"]
    final_states = ["A", "B"]
    transitions = {
        "S": {"a": "A", "b": "S"},
        "A": {"a": "S", "b": "A"},
        "B": {"a": "A", "b": "B"},
    }

    init_state = "S"
    dfa = DFA(states, alphabet, init_state, final_states, transitions)
    dfa.discard_unreachable()
    print(dfa.states)
    if set(dfa.states) == {"S", "A"}:
        print("Reachable yay!!! 1")


def test_determinization():
    states = ["S", "A", "B", "C", "X"]
    alphabet = ["a", "b"]
    final_states = ["S", "X"]
    transitions = {
        "S": {"a": ["A"], "b": ["C", "X"]},
        "A": {"a": ["B"], "b": ["A"]},
        "B": {"a": ["C", "X"], "b": ["B"]},
        "C": {"a": ["A"], "b": ["C", "X"]},
        "X": {"a": [], "b": []},
    }
    init_state = "S"
    a1 = NFA(states, alphabet, init_state, final_states, transitions, False)
    a1.determinize()

    states = ["p", "q", "r"]
    alphabet = ["a", "b", "c"]
    init_state = "p"
    final_states = ["r"]
    transitions = {
        "p": {"a": ["p"], "b": ["q"], "c": ["r"], "&": []},
        "q": {"a": ["q"], "b": ["r"], "c": [], "&": ["p"]},
        "r": {"a": ["r"], "b": [], "c": ["p"], "&": ["q"]},
    }

    a2 = NFA(states, alphabet, init_state, final_states, transitions, True)
    a2.determinize()

    transitions = {
        "p": {"a": [], "b": ["q"], "c": ["r"], "&": ["q"]},
        "q": {"a": ["p"], "b": ["r"], "c": ["p", "q"], "&": []},
        "r": {"a": [], "b": [], "c": [], "&": []},
    }
    a3 = NFA(states, alphabet, init_state, final_states, transitions, True)
    a3.determinize()


if __name__ == "__main__":
    test_minimization_alives()
    print('----------------------')
    test_minimization_reachables()
