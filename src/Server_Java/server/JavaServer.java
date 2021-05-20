package server;

import org.omg.CosNaming.*;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

import org.omg.CORBA.*;
import org.omg.PortableServer.*;
import org.omg.PortableServer.POA;
import WordUnscramblerApp.*;

public class JavaServer {
    // username, currentword
    public static Map<String, String> userWordSet;
    // container for users available words
    public static Map<String, Map<Integer, Stack<String>>> userWordStack;
    // contains all of the available words
    private static List<String> wordSet;
    // user leaderboards
    public static Map<String, Integer> leaderboards;

    public static void main(String[] args) {
        try {
            String[] params = readConfig();
            if (args == null && params == null) {
                System.out.println("args or .config parameters needed");
                System.exit(0);
            }
            ORB orb;
            if (args != null && params == null) {
                orb = ORB.init(args, null);
            } else {
                orb = ORB.init(params, null);
            }

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
            String name = "WordGame";
            NameComponent path[] = ncRef.to_name(name);
            ncRef.rebind(path, href);
            System.out.println("Server ready and waiting ...");

            wordSet = new ArrayList<>();
            userWordSet = new HashMap<>();
            leaderboards = new HashMap<>();
            userWordStack = new HashMap<>();

            Scanner in = new Scanner(System.in);
            System.out.print("Enter the path for the word list file: ");
            String filePath = in.nextLine();

            readFile(filePath);

            // wait for invocations from clients
            orb.run();
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println("Server exiting...");
    }

    /**
     * Takes a path and reads every line that contains one word only.
     * All approved lines will then be inserted into the {@code wordSet} collection.
     * @param path word file path
     */
    private static void readFile(String path) {
        try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
            String line = "";
            while (true) {
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

    public static Map<Integer, Stack<String>> sortWordSet() {
        Map<Integer, Stack<String>> set = new HashMap<>();

        Collections.shuffle(wordSet);
        for (String word : wordSet) {
            set.computeIfAbsent(word.length(), k -> new Stack<>()).add(word);
        }

        return set;
    }

    private static String[] readConfig() {
        String param = "";
        List<String> args = new ArrayList<>();
        String[] argConfig = null;
        try (BufferedReader reader = new BufferedReader(new FileReader("../../../.config"))) {
            reader.lines().map(String::valueOf).forEach(args::add);
            for (String line : args) {
                String[] getParam = line.split("=");
                if (line.contains("host")) {
                    param += "  -ORBInitialHost " + getParam[1];
                } else if (line.contains("port")) {
                    param += " -ORBInitialPort " + getParam[1];
                }
            }

            argConfig = param.split("\\s");
        } catch (IOException e) {
            e.printStackTrace();
        }
        return argConfig;
    }
}