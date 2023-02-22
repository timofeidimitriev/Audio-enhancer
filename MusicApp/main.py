import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import pathlib

import ChooseAndSave

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle('Audio enhancer')
        self.setFixedSize(1280, 720)

        # Add a label
        self.label = QLabel('Auto enhancer', self)
        self.label.setGeometry(500, 50, 300, 30)
        self.label.setStyleSheet('font-size: 18px; font-weight: bold;')
        self.label.setAlignment(Qt.AlignCenter)
        # Add a button
        self.button = QPushButton('Select', self)
        self.button.setGeometry(500, 90, 300, 30)
        self.button.setStyleSheet('background-color: #333333; color: white; font-size: 16px; border-radius: 5px;')
        self.button.clicked.connect(self.move_audio)
        



    def move_audio(self):
        ChooseAndSave.Choose_Save()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
