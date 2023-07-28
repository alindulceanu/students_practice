from string import ascii_uppercase

class reflector:                            # A reflector is added at the end of the rotors and it's role is to turn the signals back in the rotors, they don't spin
    def __init__(self, wiring):
        self.right = ascii_uppercase
        self.left = wiring

    def reflect(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal 
