from string import ascii_uppercase

class reflector:
    def __init__(self, wiring):
        self.right = ascii_uppercase
        self.left = wiring

    def reflect(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal 
