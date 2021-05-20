package model;

import WordUnscramblerApp.WordUnscrambler;

public class User {
    public static WordUnscrambler impl;
    public static String username;
    public static int score;
    public static boolean finished;

    public User(WordUnscrambler i) {
        impl = i;
        username = "";
        score = 0;
        finished = false;
    }
}