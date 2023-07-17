import EnigmaMachine.enigmaMachine;
import EnigmaMachine.rotor;
import EnigmaMachine.reflector;
import EnigmaMachine.plugboard;

public class RUN {
    public static void main(String[] args) {
        rotor rot1 = new rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q');
        rotor rot2 = new rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", 'E');
        rotor rot3 = new rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", 'V');
        rotor rot4 = new rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", 'J');
        rotor rot5 = new rotor("VZBRGITYUPSDNHLXAWMJQOFECK", 'Z');

        reflector refA = new reflector("EJMZALYXVBWFCRQUONTSPIKHGD");
        reflector refB = new reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT");
        reflector refC = new reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL");

        String[] pairs = {"BX", "GJ", "TO"};

        plugboard pb = new plugboard(pairs);

        enigmaMachine em = new enigmaMachine(rot1, rot2, rot3, refA, pb);

        String text = "LHFVDEU";

        em.setRings("DAC");
        em.start("CAR");

        String cipher = "";

        for (int i = 0; i < text.length(); i++){
            cipher += em.encode(text.charAt(i));
        }

        System.out.println(cipher);
    }
}
