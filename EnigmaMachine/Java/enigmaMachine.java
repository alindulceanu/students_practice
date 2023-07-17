package EnigmaMachine;

public class enigmaMachine {
    rotor R1, R2, R3;
    reflector REF;
    plugboard PB;
    keyboard KB = new keyboard();

    public enigmaMachine(rotor r1, rotor r2, rotor r3, reflector ref, plugboard pb){
        R1 = r1;
        R2 = r2;
        R3 = r3;
        REF = ref;
        PB = pb;
    }

    public void start(String key){
        R1.rotateToLetter(key.charAt(0));
        R2.rotateToLetter(key.charAt(1));
        R3.rotateToLetter(key.charAt(2));
    }

    public void setRings(String ring){
        R1.setRing(ring.charAt(0));
        R2.setRing(ring.charAt(1));
        R3.setRing(ring.charAt(2));
    }

    public char encode(char letter){
        if (R2.left.charAt(0) == R2.sNotch && R3.left.charAt(0) == R3.sNotch){
            R1.rotate(1, true);
            R2.rotate(1, true);
            R3.rotate(1, true);
        }

        else if (R2.left.charAt(0) == R2.sNotch){
            R1.rotate(1, true);
            R2.rotate(1, true);
            R3.rotate(1, true);
        }

        else if (R3.left.charAt(0) == R3.sNotch){
            R2.rotate(1, true);
            R3.rotate(1, true);
        }

        else{
            R3.rotate(1, true);
        }

        int signal = KB.forward(letter);
        signal = PB.forward(signal);
        signal = R3.forward(signal);
        signal = R2.forward(signal);
        signal = R1.forward(signal);
        signal = REF.reflect(signal);
        signal = R1.backward(signal);
        signal = R2.backward(signal);
        signal = R3.backward(signal);
        signal = PB.backward(signal);
        letter = KB.backward(signal);

        return letter;
    }
}
