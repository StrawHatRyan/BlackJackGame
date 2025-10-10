import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QLineEdit, QMessageBox
)
from PyQt5.QtCore import Qt
from game import Player
from dice import player_hit, dealer_hit


class BlackjackApp(QWidget):
    def __init__(self):
        super().__init__()

   
        self.setWindowTitle("Diced Blackjack")
        self.setGeometry(200, 200, 400, 300)


        self.title_label = QLabel("Welcome to Diced Blackjack!")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold;")

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name")

        self.start_button = QPushButton("Start Game")
        self.start_button.clicked.connect(self.start_game)

  
        self.exit_button = QPushButton("Exit Game")
        self.exit_button.clicked.connect(self.close_app)

        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.start_button)
        layout.addWidget(self.exit_button) 
        layout.addStretch()

        self.setLayout(layout)

    def start_game(self):
        name = self.name_input.text().strip()
        if not name:
            QMessageBox.warning(self, "Missing Name", "Please enter your name!")
            return

        self.player = Player(name)
        QMessageBox.information(self, "Game Start", f"Hello {self.player.name}, let's play Blackjack!")


    def close_app(self):
        user_choice = QMessageBox.question(
            self,
            "Exit Game",
            "Are you sure you want to exit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if user_choice == QMessageBox.Yes:
            QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BlackjackApp()
    window.show()
    sys.exit(app.exec_())

