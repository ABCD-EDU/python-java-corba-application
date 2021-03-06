package controllers;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.stage.Stage;
import javafx.scene.control.Label;
import model.User;

import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;

public class MenuController implements Initializable {

    @FXML
    private Label warning_label;

    @FXML
    private TextField loginField;
    
    @FXML
    private Button loginButton;

    @FXML
    public void onEnterPress(KeyEvent event) {
        if (event.getCode() == KeyCode.ENTER) loginPressed();
    }

    @FXML
    private void loginPressed() {
        if (loginField.getText().isEmpty()) {
            warning_label.setText("Please fill in name field");
            warning_label.setVisible(true);
            return;
        }
        String username = loginField.getText();
        model.User.username = username;
        User.impl.logIn(username);
        try {
            Stage window = (Stage) loginButton.getScene().getWindow();
            window.setScene(new Scene(FXMLLoader.load(getClass()
                    .getResource("../resources/view/Game.fxml"))));
            window.show();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
    }
}
