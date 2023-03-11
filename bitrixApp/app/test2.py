import sys

from PyQt6 import QtWidgets

import test2Design


class MainClass(QtWidgets.QMainWindow, test2Design.Ui_MainWindow):
    def __init__(self):
        super().__init__()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
