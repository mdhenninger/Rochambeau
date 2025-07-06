import sys
import random
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtCore import Qt

MOVES = ['rock', 'paper', 'scissors']

class RochambeauGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rochambeau (Rock-Paper-Scissors)")
        self.setGeometry(100, 100, 600, 400)
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.init_ui()

    def init_ui(self):
        # Modern Scoreboard
        self.score_label = QLabel(self.score_text())
        self.score_label.setFont(QFont('Arial', 18, QFont.Bold))
        self.score_label.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #222, stop:1 #444);
            color: #fff;
            border-radius: 12px;
            padding: 12px;
            margin: 8px;
            letter-spacing: 2px;
        """)

        self.result_label = QLabel("")
        self.result_label.setFont(QFont('Arial', 16, QFont.Bold))
        self.result_label.setStyleSheet("color: #2196F3; margin: 8px;")

        self.player_image = QLabel()
        self.computer_image = QLabel()
        self.player_image.setFixedSize(140, 140)
        self.computer_image.setFixedSize(140, 140)
        self.player_image.setStyleSheet("background: #f0f0f0; border-radius: 16px; border: 2px solid #bbb;")
        self.computer_image.setStyleSheet("background: #f0f0f0; border-radius: 16px; border: 2px solid #bbb;")

        self.player_text = QLabel("")
        self.computer_text = QLabel("")
        self.player_text.setFont(QFont('Arial', 12, QFont.Bold))
        self.computer_text.setFont(QFont('Arial', 12, QFont.Bold))
        self.player_text.setStyleSheet("color: #388e3c;")
        self.computer_text.setStyleSheet("color: #d32f2f;")

        self.choices_label = QLabel("Choose your move:")
        self.choices_label.setFont(QFont('Arial', 14, QFont.Bold))
        self.choices_label.setStyleSheet("margin: 8px;")

        # Modern Buttons with icons
        btn_rock = QPushButton(" Rock")
        btn_rock.setIcon(QIcon("images/rock.png"))
        btn_rock.setIconSize(self.player_image.size())
        btn_rock.setFont(QFont('Arial', 12, QFont.Bold))
        btn_rock.setStyleSheet("""
            QPushButton { background: #e0e0e0; border-radius: 18px; padding: 10px 20px; }
            QPushButton:hover { background: #bdbdbd; }
        """)
        btn_rock.clicked.connect(lambda: self.play('rock'))

        btn_paper = QPushButton(" Paper")
        btn_paper.setIcon(QIcon("images/paper.png"))
        btn_paper.setIconSize(self.player_image.size())
        btn_paper.setFont(QFont('Arial', 12, QFont.Bold))
        btn_paper.setStyleSheet("""
            QPushButton { background: #e0e0e0; border-radius: 18px; padding: 10px 20px; }
            QPushButton:hover { background: #bdbdbd; }
        """)
        btn_paper.clicked.connect(lambda: self.play('paper'))

        btn_scissors = QPushButton(" Scissors")
        btn_scissors.setIcon(QIcon("images/scissors.png"))
        btn_scissors.setIconSize(self.player_image.size())
        btn_scissors.setFont(QFont('Arial', 12, QFont.Bold))
        btn_scissors.setStyleSheet("""
            QPushButton { background: #e0e0e0; border-radius: 18px; padding: 10px 20px; }
            QPushButton:hover { background: #bdbdbd; }
        """)
        btn_scissors.clicked.connect(lambda: self.play('scissors'))

        btn_exit = QPushButton("Exit")
        btn_exit.setFont(QFont('Arial', 12, QFont.Bold))
        btn_exit.setStyleSheet("""
            QPushButton { background: #d32f2f; color: #fff; border-radius: 18px; padding: 10px 20px; }
            QPushButton:hover { background: #b71c1c; }
        """)
        btn_exit.clicked.connect(self.close)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn_rock)
        btn_layout.addWidget(btn_paper)
        btn_layout.addWidget(btn_scissors)
        btn_layout.addWidget(btn_exit)
        btn_layout.setSpacing(20)

        art_layout = QHBoxLayout()
        player_vbox = QVBoxLayout()
        player_vbox.addWidget(self.player_text, alignment=Qt.AlignHCenter)
        player_vbox.addWidget(self.player_image, alignment=Qt.AlignHCenter)
        computer_vbox = QVBoxLayout()
        computer_vbox.addWidget(self.computer_text, alignment=Qt.AlignHCenter)
        computer_vbox.addWidget(self.computer_image, alignment=Qt.AlignHCenter)
        art_layout.addLayout(player_vbox)
        art_layout.addLayout(computer_vbox)
        art_layout.setSpacing(40)

        vbox = QVBoxLayout()
        vbox.addWidget(self.score_label, alignment=Qt.AlignHCenter)
        vbox.addWidget(self.choices_label, alignment=Qt.AlignHCenter)
        vbox.addLayout(btn_layout)
        vbox.addWidget(self.result_label, alignment=Qt.AlignHCenter)
        vbox.addLayout(art_layout)
        vbox.setSpacing(16)
        self.setLayout(vbox)
        self.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #f5f7fa, stop:1 #c3cfe2);")

    def score_text(self):
        return f"Score - You: {self.player_score}  Computer: {self.computer_score}  Ties: {self.ties}"

    def play(self, player_move):
        computer_move = random.choice(MOVES)
        self.player_image.setPixmap(QPixmap(f"images/{player_move}.png").scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.computer_image.setPixmap(QPixmap(f"images/{computer_move}.png").scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.player_text.setText(f"You chose: {player_move}")
        self.computer_text.setText(f"Computer chose: {computer_move}")
        if player_move == computer_move:
            result = "It's a tie!"
            self.ties += 1
        elif (player_move == 'rock' and computer_move == 'scissors') or \
             (player_move == 'paper' and computer_move == 'rock') or \
             (player_move == 'scissors' and computer_move == 'paper'):
            result = "You win!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1
        self.result_label.setText(result)
        self.score_label.setText(self.score_text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RochambeauGUI()
    window.show()
    sys.exit(app.exec())
