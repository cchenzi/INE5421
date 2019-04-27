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

    #terminar
    def determinize_epsilon(self):
        aux = self.epsilon_closure[self.init_state]
        new_states = {}
        new_states[aux] = self.get_epsilon_transitions(aux)
