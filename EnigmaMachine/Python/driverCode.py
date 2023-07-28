from Reflector import reflector
from Rotor import rotor
from Keyboard import keyboard
from Plugboard import plugboard
from EnigmaMachine import enigma

rot1 = rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")             # Configurations of rotors used by the german army in WW2
rot2 = rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
rot3 = rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
rot4 = rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
rot5 = rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

refA = reflector("EJMZALYXVBWFCRQUONTSPIKHGD")              # Configurations of reflectors used by the german army in WW2
refB = reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
refC = reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

text = "NYXQIGN"                                            # The text that will be encrypted, you can also decrypt the same way you encrypted

kb = keyboard()
pb = plugboard(["AP", "BG", "XZ"])                          # Plugboard configuration, you can choose any pairs you want

em = enigma(rot1,rot2,rot3,refB, pb)                        # Enigma machine configuration, you can choose any 3 rotors and a reflector and it will dramatically change the way text is encrypted

em.setRings("DAC")                                          # Rings and starting configurations, again, changing any of them will make the machine encrpy in a different manner
em.start("CAR")

cipher = ""                                                 # Variable to store the encrypted text

for letter in text:
    cipher +=  em.encrypt(letter)

print(cipher)