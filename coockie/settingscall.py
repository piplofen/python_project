import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
import settings
import qdarktheme

class SettingsWindow(QtWidgets.QMainWindow, settings.Ui_SettingsWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bttn_exit.clicked.connect(self.close)
        self.bttn_accept.clicked.connect(self.acceptSettings)

        with open("cfg.cfg", 'r') as file:
            value = file.readline()

        if value == "light":
            self.radioButton.setChecked(True)
            self.radioButton_2.setChecked(False)
        elif value == "dark":
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(True)

    def acceptSettings(self):
        if self.radioButton.isChecked():
            value = "light"
        elif self.radioButton_2.isChecked():
            value = "dark"
        with open("cfg.cfg", "w") as file:
            file.write(value)
        self.close() 
        return value

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = SettingsWindow()
    q = SettingsWindow()
    if q.acceptSettings() == "light": 
        window.show()
        app.exec()
    elif q.acceptSettings() == "dark":
        app.setStyleSheet(qdarktheme.load_stylesheet())
        window.show()
        app.exec()    

if __name__ == '__main__':
    main()