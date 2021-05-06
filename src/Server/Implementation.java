import WordUnscramblerApp.WordUnscramblerPOA;

public class Implementation extends WordUnscramblerPOA{
    
    public boolean logIn(String username) {
         return username.equals("true");
    }
    
    public String requestWord() {
        return "word";
    }

    public boolean checkAnswer(String answer) {
        return answer.equals("true");
    }
    
    public String requestRescramble() {
        return "rescramble";
    }

}
