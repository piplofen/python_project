import os
import platform
import sys
import webbrowser
from ctypes import windll
import docx2pdf

import PyPDF2
from PyQt6 import QtWidgets
from PyQt6.QtCore import QSettings, Qt, pyqtSignal, QEvent
from PyQt6.QtGui import QFont, QIcon, QAction
from PyQt6.QtWidgets import QColorDialog, QSystemTrayIcon, QMenu, QMessageBox

import maindesign
import settingsdesign
import convdesogn
import fromDocToPdfDesign

settings = QSettings("Programms", "Widget")

width = windll.user32.GetSystemMetrics(0)
height = windll.user32.GetSystemMetrics(1)

file = []

class MainClass(QtWidgets.QMainWindow, maindesign.Ui_MainWindow):

    tray_icon = None
    clicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.PATH = None

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("iico.ico"))

        show_action = QAction("Показать", self)
        hide_action = QAction("Свернуть", self)
        settings_action = QAction("Настройки", self)
        quit_action = QAction("Выход", self)

        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        settings_action.triggered.connect(self.openSettings)
        quit_action.triggered.connect(app.exit)

        tray_menu = QMenu()

        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(settings_action)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        self.setWindowFlag(Qt.WindowType.Tool, True)

        self.lbl1.setText(str(platform.node()))

        self.bttn1.clicked.connect(self.openScanFolder)

        self.bttnConvert.clicked.connect(self.openConvert)

        self.bttnImage.clicked.connect(self.openSettings)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        self.setWindowFlag(Qt.WindowType.WindowStaysOnBottomHint)

        self.startSettings(2)

        self.bttnFromDocxToPdf.clicked.connect(self.convert)

    def convert(self):
        F.show()

    def openConvert(self):
        C.show()

    def startSettings(self, value):
        if settings.allKeys() == []:
            settings.setValue("label color", str((0, 0, 0)))
            settings.setValue("label font", str("System"))
            settings.setValue("label font size", str(40))
            settings.setValue("label style font", str("bold"))
            settings.setValue("widget posH", str(int(height - (height * float(.955)))))
            settings.setValue("widget posV", str(int(width - (width * float(.15)))))

        else:
            self.lbl1.setFont(QFont(settings.value("label font")))
            self.lbl1.setStyleSheet(f"font-size: {settings.value('label font size')}pt;"
                                    f"color: rgb{settings.value('label color')};"
                                    f"font: {settings.value('label style font')};")
            self.setGeometry(int(settings.value('widget posH')), int(settings.value('widget posV')), 281, 241)

    def openSettings(self):
        S.show()

    def openScanFolder(self):
        self.lisDir = os.listdir("C:/")
        print(type(self.lisDir))
        print(self.lisDir)

        try:
            if "scan" not in self.lisDir:
                os.mkdir(r"C:/scan")
                self.PATH = r"C:/scan"
                webbrowser.open(r"C:/scan")
            else:
                print("scan")
                webbrowser.open(r"C:/scan")
        except:
            pass

        try:
            if "Scan" not in self.lisDir:
                os.mkdir(r"C:/scan")
                self.PATH = r"C:/scan"
                webbrowser.open(r"C:/scan")
            else:
                print("Scan")
                webbrowser.open(r"C:/Scan")
        except:
            pass

class SettingsClass(QtWidgets.QMainWindow, settingsdesign.Ui_SettingsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.vert.setMaximum(int(height))
        self.horz.setMaximum(int(width))


        self.vert.setValue(int(settings.value('widget posV')))
        self.horz.setValue(int(settings.value('widget posH')))

        #self.setGeometry(int(settings.value('widget posH')), int(settings.value('widget posV')), 281, 213)
        self.label_7.setText(str(width))
        self.label_9.setText(str(height))

        self.lbl2.setText(str(platform.node()))

        self.color_dialog = QColorDialog(self)

        self.bttn.clicked.connect(self.openColorDialog)
        self.cbFont.currentFontChanged.connect(self.setFontForLabel)
        self.spFontSize.valueChanged.connect(self.setFontSizeForLabel)
        self.rbBold.clicked.connect(self.setStyleFontForLabel)
        self.rbItalic.clicked.connect(self.setStyleFontForLabel)
        self.rbDefault.clicked.connect(self.setStyleFontForLabel)

        self.rbBold.setChecked(False)
        self.rbItalic.setChecked(False)
        self.rbDefault.setChecked(False)

        self.setWindowFlag(Qt.WindowType.Tool, True)

        self.colorForLabel = settings.value("label color")
        self.currentFontForLabel = settings.value("label font")
        self.fontSize = settings.value("label font size")
        self.StyleFontForLabel = settings.value("label style font")

        self.bttnSave.clicked.connect(self.saveValueForlabel)

        self.cbFont.setCurrentFont(QFont(self.currentFontForLabel))

        self.spFontSize.setValue(int(settings.value("label font size")))

        if self.StyleFontForLabel == "bold":
            self.rbBold.setChecked(True)
            self.rbItalic.setChecked(False)
            self.rbDefault.setChecked(False)
        elif self.StyleFontForLabel == "italic":
            self.rbItalic.setChecked(True)
            self.rbBold.setChecked(False)
            self.rbDefault.setChecked(False)
        elif self.StyleFontForLabel == "default":
            self.rbDefault.setChecked(True)
            self.rbBold.setChecked(False)
            self.rbItalic.setChecked(False)

        if settings.allKeys() == []:
            settings.setValue("label color", str((0, 0, 0)))
            settings.setValue("label font", str("System"))
            settings.setValue("label font size", str(40))
            settings.setValue("label style font", str("bold"))
        else:
            self.lbl2.setFont(QFont(settings.value("label font")))
            self.lbl2.setStyleSheet(f"font-size: {settings.value('label font size')}pt;"
                                    f"color: rgb{settings.value('label color')};"
                                    f"font: {settings.value('label style font')};")

    def openColorDialog(self):
        self.color_dialog.exec()
        value = self.color_dialog.currentColor()
        self.setColorForLabel(value.getRgb()[:3])

    def setFontSizeForLabel(self, value):
        global fontSize
        self.fontSize = value
        self.lbl2.setStyleSheet(f"font-size: {self.fontSize}pt;"
                                f"color: rgb{self.colorForLabel};"
                                f"font: {self.StyleFontForLabel};")

    def setColorForLabel(self, color):
        global colorForLabel
        self.colorForLabel = color
        print(self.colorForLabel)
        self.lbl2.setStyleSheet(f"font-size: {self.fontSize}pt;"
                                f"color: rgb{self.colorForLabel};"
                                f"font: {self.StyleFontForLabel};")

    def setFontForLabel(self, value):
        global currentFontForLabel
        self.currentFontForLabel = value
        self.lbl2.setFont(self.currentFontForLabel)
        self.lbl2.setStyleSheet(f"font-size: {self.fontSize}pt;"
                                f"color: rgb{self.colorForLabel};"
                                f"font: {self.StyleFontForLabel};")

    def setStyleFontForLabel(self):
        global StyleFontForLabel
        if self.rbBold.isChecked():
            self.StyleFontForLabel = "bold"
            self.lbl2.setStyleSheet(f"font-size: {self.fontSize}pt;"
                                    f"color: rgb{self.colorForLabel};"
                                    f"font: {self.StyleFontForLabel};")
        elif self.rbItalic.isChecked():
            self.StyleFontForLabel = "italic"
            self.lbl2.setStyleSheet(f"font-size: {self.fontSize}pt;"
                                    f"color: rgb{self.colorForLabel};"
                                    f"font: {self.StyleFontForLabel};")
        elif self.rbDefault.isChecked():
            self.StyleFontForLabel = "default"
            self.lbl2.setStyleSheet(f"font-size: {self.fontSize}pt;"
                                    f"color: rgb{self.colorForLabel};"
                                    f"font: {self.StyleFontForLabel};")

    def saveValueForlabel(self):
        global styleForlabel
        self.styleForLabel = self.lbl2.styleSheet()

        settings.setValue("label color", str(self.colorForLabel))
        settings.setValue("label font", str(self.cbFont.currentText()))
        settings.setValue("label font size", str(self.fontSize))
        settings.setValue("label style font", str(self.StyleFontForLabel))
        settings.setValue("widget posH", str(self.horz.value()))
        settings.setValue("widget posV", str(self.vert.value()))

        window.lbl1.setFont(QFont(settings.value("label font")))
        window.lbl1.setStyleSheet(f"font-size: {settings.value('label font size')}pt;"
                                  f"color: rgb{settings.value('label color')};"
                                  f"font: {settings.value('label style font')};")
        window.setGeometry(int(settings.value('widget posH')), int(settings.value('widget posV')), 281, 241)
        print("Save value complete.")

        print(f"{self.horz.value()} горизонтально")
        print(f"{self.vert.value()} вертикально")

        #self.close()

class ConvertClass(QtWidgets.QMainWindow, convdesogn.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setAcceptDrops(True)

        self.setWindowIcon(QIcon("title.ico"))

        self.setWindowFlag(Qt.WindowType.Tool, True)

        self.listWidget.setStyleSheet("border: 2px solid black")
        self.listWidget_2.setStyleSheet("border: 2px solid black")

        self.listWidget.installEventFilter(self)
        self.listWidget.setAcceptDrops(True)
        self.listWidget_2.installEventFilter(self)
        self.listWidget_2.setAcceptDrops(True)

        self.bttnCon.clicked.connect(self.convert)

    def closeEvent(self, event):
        self.listWidget.clear()
        self.listWidget.setStyleSheet("border: 2px solid black")
        self.listWidget_2.clear()
        self.listWidget_2.setStyleSheet("border: 2px solid black")

    def convert(self):
        try:
            fileSud = self.listWidget_2.item(0).text()

            for i in range(self.listWidget.count()):
                file.append(self.listWidget.item(i).text())

            for i in range(len(file)):
                self.mergeFile = PyPDF2.PdfFileMerger()
                self.mergeFile.append(PyPDF2.PdfFileReader(file[i]))
                self.mergeFile.append(PyPDF2.PdfFileReader(fileSud))
                file[i] = file[i].split("/")
                fileName = file[i].pop(int(len(file[i]) - 1))
                filePath = "/".join(file[i])
                #print(f"{filePath}/{fileName[:-4]} решение суда{fileName[-4:]}")
                self.mergeFile.write(f"{filePath}/{fileName[:-4]} решение суда{fileName[-4:]}")

            self.listWidget.clear()
            self.listWidget.setStyleSheet("border: 2px solid black")
            self.listWidget_2.clear()
            self.listWidget_2.setStyleSheet("border: 2px solid black")

            self.msg = QMessageBox()
            self.msg.setWindowFlag(Qt.WindowType.Tool, True)
            self.msg.setIcon(QMessageBox.Icon.Information)
            self.msg.setWindowIcon(QIcon("inf.ico"))
            self.msg.setText("Успешное слияние документов!")
            self.msg.setWindowTitle("Внимание")
            self.msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

            returnValue = self.msg.exec()
            self.close()

        except:

            self.msg = QMessageBox()
            self.msg.setWindowFlag(Qt.WindowType.Tool, True)
            self.msg.setIcon(QMessageBox.Icon.Information)
            self.msg.setWindowIcon(QIcon("inf.ico"))
            self.msg.setText("Добавьте файлы для слияния.")
            self.msg.setWindowTitle("Внимание")
            self.msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

            returnValue = self.msg.exec()
            self.listWidget.clear()
            self.listWidget.setStyleSheet("border: 2px solid black")
            self.listWidget_2.clear()
            self.listWidget_2.setStyleSheet("border: 2px solid black")


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
        if K == 1:
            if path[-4:] != ".pdf":
                pass
            elif path[-4:] == ".pdf":
                self.listWidget.addItem(str(path))
        if K == 2:
            if path[-4:] != ".pdf":
                pass
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

class FromClass(QtWidgets.QMainWindow, fromDocToPdfDesign.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setAcceptDrops(True)

        self.setWindowIcon(QIcon("title.ico"))

        self.setWindowFlag(Qt.WindowType.Tool, True)

        self.listWidget.setStyleSheet("border: 2px solid black")

        self.listWidget.installEventFilter(self)
        self.listWidget.setAcceptDrops(True)

        self.bttnCon.clicked.connect(self.convert)

    def closeEvent(self, event):
        self.listWidget.clear()
        self.listWidget.setStyleSheet("border: 2px solid black")

    def convert(self):
        try:
            for i in range(self.listWidget.count()):
                docx2pdf.convert(self.listWidget.item(i).text())
            self.msg = QMessageBox()
            self.msg.setWindowFlag(Qt.WindowType.Tool, True)
            self.msg.setIcon(QMessageBox.Icon.Information)
            self.msg.setWindowIcon(QIcon("inf.ico"))
            self.msg.setText("Успешное конвертирование документов!")
            self.msg.setWindowTitle("Внимание")
            self.msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

            returnValue = self.msg.exec()

            self.listWidget.clear()
            self.listWidget.setStyleSheet("border: 2px solid black")

            self.close()

        except:

            self.msg = QMessageBox()
            self.msg.setWindowFlag(Qt.WindowType.Tool, True)
            self.msg.setIcon(QMessageBox.Icon.Information)
            self.msg.setWindowIcon(QIcon("inf.ico"))
            self.msg.setText("Ошибка!")
            self.msg.setWindowTitle("Внимание")
            self.msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

            returnValue = self.msg.exec()
            self.listWidget.clear()
            self.listWidget.setStyleSheet("border: 2px solid black")

    def addFileListWidget(self, path):
        if path[-5:] != ".docx":
            pass
        elif path[-5:] == ".docx":
            self.listWidget.addItem(str(path))

    def eventFilter(self, source, event):
        global K
        if source == self.listWidget and event.type() == QEvent.Type.DragEnter:
            self.listWidget.setStyleSheet("border: 2px solid red")
        return super().eventFilter(source, event)

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
    global window, S, app, C, F
    app = QtWidgets.QApplication(sys.argv)
    window = MainClass()
    S = SettingsClass()
    C = ConvertClass()
    F = FromClass()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()