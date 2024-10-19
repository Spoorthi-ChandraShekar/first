class State:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Transition:
    def __init__(self, from_state, input_symbol, to_state):
        self.from_state = from_state
        self.input_symbol = input_symbol
        self.to_state = to_state


class StateMachine:
    def __init__(self):
        self.states = {}
        self.transitions = []
        self.current_state = None

    def add_state(self, state_name):
        state = State(state_name)
        self.states[state_name] = state

    def add_transition(self, from_state_name, input_symbol, to_state_name):
        from_state = self.states[from_state_name]
        to_state = self.states[to_state_name]
        transition = Transition(from_state, input_symbol, to_state)
        self.transitions.append(transition)

    def set_initial_state(self, state_name):
        self.current_state = self.states[state_name]

    def simulate(self, input_sequence):
        sequence = [self.current_state]
        for input_symbol in input_sequence:
            next_state = self.get_next_state(self.current_state, input_symbol)
            if next_state:
                sequence.append(next_state)
                self.current_state = next_state
        return sequence

    def get_next_state(self, current_state, input_symbol):
        for transition in self.transitions:
            if transition.from_state == current_state and transition.input_symbol == input_symbol:
                return transition.to_state
        return None


# Sample usage
if __name__ == "__main__":
    sm = StateMachine()
    
    # Define states
    sm.add_state('A')
    sm.add_state('B')
    sm.add_state('C')
    
    # Define transitions
    sm.add_transition('A', '0', 'A')
    sm.add_transition('A', '1', 'B')
    sm.add_transition('B', '0', 'C')
    sm.add_transition('B', '1', 'A')
    sm.add_transition('C', '0', 'B')
    sm.add_transition('C', '1', 'C')
    
    # Set initial state
    sm.set_initial_state('A')
    
    # Simulate state machine with input sequence
    input_sequence = ['1', '0', '1', '1', '0']
    state_sequence = sm.simulate(input_sequence)
    
    print("State sequence:", state_sequence)
