import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        self.lcdNumber = QLCDNumber()
        self.lcdNumber.setGeometry(QRect(0, 0, 551, 211))
        self.lcdNumber.setProperty("intValue", 111)

        self.grid = QGridLayout(self.centralwidget)
        self.grid.addWidget(self.lcdNumber)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.resize(550, 246)
    ex.show()
    sys.exit(app.exec())