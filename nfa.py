from dfa import DFA

class NFA:
    def __init__(self, states, alphabet, init_state, final_states,
                 transitions, has_epsilon):
        self.states = states
        self.alphabet = alphabet
        self.final_states = final_states
        self.transitions = transitions
        self.init_state = init_state
        self.current_state = init_state
        self.epsilonEnabled = has_epsilon
        if has_epsilon:
            self.epsilon_closure = dict.fromkeys(transitions)
        self.dead_state = 'qdead'

    def make_transition(self, symbol):
        print(f'Current state before: {self.current_state} | Symbol: {symbol}')
        aux = self.transitions[self.current_state][symbol]
        self.current_state = self.dead_state if aux == '' else aux
        print(f'Current state after: {self.current_state}')

    def reset_init_state(self):
        self.current_state = self.init_state

    def is_word_input_valid(self, word_input):
        if self.determinized == []:
            if self.epsilonEnabled:
                self.determinized = self.determinize_epsilon()
            else:
                self.determinized = self.determinize()
        return self.determinized.is_word_input_valid(word_input)

    def compute_epsilon_closure(self):
        for k, tr in self.transitions.items():
            aux = []
            aux.append(k)
            for state in tr['&']:
                if state not in aux:
                    aux.append(state)
                for y in aux:
                    for epsilon_states in self.transitions[y]['&']:
                        if epsilon_states not in aux:
                            aux.append(epsilon_states)
            # print(aux)
            self.epsilon_closure[k] = list(set(aux))
        print(self.epsilon_closure)

    def minimize(self):
        self.discard_dead()
        self.discard_unreachable()
        self.determinize_epsilon()

    def discard_dead(self):
        alive_states = []

        def recursive_is_alive(current_state):
            for state in self.states:
                if state not in alive_states and current_state in self.transitions[state].values():
                    alive_states.append(current_state)
                    recursive_is_alive(current_state)
        for final_state in self.final_states:
            recursive_is_alive(final_state)
        self.states = alive_states

    def discard_unreachable(self):
        reachable_states = []

        def recursive_get_reachable(state):
            for transition in self.transitions[state]:
                if all(transition.values() not in reachable_states):
                    reachable_states.append(state)
                    recursive_get_reachable(transition)
        recursive_get_reachable(self.init_state)
        self.states = reachable_states

    def determinize(self):
        index = 0
        new_states = {}
        state_queue = [[self.init_state]]
        new_transitions = {}
        while bool(state_queue):
            new_states[f'q{index}'] = state_queue.pop()
            new_transitions[f'q{index}'] = {}
            for symbol in self.alphabet:
                new_transitions[f'q{index}'][symbol] = set()
            for state in new_states[f'q{index}']:
                for symbol, new_state in self.transitions[state].items():
                    new_transitions[f'q{index}'][symbol].update(new_state)
                    nt = new_transitions[f'q{index}'][symbol]
                    if (bool(nt)
                        and not any(set(nt) == set(nsv) for nsv in new_states.values())
                        and not any(set(nt) == set(sq) for sq in state_queue)):
                        state_queue.append(nt)
            index += 1
        print(f'states: {new_states}')
        # print(new_transitions)
        # update states and set final states
        final_states = set()
        for state, old_states in new_states.items():
            if any(os in self.final_states for os in old_states):
                final_states.add(state)
            for symbol in self.alphabet:
                for new_s, old_s in new_states.items():
                    if new_transitions[state][symbol] == old_s:
                        new_transitions[state][symbol] = list(new_s)
        print(f'transitions: {new_transitions}')
        print(f'final states: {final_states}')
        states = set()
        for s in new_states:
            states.add(s)
        return DFA(states, self.alphabet, 'q0', final_states, new_transitions)

    def determinize_epsilon(self):
        self.compute_epsilon_closure()
        print('epsilon closure ok')
        index = 0
        new_states = {}
        state_queue = [self.epsilon_closure[init_state]]
        new_transitions = {}
        while bool(state_queue):
            new_states[f'q{index}'] = state_queue.pop()
            new_transitions[f'q{index}'] = {}
            for symbol in self.alphabet:
                if symbol != '&':
                    new_transitions[f'q{index}'][symbol] = set()
            for state in new_states[f'q{index}']:
                for cls in self.epsilon_closure[state]:
                    for symbol, t_state in self.transitions[cls].items():
                        if symbol != '&':
                            closure = set()
                            for cs in t_state:
                                closure.update(self.epsilon_closure[cs])
                            new_transitions[f'q{index}'][symbol].update(closure)
                            nt = new_transitions[f'q{index}'][symbol]
                            if (bool(nt)
                                    and not any(nt == set(nsv) for nsv in new_states.values())
                                    and not any(nt == set(sq) for sq in state_queue)):
                                state_queue.append(list(nt))
            index += 1
        print(f'states: {new_states}')
        # print(new_transitions)
        # update states and set final states
        final_states = set()
        for state, old_states in new_states.items():
            if any(os in self.final_states for os in old_states):
                final_states.add(state)
            for symbol in self.alphabet:
                for new_s, old_s in new_states.items():
                    if new_transitions[state][symbol] == old_s:
                        new_transitions[state][symbol] = list(new_s)
        print(f'transitions: {new_transitions}')
        print(f'final states: {final_states}')
        states = []
        for s in new_states:
            states.append(s)
        return DFA(states, self.alphabet, 'q0', final_states, new_transitions)


if __name__ == "__main__":
    states = ['S', 'A', 'B', 'C', 'X']
    alphabet = ['a', 'b']
    final_states = ['S', 'X']
    transitions = {
        'S': {'a': ['A'], 'b': ['C', 'X']},
        'A': {'a': ['B'], 'b': ['A']},
        'B': {'a': ['C', 'X'], 'b': ['B']},
        'C': {'a': ['A'], 'b': ['C', 'X']},
        'X': {'a': [], 'b': []}
    }
    init_state = 'S'
    a1 = NFA(states, alphabet, init_state, final_states, transitions, False)
    a1.determinize()

    states = ['p', 'q', 'r']
    alphabet = ['a', 'b', 'c']
    init_state = 'p'
    final_states = ['r']
    transitions = {
        'p': {'a': ['p'], 'b': ['q'], 'c': ['r'], '&': []},
        'q': {'a': ['q'], 'b': ['r'], 'c': [], '&': ['p']},
        'r': {'a': ['r'], 'b': [], 'c': ['p'], '&': ['q']}
    }

    a2 = NFA(states, alphabet, init_state, final_states, transitions, True)
    a2.determinize_epsilon()

    # result
    # states: {
    #     'q0': ['p'],
    #     'q1': ['p', 'r', 'q'],
    #     'q2': ['p', 'q']
    # }
    # transitions: {
    #     'q0': {'a': {'p'}, 'b': {'p', 'q'}, 'c': {'p', 'r', 'q'}},
    #     'q1': {'a': {'p', 'q', 'r'}, 'b': {'p', 'q', 'r'}, 'c': {'p', 'r', 'q'}},
    #     'q2': {'a': {'p', 'q'}, 'b': {'p', 'q', 'r'}, 'c': {'p', 'r', 'q'}}
    # }
    # final states: {'q1'}

    transitions = {
        'p': {'a': [], 'b': ['q'], 'c': ['r'], '&': ['q']},
        'q': {'a': ['p'], 'b': ['r'], 'c': ['p', 'q'], '&': []},
        'r': {'a': [], 'b': [], 'c': [], '&': []}
    }
    a3 = NFA(states, alphabet, init_state, final_states, transitions, True)
    a3.determinize_epsilon()

