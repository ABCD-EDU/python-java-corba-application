import org.omg.CosNaming.*;
import org.omg.CosNaming.NamingContextPackage.*;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.Map;
import java.util.List;
import org.omg.CORBA.*;
import org.omg.PortableServer.*;
import org.omg.PortableServer.POA;
import WordUnscramblerApp.*;

public class Server {
    // username, currentword
    public static Map<String, String> userWordSet;
    // contains all of the available words
    public static List<String> wordSet;


    public static void main(String[] args) {
        try {
            ORB orb = ORB.init(args, null);
            
            // get reference to rootpoa & activate the POAManager
            POA rootpoa = POAHelper.narrow(orb.resolve_initial_references("RootPOA"));
            rootpoa.the_POAManager().activate();
            
            // create servant and register it with the ORB
            WordUnscramblerImpl implementation = new WordUnscramblerImpl();
            
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
        System.out.print("Enter the path for the word list file: ");
        String path = in.nextLine();

        readFile(path);
        System.out.println("Server exiting...");
    }

    /**
     * Takes a path and reads every line that contains one word only.
     * All approved lines will then be inserted into the {@code wordSet} collection.
     * @param path word file path
     */
    private static void readFile(String path) {
        try (BufferedReader reader = new BufferedReader(new FileReader(new File(path)))) {
            String line = "";
            while (line != null) {
                line = reader.readLine();
                if (line == null) {
                    break;
                }

                if (line.split(" ").length == 1) {
                    wordSet.add(line);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}