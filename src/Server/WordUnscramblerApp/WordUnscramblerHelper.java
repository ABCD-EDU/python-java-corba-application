package WordUnscramblerApp;


/**
* WordUnscramblerApp/WordUnscramblerHelper.java .
* Generated by the IDL-to-Java compiler (portable), version "3.2"
* from ../IDL/WordUnscramblerApp.idl
* Saturday, May 8, 2021 2:46:30 AM CST
*/

abstract public class WordUnscramblerHelper
{
  private static String  _id = "IDL:WordUnscramblerApp/WordUnscrambler:1.0";

  public static void insert (org.omg.CORBA.Any a, WordUnscramblerApp.WordUnscrambler that)
  {
    org.omg.CORBA.portable.OutputStream out = a.create_output_stream ();
    a.type (type ());
    write (out, that);
    a.read_value (out.create_input_stream (), type ());
  }

  public static WordUnscramblerApp.WordUnscrambler extract (org.omg.CORBA.Any a)
  {
    return read (a.create_input_stream ());
  }

  private static org.omg.CORBA.TypeCode __typeCode = null;
  synchronized public static org.omg.CORBA.TypeCode type ()
  {
    if (__typeCode == null)
    {
      __typeCode = org.omg.CORBA.ORB.init ().create_interface_tc (WordUnscramblerApp.WordUnscramblerHelper.id (), "WordUnscrambler");
    }
    return __typeCode;
  }

  public static String id ()
  {
    return _id;
  }

  public static WordUnscramblerApp.WordUnscrambler read (org.omg.CORBA.portable.InputStream istream)
  {
    return narrow (istream.read_Object (_WordUnscramblerStub.class));
  }

  public static void write (org.omg.CORBA.portable.OutputStream ostream, WordUnscramblerApp.WordUnscrambler value)
  {
    ostream.write_Object ((org.omg.CORBA.Object) value);
  }

  public static WordUnscramblerApp.WordUnscrambler narrow (org.omg.CORBA.Object obj)
  {
    if (obj == null)
      return null;
    else if (obj instanceof WordUnscramblerApp.WordUnscrambler)
      return (WordUnscramblerApp.WordUnscrambler)obj;
    else if (!obj._is_a (id ()))
      throw new org.omg.CORBA.BAD_PARAM ();
    else
    {
      org.omg.CORBA.portable.Delegate delegate = ((org.omg.CORBA.portable.ObjectImpl)obj)._get_delegate ();
      WordUnscramblerApp._WordUnscramblerStub stub = new WordUnscramblerApp._WordUnscramblerStub ();
      stub._set_delegate(delegate);
      return stub;
    }
  }

  public static WordUnscramblerApp.WordUnscrambler unchecked_narrow (org.omg.CORBA.Object obj)
  {
    if (obj == null)
      return null;
    else if (obj instanceof WordUnscramblerApp.WordUnscrambler)
      return (WordUnscramblerApp.WordUnscrambler)obj;
    else
    {
      org.omg.CORBA.portable.Delegate delegate = ((org.omg.CORBA.portable.ObjectImpl)obj)._get_delegate ();
      WordUnscramblerApp._WordUnscramblerStub stub = new WordUnscramblerApp._WordUnscramblerStub ();
      stub._set_delegate(delegate);
      return stub;
    }
  }

}
