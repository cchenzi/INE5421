class NFA:
    def __init__(self, states, alphabet, init_state, final_states,
            transitions, has_epsilon):
        self.states = states
        self.alphabet = alphabet
        self.final_states = final_states
        self.transitions = transitions
        self.init_state = init_state
        self.current_state = init_state
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

    def is_input_valid(self, input):
        self.reset_init_state()
        print(f'\nStarting to check if {input} is valid...')
        for x in input:
            self.make_transition(x)
            if self.current_state == self.dead_state:
                break
        print(f'End state: {self.current_state}')
        return True if self.current_state in self.final_states else False

    def compute_epsilon_closure(self):
        for k, tr in self.transitions.items():
            aux = []
            aux.append(k)
            if tr['&'] not in aux:
                aux.append(tr['&'])
            for y in aux:
                if self.transitions[y]['&'] not in aux:
                    aux.append(self.transitions[y]['&'])
            print(aux)
            self.epsilon_closure[k] = list(set(aux))

    def get_epsilon_transitions(self, state):
        newdd = {key: [] for key in self.alphabet}
        print(self.states)
        for x in self.states:
            print('\n\n')
            print('in: ', x)
            for letter in self.alphabet:
                aux = []
                print('letter: ', letter)
                print('transitions for x: ', self.transitions[x])
                for t in self.transitions[x][letter]:
                    if t != '':
                        aux.append(self.epsilon_closure[t])
                flat_list = [item for sublist in aux for item in sublist]
        for k, x in newdd.items():
            newdd[k] = list(set([item for sublist in newdd[k] for item in sublist]))
        return newdd

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

    def determinize_epsilon(self):
        pass

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
            # new_states = {'q0':['q0']}
            # new_states = {
            #                   'q0': ['q0']
            #                   'q1': ['q0','q1']
            #              }
            for state in new_states[f'q{index}']:
                # state = 'q0'
                # self.transitions[state] = {'0':['q0','q1'], '1':[q2]}
                for symbol, new_state in self.transitions[state].items():
                    # symbol = '0'
                    # new_state = ['q0','q1']
                    new_transitions[f'q{index}'][symbol].update(new_state)
                    if (bool(new_state)
                        and not any(set(new_state) == set(nsv) for nsv in new_states.values())
                        and not any(set(new_state) == set(sq) for sq in state_queue)):
                        state_queue.append(new_state)
            index += 1
        print(new_states)
        # print(new_transitions)
        for state in new_states:
            for symbol in self.alphabet:
                for new_s, old_s in new_states.items():
                    if new_transitions[state][symbol] == old_s:
                        new_transitions[state][symbol] = new_s
        print(new_transitions)

        self.states = []
        for s in new_states:
            self.states.append(s)
        self.transitions = new_transitions


# pega estado inicial
# transição por a
# pega o e-fecho do estado-alvo

# checa se o estado já existe
    # caso não exista, insere na lista
    # chama a função

if __name__== "__main__":
    states = ['S', 'A', 'B', 'C', 'X']
    alphabet = ['a', 'b']
    final_states = ['S', 'X']
    transitions = {
        'S': {'a': {'A'}, 'b': {'C','X'}},
        'A': {'a': {'B'}, 'b': {'A'}},
        'B': {'a': {'C','X'}, 'b': {'B'}},
        'C': {'a': {'A'}, 'b': {'C','X'}},
        'X': {'a': set(), 'b': set() }
    }
    init_state = 'S'
    a1 = NFA(states, alphabet, init_state, final_states, transitions, False)
    a1.determinize()