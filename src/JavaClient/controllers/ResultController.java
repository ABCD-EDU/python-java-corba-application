package controllers;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

public class ResultController implements Initializable {
    @FXML
    private Label resultLabel;

    @FXML
    private AnchorPane resultPane;

    @FXML
    private Label playAgainButton;

    @FXML
    private Label exitButton;

    private String winColor = "0xF2F5EA";
    private String loseColor = "0x2C363F";

    @FXML
    public void playAgain() {
        try {
            Stage window = (Stage) exitButton.getScene().getWindow();
            window.setScene(new Scene(FXMLLoader.load(getClass()
                    .getResource("../resources/view/Menu.fxml"))));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @FXML
    public void exitGame() {
        System.exit(1);
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

    }
}
