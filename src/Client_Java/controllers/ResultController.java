package controllers;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;
import javafx.stage.Stage;
import model.User;

import java.io.IOException;
import java.net.URL;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.ResourceBundle;

public class ResultController implements Initializable {
    public VBox scoreBox;
    public VBox nameBox;
    public Label nameHeader;
    public Label scoreHeader;
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
        if (User.finished) {
            // set to winning
            resultPane.setStyle("-fx-background-color: #F2F5EA");
            resultLabel.setText("YOU WON!");
        } else {
            // set to losing
            resultPane.setStyle("-fx-background-color: #2C363F");
            resultLabel.setText("GAME OVER!");
            playAgainButton.setStyle("-fx-text-fill: #F2F5EA");
            exitButton.setStyle("-fx-text-fill: #F2F5EA");
            nameHeader.setStyle("-fx-text-fill: #F2F5EA");
            scoreHeader.setStyle("-fx-text-fill: #F2F5EA");
        }
        for (int i = 0; i < 10 ; i++) {
            String req = User.impl.getLeaderboardPosition(i);
            if (!req.equals("")) {
                String[] scoreName = req.split("%%%");

                String name = scoreName[0];
                String score = scoreName[1];

                Label nameLabel = new Label(name);
                nameLabel.setFont(new Font("System Bold", 20.0));

                Label scoreLabel = new Label(score);
                scoreLabel.setFont(new Font("System Bold", 20.0));

                if (!User.finished) {
                    scoreLabel.setStyle("-fx-text-fill: #F2F5EA");
                    nameLabel.setStyle("-fx-text-fill: #F2F5EA");
                }

                scoreBox.getChildren().add(scoreLabel);
                nameBox.getChildren().add(nameLabel);
            }
        }
    }
}
