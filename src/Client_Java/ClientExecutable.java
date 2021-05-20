import WordUnscramblerApp.*;
import model.User;
import org.omg.CosNaming.*;
import org.omg.CosNaming.NamingContextPackage.*;
import org.omg.CORBA.*;
import java.util.Scanner;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class ClientExecutable extends Application {
    public static WordUnscrambler impl;
    public static model.User currUser;

    @Override
    public void start(Stage primaryStage) throws Exception {
        Parent root = FXMLLoader.load(getClass().getClassLoader().getResource("resources/view/Menu.fxml"));
        Scene scene = new Scene(root);
        primaryStage.setTitle("Textra");
        primaryStage.setScene(scene);
        primaryStage.show();
        primaryStage.setResizable(false);
    }

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
            impl = WordUnscramblerHelper.narrow(ncRef.resolve_str(name));

            System.out.println("Client successfuly connected");
            User.impl = impl;

            Scanner in = new Scanner(System.in);
            in.nextLine();

            currUser = null;
            launch(args);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
