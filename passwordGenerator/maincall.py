import sys
from PyQt6 import QtWidgets
import maindesign
import random
import pyperclip

class MainClass(QtWidgets.QMainWindow, maindesign.Ui_MainClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.digit = "0123456789"
        self.charLower = "abcdefghijklnopqrstuvwxyz"
        self.charUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alpha = "+-/*!&$#?=@<>"
        self.result = []
        self.password = ""
        self.slider.valueChanged.connect(self.check)
        self.bttnGenerate.clicked.connect(self.generate)

    def check(self, value):
        self.labelForSlider.setText(str(value))

    def generate(self):
        value = self.labelForSlider.text()
        self.result.clear()
        if self.cbDigit.isChecked():
            self.result.extend(self.digit)
        if self.cbLower.isChecked():
            self.result.extend(self.charLower)
        if self.cbUpper.isChecked():
            self.result.extend(self.charUpper)
        if self.cbAlpha.isChecked():
            self.result.extend(self.alpha)

        for n in range(len(self.result)):
            self.password = ""
            for i in range(int(self.labelForSlider.text())):
                self.password += random.choice(self.result)

        self.lineEditPassword.setText(self.password)

        pyperclip.copy(self.lineEditPassword.text())

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainClass()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()