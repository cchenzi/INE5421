# description: "Projeto da disciplina de Linguagens Formais 2019.1"
# authors:
#     "Arthur Mesquita Pickcius",
#     "Francisco Luiz Vicenzi",
#     "Joao Fellipe Uller"
# Copyright 2019
import copy
from graphviz import Digraph


class NFA:
    def __init__(self, states, alphabet, init_state, final_states, transitions, has_epsilon):
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
        self.draw()
        return self.determinized.is_word_input_valid(word_input)

    def draw(self):
        automata = Digraph(comment='NFA')
        for from_state in self.transitions:
            for letter, states in self.transitions[from_state].items():
                for to_state in states:
                    if to_state != '':
                        automata.edge(from_state, to_state, label=letter)
        for x in self.final_states:
            automata.node(x, shape='doublecircle')
        # ???
        automata.view()

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

    def draw(self):
        automata = Digraph(comment='DFA')
        for from_state in self.transitions:
            for letter, to_state in self.transitions[from_state].items():
                if to_state != '':
                    automata.edge(from_state, to_state, label=letter)
        for x in self.final_states:
            automata.node(x, shape='doublecircle')
        # ???
        automata.view()

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
        self.discard_unreachable()
        self.discard_dead()
        self.group_equivalent()

    def discard_dead(self):
        last_alive_states = set()
        alive_states = set(self.final_states)

        while last_alive_states != alive_states:
            last_alive_states = alive_states.copy()
            for state in self.states:
                if state not in alive_states and alive_states.intersection(
                    set(self.transitions[state].values())
                ):
                    alive_states.add(state)

        if self.init_state not in alive_states:
            print("ERROR: init state is DEAD!")
        dead_states = set(self.states).difference(alive_states)
        for dead_state in dead_states:
            self.transitions.pop(dead_state)
        self.states = list(alive_states)

    def discard_unreachable(self):
        reachable = set()

        def recursive_reachable(current_state):
            for state in self.transitions[current_state].values():
                if state not in reachable and state in self.states:
                    reachable.add(state)
                    recursive_reachable(state)

        recursive_reachable(self.init_state)

        unreachable = set(self.states).difference(reachable)
        for state in unreachable:
            self.transitions.pop(state)
            if state in self.final_states:
                self.final_states.remove(state)
        if not self.final_states:
            print("ERROR: No final states!")
        self.states = list(reachable)

    def group_equivalent(self):
        print(f"states: {self.states}")
        final_states = set(self.final_states)
        non_final_states = set(self.states).difference(final_states)

        classes = [non_final_states, final_states]
        last_classes = []

        def find_class(state: str) -> set:
            for eclass in last_classes:
                if state in eclass:
                    return eclass.copy()
            return None

        def copy_classes(classes):
            cpy = []
            for cclass in classes:
                cpy.append(cclass.copy())
            return cpy

        def remove_state(state, classes):
            for inner_class in classes:
                if state in inner_class:
                    inner_class.remove(state)
            new_classes = []
            for cl in classes:
                if cl:
                    new_classes.append(cl)
            return new_classes

        while classes != last_classes:
            last_classes = copy_classes(classes)
            for symbol in self.alphabet:
                for eclass in last_classes:
                    relations = []

                    for state in eclass:
                        target_class = find_class(self.transitions[state][symbol])
                        on_list = False

                        classes = remove_state(state, classes)

                        for row in relations:  # Row[0]=state Row[1]=target class
                            if target_class == row[1]:
                                on_list = True

                                for inner_class in classes:
                                    if row[0] in inner_class:
                                        inner_class.add(state)
                        if not on_list:
                            classes.append({state})
                        relations.append([state, target_class])
        print(f"classes: {classes}")

        self.states = []
        for group in classes:
            new_state = None
            if self.init_state in group:
                new_state = self.init_state
            else:
                new_state = group.pop()
            for st, trs in self.transitions.items():
                for symbol in trs:
                    if self.transitions[st][symbol] in group:
                        self.transitions[st][symbol] = new_state
            self.states.append(new_state)

        dead = set(self.transitions).difference(set(self.states))
        for state in dead:
            self.transitions.pop(state)
            if state in self.final_states:
                self.final_states.remove(state)

        print(f"classes: {classes}")


class RegularGrammar:
    def __init__(self, nonterminals, terminals, productions, start_symbol, accepted_symbol="X"):
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

    # Retorna true se for regular, falso caso contrário
    def check_type(self):
        error = False
        for non, prods in self.productions.items():
            for x in prods:
                if len(x) > 2:
                    error = True
                    print(x)
                    break
                if len(x) > 1:
                    if x[0] not in self.terminals:
                        error = True
                        print(x)
                        break
                    if x[1] not in self.nonterminals:
                        error = True
                        print(x)
                        break
                else:
                    if x not in self.terminals:
                        error = True
                        print(x)
                        break
        return !error


def union(automata_1, automata_2):
    # Quantidade de estados novos = velhos + inicial + final
    tr_len = len(automata_1.transitions) + len(automata_2.transitions) + 2
    
    # Unindo alfabetos e adicionando epsilon
    new_ab = automata_1.alphabet + automata_2.alphabet
    if '&' not in new_ab:
        new_ab.append('&')
    new_ab = list(set(new_ab))
    new_states = []
    
    # Criando e convertendo transições para os novos estados
    transition_conversion_1, transition_conversion_2, new_states = create_conversion(automata_1.transitions, automata_2.transitions, tr_len, True)
    tr1_converted = convert_transitions(automata_1.transitions, transition_conversion_1, automata_1.init_state)
    tr2_converted = convert_transitions(automata_2.transitions, transition_conversion_2, automata_2.init_state)
    
    # Une ambas as transições
    new_transitions = to_transitions(tr1_converted, tr2_converted, new_states, new_ab)
    
    # Adicionando inicial e final
    new_states.append('q0')
    new_states.append('qf')
    
    # Transição por epsilon de q0 para os respectivos estados iniciais
    new_transitions['q0'] = dd_aux = {k: [] for k in new_ab}
    new_transitions['q0']['&'].append(transition_conversion_1[automata_1.init_state])
    new_transitions['q0']['&'].append(transition_conversion_2[automata_2.init_state])
    
    
    
    # Transição por epsilon dos estados finais para o estado final qf
    new_transitions = append_final_states(new_transitions, transition_conversion_1, automata_1.final_states, 'qf')
    new_transitions = append_final_states(new_transitions, transition_conversion_2, automata_2.final_states, 'qf')
    
    return NFA(new_states, new_ab, ['q0'], ['qf'], new_transitions, True)


def concatenation(automata_1, automata_2):
    tr_len = len(automata_1.transitions) + len(automata_2.transitions)
    
    # Unindo alfabetos e adicionando epsilon
    new_ab = automata_1.alphabet + automata_2.alphabet
    if '&' not in new_ab:
        new_ab.append('&')
    new_ab = list(set(new_ab))
    new_states = []
    # Criando e convertendo transições para os novos estados
    transition_conversion_1, transition_conversion_2, new_states = create_conversion(automata_1.transitions, automata_2.transitions, tr_len, False)
    tr1_converted = convert_transitions(automata_1.transitions, transition_conversion_1, automata_1.init_state)
    tr2_converted = convert_transitions(automata_2.transitions, transition_conversion_2, automata_2.init_state)
    
    # Une ambas as transições
    new_transitions = to_transitions(tr1_converted, tr2_converted, new_states, new_ab)
    
    # Transição por epsilon dos estados finais de dfa1 para o estado inicial de dfa2
    init_2 = transition_conversion_2[automata_2.init_state]
    new_transitions = append_final_states(new_transitions, transition_conversion_1, automata_1.final_states, init_2)
    
    new_init = transition_conversion_1[automata_1.init_state]
    new_final = []
    for x in automata_2.final_states:
        new_final.append(transition_conversion_2[x])
    
    return NFA(new_states, new_ab, new_init, new_final, new_transitions, True)
    

def convert_transitions(transitions, transition_conversion, init_state):
    alphabet = list(transitions[init_state].keys())
    tr_converted = {k: {} for k in list(transitions.keys())}

    for k, x in transitions.items():
        internal_tr = {k: '' for k in alphabet}
        for letter in alphabet:
            aux = transitions[k][letter]
            if type(aux) == list:
                for aux_2 in aux:
                    if aux_2 != '':
                        internal_tr[letter] = transition_conversion[aux_2]
            else:
                if aux != '':
                    internal_tr[letter] = transition_conversion[aux] 
        tr_converted[k] = internal_tr
    
    return tr_converted


def append_final_states(transitions, transition_conversion, final_states, state_to_append):
    for x in final_states:
        print(x)
        transitions[transition_conversion[x]]['&'].append(state_to_append)
    return transitions
        

def create_conversion(transitions_1, transitions_2, tr_len, goal):
    # goal True = union, False = concatenation
    if (goal):
        begin = 1
        end = tr_len - 1
    else:
        begin = 0
        end = tr_len
    
    c = 0
    d = 0
    transition_conversion_1 = {}
    transition_conversion_2 = {}
    new_states = []

    for x in range(begin, end):
        state = 'q' + str(x)
        new_states.append(state)
        if (c < len(transitions_1)):
            transition_conversion_1[state] = list(transitions_1.keys())[c]
            c += 1
        else:
            transition_conversion_2[state] = list(transitions_2.keys())[d]
            d += 1
    transition_conversion_1 = dict((v,k) for k, v in transition_conversion_1.items())
    transition_conversion_2 = dict((v,k) for k, v in transition_conversion_2.items())
    
    return transition_conversion_1, transition_conversion_2, new_states


def to_transitions(tr1_converted, tr2_converted, new_states, new_ab):
    all_trs = [tr1_converted, tr2_converted]
    print('1: ', tr1_converted)
    print('2: ', tr2_converted)
    transitions = {k: {} for k in new_states}
    count = 0
    for tr_aux in all_trs:
        for key, tr in tr_aux.items():
            print(count)
            dd_aux = {k: [] for k in new_ab}
            for letter, state in tr.items():
                if state != '':
                    dd_aux[letter].append(state)
            transitions[new_states[count]] = dd_aux
            count += 1
    return transitions


def test_minimization_alives():
    states = ["S", "A", "B"]
    alphabet = ["a", "b"]
    final_states = ["B"]
    transitions = {
        "S": {"a": "A", "b": "S"},
        "A": {"a": "S", "b": "A"},
        "B": {"a": "A", "b": "B"},
    }

    init_state = "S"
    dfa = DFA(states, alphabet, init_state, final_states, transitions)
    dfa.discard_dead()
    if set(dfa.states) == {"B"}:
        print("Alive yay!!! 1")

    transitions = {
        "S": {"a": "B", "b": "S"},
        "A": {"a": "A", "b": "A"},
        "B": {"a": "A", "b": "B"},
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


def test_group_equivalent():
    states = ["S", "A", "B", "C"]
    alphabet = ["a", "b"]
    final_states = ["A", "B"]
    transitions = {
        "S": {"a": "A", "b": "S"},
        "A": {"a": "A", "b": "B"},
        "B": {"a": "A", "b": "B"},
        "C": {"a": "A", "b": "S"},
    }

    init_state = "S"
    dfa = DFA(states, alphabet, init_state, final_states, transitions)
    dfa.group_equivalent()
    print(dfa.states)
    if set(dfa.states) == {"S", "A"}:
        print("Group yay!!! 1")


def test_minimization():
    print("\nTest minimization:")
    states = ["A", "B", "C", "D", "E", "F", "G", "H"]
    alphabet = ["0", "1"]
    final_states = ["A", "D", "G"]
    transitions = {
        "A": {"0": "G", "1": "B"},
        "B": {"0": "F", "1": "E"},
        "C": {"0": "C", "1": "G"},
        "D": {"0": "A", "1": "H"},
        "E": {"0": "E", "1": "A"},
        "F": {"0": "B", "1": "C"},
        "G": {"0": "G", "1": "F"},
        "H": {"0": "H", "1": "D"},
    }

    init_state = "A"
    dfa = DFA(states, alphabet, init_state, final_states, transitions)
    dfa.minimize()
    print(dfa.states)


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
    # test_minimization_alives()
    # print('----------------------')
    # test_minimization_reachables()
    # print('----------------------')
    # test_group_equivalent()
    test_minimization()
