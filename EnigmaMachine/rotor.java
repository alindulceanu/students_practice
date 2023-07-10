package EnigmaMachine;

public class rotor {
    keyboard kb = new keyboard();
    String left = kb.ASCII_UPPERCASE;
    String right;
    char sNotch;

    public rotor(String wiring, char notch){
        right = wiring;
        sNotch = notch;
    }

    public int forward(int signal){
        char letter = right.charAt(signal);
        signal = left.indexOf(letter);
        return signal;
    }

    public int backward(int signal){
        char letter = left.charAt(signal);
        signal  = right.indexOf(letter);
        return signal;
    }

    public void rotate(int n,  boolean forward){
        for (int i = 0; i < n; i++){
            if (forward){
                left = left.substring(1, left.length()) + left.charAt(0);
                right = right.substring(1, right.length()) + right.charAt(0);
            }

            else{
                left = left.charAt(25) + left.substring(0, 25);
                right = right.charAt(25) + right.substring(0, 25);
            }
        }
    }

    public void rotateToLetter(char letter){
        int signal = kb.ASCII_UPPERCASE.indexOf(letter);
        rotate(signal, true);
    }

    public void setRing(char letter){
        int signal = kb.ASCII_UPPERCASE.indexOf(letter);
        rotate(signal, false);

        int notch = kb.ASCII_UPPERCASE.indexOf(sNotch);
        sNotch = kb.ASCII_UPPERCASE.charAt((notch - signal) % 26);
    }
}
