from Reflector import reflector
from Rotor import rotor
from Keyboard import keyboard
from Plugboard import plugboard
from EnigmaMachine import enigma

rot1 = rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
rot2 = rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
rot3 = rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
rot4 = rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
rot5 = rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

refA = reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
refB = reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
refC = reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")


text = "NYXQIGN"

kb = keyboard()
pb = plugboard(["AP", "BG", "XZ"])

em = enigma(rot1,rot2,rot3,refB, pb)

em.setRings("DAC")
em.start("CAR")

cipher = ""

for letter in text:
    cipher +=  em.encrypt(letter)

print(cipher)