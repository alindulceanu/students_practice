from string import ascii_uppercase

class plugboard:
    def __init__(self, pairs):                              # The plugboard is used to swap letters when encrypting a letter
        self.left = ascii_uppercase                         # Left is a string with the swapped letters
        self.right =  ascii_uppercase                       # While right is a refference to the alphabet

        for i in pairs:
            A = i[0]
            B = i[1]
            pos_A = self.left.find(A)
            pos_B = self.left.find(B)
            self.left = self.left[:pos_A] + B + self.left[pos_A+1:]
            self.left = self.left[:pos_B] + A + self.left[pos_B+1:]

    def forward(self, signal):                              # This method converts a position from the right the to the left strings
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal 

    def backward(self, signal):                             # This method does the exact opposite of the previous one
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal 