package WordUnscramblerApp;


/**
* WordUnscramblerApp/WordUnscramblerPOA.java .
* Generated by the IDL-to-Java compiler (portable), version "3.2"
* from C:/Users/Lance/Desktop/9322-fingrp2/src/IDL/WordUnscramblerApp.idl
* Tuesday, May 18, 2021 7:02:07 PM CST
*/

public abstract class WordUnscramblerPOA extends org.omg.PortableServer.Servant
 implements WordUnscramblerApp.WordUnscramblerOperations, org.omg.CORBA.portable.InvokeHandler
{

  // Constructors

  private static java.util.Hashtable _methods = new java.util.Hashtable ();
  static
  {
    _methods.put ("logIn", new java.lang.Integer (0));
    _methods.put ("requestWord", new java.lang.Integer (1));
    _methods.put ("checkAnswer", new java.lang.Integer (2));
    _methods.put ("requestRescramble", new java.lang.Integer (3));
    _methods.put ("requestScore", new java.lang.Integer (4));
    _methods.put ("getLeaderboardPosition", new java.lang.Integer (5));
  }

  public org.omg.CORBA.portable.OutputStream _invoke (String $method,
                                org.omg.CORBA.portable.InputStream in,
                                org.omg.CORBA.portable.ResponseHandler $rh)
  {
    org.omg.CORBA.portable.OutputStream out = null;
    java.lang.Integer __method = (java.lang.Integer)_methods.get ($method);
    if (__method == null)
      throw new org.omg.CORBA.BAD_OPERATION (0, org.omg.CORBA.CompletionStatus.COMPLETED_MAYBE);

    switch (__method.intValue ())
    {
       case 0:  // WordUnscramblerApp/WordUnscrambler/logIn
       {
         String username = in.read_string ();
         boolean $result = false;
         $result = this.logIn (username);
         out = $rh.createReply();
         out.write_boolean ($result);
         break;
       }

       case 1:  // WordUnscramblerApp/WordUnscrambler/requestWord
       {
         String username = in.read_string ();
         String $result = null;
         $result = this.requestWord (username);
         out = $rh.createReply();
         out.write_string ($result);
         break;
       }

       case 2:  // WordUnscramblerApp/WordUnscrambler/checkAnswer
       {
         String username = in.read_string ();
         String answer = in.read_string ();
         boolean $result = false;
         $result = this.checkAnswer (username, answer);
         out = $rh.createReply();
         out.write_boolean ($result);
         break;
       }

       case 3:  // WordUnscramblerApp/WordUnscrambler/requestRescramble
       {
         String username = in.read_string ();
         String $result = null;
         $result = this.requestRescramble (username);
         out = $rh.createReply();
         out.write_string ($result);
         break;
       }

       case 4:  // WordUnscramblerApp/WordUnscrambler/requestScore
       {
         String username = in.read_string ();
         int $result = (int)0;
         $result = this.requestScore (username);
         out = $rh.createReply();
         out.write_long ($result);
         break;
       }

       case 5:  // WordUnscramblerApp/WordUnscrambler/getLeaderboardPosition
       {
         int index = in.read_long ();
         String $result = null;
         $result = this.getLeaderboardPosition (index);
         out = $rh.createReply();
         out.write_string ($result);
         break;
       }

       default:
         throw new org.omg.CORBA.BAD_OPERATION (0, org.omg.CORBA.CompletionStatus.COMPLETED_MAYBE);
    }

    return out;
  } // _invoke

  // Type-specific CORBA::Object operations
  private static String[] __ids = {
    "IDL:WordUnscramblerApp/WordUnscrambler:1.0"};

  public String[] _all_interfaces (org.omg.PortableServer.POA poa, byte[] objectId)
  {
    return (String[])__ids.clone ();
  }

  public WordUnscrambler _this() 
  {
    return WordUnscramblerHelper.narrow(
    super._this_object());
  }

  public WordUnscrambler _this(org.omg.CORBA.ORB orb) 
  {
    return WordUnscramblerHelper.narrow(
    super._this_object(orb));
  }


} // class WordUnscramblerPOA
