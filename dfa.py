class DFA:
    def __init__(self, states, alphabet, init_state, final_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.final_states = final_states
        self.transitions = transitions
        self.init_state = init_state
        self.current_state = init_state
        self.dead_state = 'qdead'
        
    def make_transition(self, symbol):
        print('Current state before: ', self.current_state, '| Symbol: ', symbol)
        aux = self.transitions[self.current_state][symbol]
        self.current_state = self.dead_state if aux == '' else aux
        print('Current state after: ', self.current_state)
    
    def reset_init_state(self):
        self.current_state = self.init_state

    def is_word_input_valid(self, word_input):
        self.reset_init_state()
        print('\nStarting to check if', word_input, 'is valid...')
        for x in word_input:
            self.make_transition(x)
            if self.current_state == self.dead_state:
                break
        print('End state: ', self.current_state)
        return True if self.current_state in self.final_states else False

    def to_grammar(self):
        grQ = {k: {} for k in self.states}
        for k, x in self.transitions.items():
            aux = []
            for q, t in x.items():
                aux.append(q+t)
                if t in self.final_states: aux.append(q)
            grQ[k] = aux
        return grQ