from string import ascii_uppercase

class keyboard:                                      # This class has two properties
    def forward(self, letter):                       # To turn a letter into it's position in the 'ascii_uppercase'
        signal = ascii_uppercase.find(letter)
        return signal

    def backward(self, signal):                      # And turning a position from the 'ascii_uppercase' into a letter
        letter = ascii_uppercase[signal]
        return letter