from Keyboard import keyboard

class enigma:
    def __init__(self, r1, r2, r3, ref, pb):
        self.r1 = r1                            # Initializing the configuration
        self.r2 = r2
        self.r3 = r3
        self.ref = ref
        self.pb = pb
        self.kb = keyboard()

    def start(self, key):                       # Method to set all the rotors into a choosen position
        self.r1.rotateToLetter(key[0])
        self.r2.rotateToLetter(key[1])
        self.r3.rotateToLetter(key[2])

    def setRings(self, ring):                   # Method to set all the notches
        self.r1.setRing(ring[0])
        self.r2.setRing(ring[1])
        self.r3.setRing(ring[2])

    def encrypt(self, letter):

        if self.r2.left[0] == self.r2.notch and self.r3.left[0] == self.r3.notch:       # The if...else if ... else statements make the rotors spin, taking the notches into account
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        
        elif self.r2.left[0] == self.r2.notch:
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()

        elif self.r3.left[0] == self.r3.notch:
            self.r2.rotate()
            self.r3.rotate()

        else:
            self.r3.rotate()

        signal = self.kb.forward(letter)        # The signal goes from the keyboard to the plugboard, then to all the rotors and the reflector, then back in the same path
        signal = self.pb.forward(signal)
        signal = self.r3.forward(signal)
        signal = self.r2.forward(signal)
        signal = self.r1.forward(signal)
        signal = self.ref.reflect(signal)
        signal = self.r1.backward(signal)
        signal = self.r2.backward(signal)
        signal = self.r3.backward(signal)
        signal = self.pb.backward(signal)
        letter = self.kb.backward(signal)

        return letter