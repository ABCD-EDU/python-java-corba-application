package WordUnscramblerApp;


/**
* WordUnscramblerApp/WordUnscramblerOperations.java .
* Generated by the IDL-to-Java compiler (portable), version "3.2"
* from ../IDL/WordUnscramblerApp.idl
* Sunday, May 9, 2021 7:28:39 PM CST
*/

public interface WordUnscramblerOperations 
{
  boolean logIn (String username);
  String requestWord (String username);
  boolean checkAnswer (String username, String answer);
  String requestRescramble (String username);
} // interface WordUnscramblerOperations