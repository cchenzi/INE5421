# description: "Projeto da disciplina de Linguagens Formais 2019.1"
# authors:
#     "Arthur Mesquita Pickcius",
#     "Francisco Luiz Vicenzi",
#     "Joao Fellipe Uller"
# Copyright 2019
import copy
from graphviz import Digraph


class NFA:
    # constructor
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


    # makes a state transition based on current state and entry symbol
    def make_transition(self, symbol):
        print(f"Current state before: {self.current_state} | Symbol: {symbol}")
        aux = self.transitions[self.current_state][symbol]
        self.current_state = self.dead_state if aux == "" else aux
        print(f"Current state after: {self.current_state}")


    # resets the automaton to it's initial state
    def reset_init_state(self):
        self.current_state = self.init_state


    # evaluates if an input is accepted by the automaton
    def is_word_input_valid(self, word_input):
        print(self.transitions)
        if not (self.determinized):
            self.determinized = self.determinize()

        return self.determinized.is_word_input_valid(word_input)


    # draws an automaton
    def draw(self, filename):
        automata = Digraph(comment='NFA', format='png')
        for from_state in self.transitions:
            for letter, states in self.transitions[from_state].items():
                for to_state in states:
                    if to_state != '' and to_state != '-':
                        automata.edge(from_state, to_state, label=letter)
        for x in self.final_states:
            automata.node(x, shape='doublecircle')

        automata.view(filename=filename, cleanup='True')


    # computes epsilon_closure of all states of the automaton
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

                self.epsilon_closure[k] = sorted(list(set(aux)))
            elif k in self.states:
                self.epsilon_closure[k] = [k]
            else:
                self.epsilon_closure = []


    # determinizes a NFA to a DFA
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

#############################################################################################

class DFA:
    # constructor
    def __init__(self, states, alphabet, init_state, final_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.final_states = final_states
        self.transitions = transitions
        self.init_state = init_state
        self.current_state = init_state
        self.dead_state = "qdead"


    # makes a state transition based on current state and entry symbol
    def make_transition(self, symbol):
        print("Current state before: ", self.current_state, "| Symbol: ", symbol)
        if symbol not in list(self.transitions[self.init_state].keys()):
            self.current_state = self.dead_state
        else:
            aux = self.transitions[self.current_state][symbol]
            self.current_state = self.dead_state if aux == "" else aux
        print("Current state after: ", self.current_state)


    def draw(self, filename):
        automata = Digraph(comment='DFA', format='png')
        for from_state in self.transitions:
            for letter, to_state in self.transitions[from_state].items():
                if to_state != '' and to_state != '-':
                    automata.edge(from_state, to_state, label=letter)
        for x in self.final_states:
            automata.node(x, shape='doublecircle')

        automata.view(filename=filename, cleanup='True')


    def reset_init_state(self):
        self.current_state = self.init_state


    def is_word_input_valid(self, word_input):
        self.reset_init_state()
        print(self.transitions)
        print("\nStarting to check if", word_input, "is valid...")
        for x in word_input:
            self.make_transition(x)
            if self.current_state == self.dead_state:
                break
        print("End state: ", self.current_state)
        return True if self.current_state in self.final_states else False


    # returns an equivalent regular grammar to the automaton
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


    # returns the a minimized version of the automaton
    def minimize(self):
        minimized = copy.deepcopy(self)
        minimized.discard_unreachable()
        minimized.discard_dead()
        minimized.group_equivalent()

        return minimized


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
            self.init_state = ''
        dead_states = set(self.states).difference(alive_states)
        for dead_state in dead_states:
            self.transitions.pop(dead_state)
        self.states = list(alive_states)


    def discard_unreachable(self):
        reachable = {self.init_state}
        last_reachable = set()

        while reachable != last_reachable:
            last_reachable = reachable.copy()
            for state in self.states:
                if state in reachable:
                    for val in self.transitions[state].values():
                        if val in self.states:
                            reachable.add(val)

        unreachable = set(self.states).difference(reachable)
        for state in unreachable:
            self.transitions.pop(state)
            if state in self.final_states:
                self.final_states.remove(state)
        self.states = list(reachable)
        print(f'reachable states: {reachable}')


    def group_equivalent(self):
        final_states = set(self.final_states)
        non_final_states = set(self.states).difference(final_states)

        classes = [non_final_states, final_states]
        last_classes = []
        previous_classes = []

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

        while classes != previous_classes:
            previous_classes = copy_classes(last_classes)
            for symbol in self.alphabet:
                last_classes = copy_classes(classes)
                for eclass in last_classes:
                    relations = []

                    for state in eclass:
                        target_class = find_class(self.transitions[state][symbol])
                        on_list = False

                        classes = remove_state(state, classes)

                        for row in relations:  # Row[0]=state Row[1]=target class
                            if target_class == row[1]:  # goes to same class
                                on_list = True

                                # search for the state tha goes to same class
                                for inner_class in classes:
                                    if row[0] in inner_class:
                                        inner_class.add(state)
                        if not on_list:
                            classes.append({state})
                        relations.append([state, target_class])

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

############################################################################################

class RegularGrammar:
    # constructor
    def __init__(self, nonterminals, terminals, productions, start_symbol, accepted_symbol="X"):
        self.nonterminals = nonterminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol
        self.accepted_symbol = accepted_symbol


    # converts a regularGramm to a Non-Deterministic automaton
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

#######################################################################################################

class RegularExpression:
    def __init__(self, description):
        self.description = description

########################################################################################################

# returns the union of two finite automatons
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
    new_transitions['q0'] = {k: [] for k in new_ab}
    new_transitions['qf'] = {k: [] for k in new_ab}
    new_transitions['q0']['&'].append(transition_conversion_1[automata_1.init_state])
    new_transitions['q0']['&'].append(transition_conversion_2[automata_2.init_state])

    # Transição por epsilon dos estados finais para o estado final qf
    new_transitions = append_final_states(new_transitions, transition_conversion_1, automata_1.final_states, 'qf')
    new_transitions = append_final_states(new_transitions, transition_conversion_2, automata_2.final_states, 'qf')

    new_ab = set(new_ab)
    new_ab.discard('&')
    new_ab = list(new_ab)

    return NFA(new_states, new_ab, 'q0', ['qf'], new_transitions, True)


# returns the concatenation of two finite automatons
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

    new_ab = set(new_ab)
    new_ab.discard('&')
    new_ab = list(new_ab)

    return NFA(new_states, new_ab, new_init, new_final, new_transitions, True)


def convert_transitions(transitions, transition_conversion, init_state):
    alphabet = list(transitions[init_state].keys())
    tr_converted = {k: {} for k in list(transitions.keys())}

    for k, x in transitions.items():
        internal_tr = {k: '' for k in alphabet}
        for letter in alphabet:
            aux = transitions[k][letter]
            if type(aux) == set:
                aux_set = []
                for aux_2 in aux:
                    if aux_2 != '':
                        aux_set.append(transition_conversion[aux_2])
                internal_tr[letter] = aux_set
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
    transitions = {k: {} for k in new_states}
    count = 0
    for tr_aux in all_trs:
        for key, tr in tr_aux.items():
            print(count)
            dd_aux = {k: [] for k in new_ab}
            for letter, state in tr.items():
                if type(state) == str and state != '':
                    dd_aux[letter].append(state)
                else:
                    dd_aux[letter] = state
            transitions[new_states[count]] = dd_aux
            count += 1
    return transitions
