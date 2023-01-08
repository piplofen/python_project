import sys
import PyPDF2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QEvent, QMimeData
from PyQt5.QtGui import QDrag, QPixmap, QPainter
from PyQt5.QtWidgets import QMessageBox, QLabel, QPushButton, QListWidget
from PyQt5.uic.properties import QtCore

import maindesign

K = 0

class MainClass(QtWidgets.QMainWindow, maindesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setAcceptDrops(True)

        self.listWidget.installEventFilter(self)
        self.listWidget.setAcceptDrops(True)
        self.listWidget_2.installEventFilter(self)
        self.listWidget_2.setAcceptDrops(True)

    #     self.label.installEventFilter(self)
    #     self.label.setAcceptDrops(True)
    #     self.label_2.installEventFilter(self)


    def eventFilter(self, source, event):
        global K
        if source == self.listWidget and event.type() == QEvent.Type.DragEnter:
            K = 1
            self.listWidget.setStyleSheet("border: 2px solid red")
        elif source == self.listWidget_2 and event.type() == QEvent.Type.DragEnter:
            K = 2
            self.listWidget_2.setStyleSheet("border: 2px solid blue")
        elif source != self.listWidget and source != self.listWidget_2:
            K = 0
        return super().eventFilter(source, event)

    def addFileListWidget(self, path):
        print(K)
        if K == 1:
            print(path)
            if path[-4:] != ".pdf":
                print("-")
            elif path[-4:] == ".pdf":Гавно
                self.listWidget.addItem(str(path))
        if K == 2:
            if path[-4:] != ".pdf":
                print("-")
            elif path[-4:] == ".pdf":
                self.listWidget_2.addItem(str(path))

    def dragEnterEvent(self, event):
        if event.mimeData().hasText:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasText:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasText:
            event.accept()
            for url in event.mimeData().urls():
                file_name = url.toLocalFile()
                self.addFileListWidget(file_name)
        else:
            event.ignore()

def main():
    global app, window
    app = QtWidgets.QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
