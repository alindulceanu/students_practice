package EnigmaMachine;

public class keyboard {
    String ASCII_UPPERCASE = "";

    public keyboard(){
        char c;
        for (c = 'A'; c <= 'Z'; c++) 
        {
            ASCII_UPPERCASE += c;
        }
    }

    public int forward(char letter){
        int signal = ASCII_UPPERCASE.indexOf(letter);
        return signal;

    }

    public char backward(int signal){
        char letter = ASCII_UPPERCASE.charAt(signal);
        return letter;

    }
}

