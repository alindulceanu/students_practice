package EnigmaMachine;

public class plugboard{
    keyboard kb = new keyboard();

    String right = kb.ASCII_UPPERCASE;
    String left = kb.ASCII_UPPERCASE;


    public plugboard(String[] pairs){
        for (String i : pairs){
            char A = i.charAt(0);
            char B = i.charAt(1);

            int posA = left.indexOf(A);
            int posB = left.indexOf(B);

            left = left.substring(0, posA) + B + left.substring(posA + 1, left.length());
            left = left.substring(0, posB) + A + left.substring(posB + 1, left.length());

        }
    }

    public int forward(int signal){
        char letter = right.charAt(signal);
        signal = left.indexOf(letter);
        return signal;
    }

    public int backward(int signal){
        char letter = left.charAt(signal);
        signal = right.indexOf(letter);
        return signal;
    }
}
