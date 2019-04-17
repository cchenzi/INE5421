import copy
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
        aux = transitions[self.current_state][symbol]
        self.current_state = self.dead_state if aux == '' else aux
        print('Current state after: ', self.current_state)
    
    def reset_init_state(self):
        self.current_state = self.init_state

    def is_input_valid(self, input):
        self.reset_init_state()
        print('\nStarting to check if', input, 'is valid...')
        for x in input:
            self.make_transition(x)
            if self.current_state == self.dead_state:
                break
        print('End state: ', self.current_state)
        return True if self.current_state in self.final_states else False
