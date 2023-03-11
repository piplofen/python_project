import sys
from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import *
from PyQt6 import QtCore

import testsizecopyDesign

class MainClass(QtWidgets.QMainWindow, testsizecopyDesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.toolBar.setMinimumSize(75, 0)
        self.toolBar.setIconSize(QtCore.QSize(52, 52))
        self.toolBar.addAction(QIcon("iico.ico"), "Главное меню", self.main1)
        self.toolBar.addAction(QIcon("deal.png"), "Ваши сделки", self.main2)
        self.toolBar.addAction(QIcon("contact.png"), "Контакты", self.main3)


    def main1(self):
        self.stackedWidget.setCurrentIndex(0)

    def main2(self):
        self.stackedWidget.setCurrentIndex(1)

    def main3(self):
        self.stackedWidget.setCurrentIndex(2)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
