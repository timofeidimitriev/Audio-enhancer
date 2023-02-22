import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle('My Beautiful Interface')
        self.setGeometry(200, 200, 1280, 720)

        # Add a label
        self.label = QLabel('Enter your name:', self)
        self.label.setGeometry(50, 50, 300, 30)
        self.label.setStyleSheet('font-size: 18px; font-weight: bold;')

        # Add a text input field
        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 90, 300, 30)
        self.textbox.setStyleSheet('font-size: 16px;')

        # Add a button
        self.button = QPushButton('Submit', self)
        self.button.setGeometry(50, 130, 300, 30)
        self.button.setStyleSheet('background-color: #0080ff; color: white; font-size: 16px;')
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        name = self.textbox.text()
        message = f'Hello, {name}!'
        self.statusBar().showMessage(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
