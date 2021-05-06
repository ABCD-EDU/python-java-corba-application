import org.omg.CosNaming.*;
import org.omg.CosNaming.NamingContextPackage.*;
import java.util.Scanner;
import org.omg.CORBA.*;
import org.omg.PortableServer.*;
import org.omg.PortableServer.POA;
import WordUnscramblerApp.*;

public class Server {
    public static void main(String[] args) {
        try {
            ORB orb = ORB.init(args, null);
            
            // get reference to rootpoa & activate the POAManager
            POA rootpoa = POAHelper.narrow(orb.resolve_initial_references("RootPOA"));
            rootpoa.the_POAManager().activate();
            
            // create servant and register it with the ORB
            Implementation implementation = new Implementation();
            
            // get object reference from the servant
            org.omg.CORBA.Object ref = rootpoa.servant_to_reference(implementation);
            WordUnscrambler href = WordUnscramblerHelper.narrow(ref);
            
            // get the root naming context
            org.omg.CORBA.Object objRef = orb.resolve_initial_references("NameService");
            
            // Use NamingContextExt which is part of the Interoperable
            // Naming Service (INS) specification.
            NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);
            
            // bind the Object Reference in Naming
            String name = "Hello";
            NameComponent path[] = ncRef.to_name(name);
            ncRef.rebind(path, href);
            System.out.println("Server ready and waiting ...");
            
            // wait for invocations from clients
            orb.run();
        } catch (Exception e) {
            e.printStackTrace();
        }
        Scanner in = new Scanner(System.in);
        in.nextLine();
        System.out.println("Server exiting...");
    }

}