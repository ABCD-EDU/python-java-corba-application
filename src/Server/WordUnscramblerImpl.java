import java.util.Random;

import WordUnscramblerApp.WordUnscramblerPOA;

public class WordUnscramblerImpl extends WordUnscramblerPOA{
    
    public boolean logIn(String username) {
        Server.userWordSet.put(username, "");
        return true;
    }
    
    public String requestWord(String username) {
        Random rand = new Random();

        String word = Server.wordSet.get(rand.nextInt(Server.wordSet.size() - 1));
        Server.userWordSet.put(username, word);
        return word;
    }

    public boolean checkAnswer(String username, String answer) {
        String currWord = Server.userWordSet.get(username);
        
        return currWord.equalsIgnoreCase(answer);
    }
    
    public String requestRescramble(String username) {
        String word = Server.userWordSet.get(username);        

        return scrambleWord(word);
    }

    private String scrambleWord(String word) {
        Random random = new Random();
        char a[] = word.toCharArray();

        for( int i=0 ; i<a.length ; i++ ) { 
            int j = random.nextInt(a.length);
            char temp = a[i]; a[i] = a[j];  a[j] = temp;
        }

        return new String(a);
    }
}
