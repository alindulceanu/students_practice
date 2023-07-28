from string import ascii_uppercase

class rotor:                                                        # A rotor works like a plugboard, but every letter is swapped with another one and everytime you type a letter, it spins, changing the configuration
    def __init__(self, wiring, notch):
        self.left = ascii_uppercase
        self.right = wiring 
        self.notch = notch

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal 

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal 

    def rotate(self, n = 1, forward = True):                        # It can rotate both backwards and forward so we need to take that into account
        for i in range(n):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]

            else:
                self.left = self.left[25] + self.left[:25]
                self.right = self.right[25] + self.right[:25]

    def rotateToLetter(self, letter):                               # Method to rotate so that the 'letter' atribute comes first in the string
        n = ascii_uppercase.find(letter)
        self.rotate(n)

    def show(self):                                                 # Debugging tool
        print(self.left)
        print(self.right)
        print(" ")

    def setRing(self, letter):                                      # The notch is the letter at which two rotors connect, spinning both of them at the same time
        n = ascii_uppercase.find(letter)
        self.rotate(n, forward = False)

        notch = ascii_uppercase.find(self.notch)
        self.notch = ascii_uppercase[(notch - n) % 26]