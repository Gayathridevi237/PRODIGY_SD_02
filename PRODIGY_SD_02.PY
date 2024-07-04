import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class GuessingGame(QWidget):
    def __init__(self):
        super().__init__()

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Guessing Game")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        label = QLabel("Guess a number between 1 and 100:")
        layout.addWidget(label)

        self.entry = QLineEdit()
        layout.addWidget(self.entry)

        button = QPushButton("Guess")
        button.clicked.connect(self.check_guess)
        layout.addWidget(button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def check_guess(self):
        user_guess = int(self.entry.text())
        self.attempts += 1

        if user_guess < self.secret_number:
            self.result_label.setText("Too low! Try again.")
        elif user_guess > self.secret_number:
            self.result_label.setText("Too high! Try again.")
        else:
            self.result_label.setText(f"Congratulations! You guessed the number in {self.attempts} attempts.")
            button = self.findChild(QPushButton)
            button.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = GuessingGame()
    game.show()
    sys.exit(app.exec_())