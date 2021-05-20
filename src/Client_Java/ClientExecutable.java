import WordUnscramblerApp.*;
import model.User;
import org.omg.CosNaming.*;
import org.omg.CosNaming.NamingContextPackage.*;
import org.omg.CORBA.*;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
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

            org.omg.CORBA.Object objRef = orb.resolve_initial_references("NameService");

            NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);

            String name = "WordGame";
            impl = WordUnscramblerHelper.narrow(ncRef.resolve_str(name));

            User.impl = impl;

            currUser = null;
            launch(args);
        } catch (Exception e) {
            e.printStackTrace();
        }
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
