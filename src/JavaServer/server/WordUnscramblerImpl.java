package server;

import java.util.Random;

import WordUnscramblerApp.*;

public class WordUnscramblerImpl extends WordUnscramblerPOA{
    
    public boolean logIn(String username) {
        JavaServer.userWordSet.put(username, "");
        JavaServer.leaderboards.put(username, 0);
        JavaServer.userWordStack.put(username, JavaServer.sortWordSet());
        return true;
    }
    
    public String requestWord(String username) {
        for (int i = 1; i <= JavaServer.userWordStack.get(username).size(); i++) {
            try {
                String word = JavaServer.userWordStack.get(username).get(i).pop();
                if (word != null) {
                    JavaServer.userWordSet.put(username, word);
                    return word;
                }
            } catch (NullPointerException ignored) {
            }
        }
        return "";
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

        String scrambled = scrambleWord(word);
        while (word.equalsIgnoreCase(scrambled)) {
            scrambled = scrambleWord(word);
        }
        return scrambled;
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