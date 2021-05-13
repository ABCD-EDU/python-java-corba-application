package server;

import java.util.Random;

import WordUnscramblerApp.*;

public class WordUnscramblerImpl extends WordUnscramblerPOA{
    
    public boolean logIn(String username) {
        JavaServer.userWordSet.put(username, "");
        JavaServer.leaderboards.put(username, 0);
        return true;
    }
    
    public String requestWord(String username) {
        Random rand = new Random();

        String word = JavaServer.wordSet.get(rand.nextInt(JavaServer.wordSet.size() - 1));
        JavaServer.userWordSet.put(username, word);
        return word;
    }

    public boolean checkAnswer(String username, String answer) {
        String currWord = JavaServer.userWordSet.get(username);
        
        if (currWord.equalsIgnoreCase(answer)) {
            JavaServer.leaderboards.put(username, JavaServer.leaderboards.get(username)+1);
            return true;
        }

        return false;
    }
    
    public String requestRescramble(String username) {
        String word = JavaServer.userWordSet.get(username);

        return scrambleWord(word);
    }

    @Override
    public int requestScore(String username) {
        return JavaServer.leaderboards.get(username);
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
