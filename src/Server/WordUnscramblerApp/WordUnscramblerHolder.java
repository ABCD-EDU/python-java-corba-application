package WordUnscramblerApp;

/**
* WordUnscramblerApp/WordUnscramblerHolder.java .
* Generated by the IDL-to-Java compiler (portable), version "3.2"
* from ../IDL/WordUnscramblerApp.idl
* Saturday, May 8, 2021 2:46:30 AM CST
*/

public final class WordUnscramblerHolder implements org.omg.CORBA.portable.Streamable
{
  public WordUnscramblerApp.WordUnscrambler value = null;

  public WordUnscramblerHolder ()
  {
  }

  public WordUnscramblerHolder (WordUnscramblerApp.WordUnscrambler initialValue)
  {
    value = initialValue;
  }

  public void _read (org.omg.CORBA.portable.InputStream i)
  {
    value = WordUnscramblerApp.WordUnscramblerHelper.read (i);
  }

  public void _write (org.omg.CORBA.portable.OutputStream o)
  {
    WordUnscramblerApp.WordUnscramblerHelper.write (o, value);
  }

  public org.omg.CORBA.TypeCode _type ()
  {
    return WordUnscramblerApp.WordUnscramblerHelper.type ();
  }

}
