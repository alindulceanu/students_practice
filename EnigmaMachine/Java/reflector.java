package EnigmaMachine;

public class reflector {
    keyboard kb = new keyboard();
    String right = kb.ASCII_UPPERCASE;
    String left;
    
    public reflector(String wiring){
        left = wiring;
    }

    public int reflect(int signal){
        char letter = right.charAt(signal);
        signal = left.indexOf(letter);
        return signal;
    }
}
