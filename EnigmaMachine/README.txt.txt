Enigma Machine ecryption project made in Java

How to use:

Execute the RUN.java file and the console output should be the encrpyted version of the text variable.

There are 5 rotor configurations and 3 reflectors, all used in WW2 by the German Army.

You can further customize the settings of the enigma machine by changing the rotors and reflectors in the "em" object (The order of which the rotors are declared matters!)

You can change the pairs of letters connected in the plugboard by changing the "pairs" string array (You can add as may pairs as you wish)

The plugboard swapps the letters connected everytime they go through it (Once at the beggining of the encrpytion and once again at the end of the encrpytion as seen in the enigmaMachine class in the encode method)
If you connect B to Z ("BZ") every B will be swapped with Z and every Z to B

em.start() changes the letters at which the rotors start (default is "AAA")
em.setRings() changes the wirings of the rotors relative to the position of the rotor ex:

ABCDEFGHIJKLMNOPQRSTUVWXYZ
VZBRGITYUPSDNHLXAWMJQOFECK

Changing the ring setting of this rotor to B will change the wiring in this manner:

ABCDEFGHIJKLMNOPQRSTUVWXYZ
ZBRGITYUPSDNHLXAWMJQOFECKV

Only use UPPERCASE letters in the text string!!