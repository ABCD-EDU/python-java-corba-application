import WordUnscramblerApp.*;
import org.omg.CosNaming.*;
import org.omg.CosNaming.NamingContextPackage.*;
import org.omg.CORBA.*;
import java.util.Scanner;

public class Client {
    static WordUnscrambler implementation;

    public static void main(String[] args) {
        try {
            // create and initialize the ORB
            ORB orb = ORB.init(args, null);
            
            // get the root naming context
            org.omg.CORBA.Object objRef = orb.resolve_initial_references("NameService");
            
            // Use NamingContextExt instead of NamingContext. This is part
            // of the Interoperable naming Service.
            NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);
            
            // resolve the Object Reference in Naming
            String name = "Hello";
            implementation = WordUnscramblerHelper.narrow(ncRef.resolve_str(name));

            System.out.println("Client successfuly connected");
            System.out.println(implementation.logIn("true"));
            System.out.println(implementation.checkAnswer("true"));
            System.out.println(implementation.requestRescramble());
            System.out.println(implementation.requestWord());

            Scanner in = new Scanner(System.in);
            in.nextLine();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
