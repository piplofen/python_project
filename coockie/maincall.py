import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTreeWidgetItem
import main
import os
import settingscall
import qdarktheme

class MainClass(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.word = ["domain","expirationDate","httpOnly","name","path","secure","value"]

        self.settings_window = settingscall.SettingsWindow()

        self.pushButton.clicked.connect(self.download)
        self.pushButton_2.clicked.connect(self.openSettings)
        self.bttn_exit.clicked.connect(self.close)
        self.value = []
        self.count = 0

        for i in range(len(os.listdir())):
            self.comboBox.addItem(os.listdir()[i])

    def openSettings(self):
        self.settings_window.show()

    def download(self):
        if self.comboBox.currentText() == "Cookies_List.txt":
            self.treeWidget.clear()
            with open(self.comboBox.currentText(), 'r') as file:
                for line in file.readlines():
                    if self.word[0] in line:
                        line = line[8:-2]
                        self.value.append(line)
                        self.count += 1

                    elif self.word[1] in line:
                        line = line[8:-3]
                        self.value.append(line)

                    elif self.word[2] in line:
                        line = line[8:-2]
                        self.value.append(line)

                    elif self.word[3] in line:
                        line = line[8:-2]
                        self.value.append(line)

                    elif self.word[4] in line:
                        line = line[8:-2]
                        self.value.append(line)

                    elif self.word[5] in line:
                        line = line[8:-2]
                        self.value.append(line)

                    elif self.word[6] in line:
                        line = line[8:-1]
                        self.value.append(line)


            self.treeWidget.setHeaderLabels(['Название'])
            self.label.setText("Количество полученных кук: " + str(self.count-1))

            k = 7

            print(self.count)

            for i in range(self.count-1):
                if i < 188:
                    self.itemDomain = QTreeWidgetItem(self.treeWidget)
                    self.itemExpirationDate = QTreeWidgetItem(self.itemDomain)
                    self.itemHttpOnly = QTreeWidgetItem(self.itemDomain)
                    self.itemName = QTreeWidgetItem(self.itemDomain)
                    self.itemPath = QTreeWidgetItem(self.itemDomain)
                    self.itemSecure = QTreeWidgetItem(self.itemDomain)
                    self.itemValue = QTreeWidgetItem(self.itemDomain)

                    self.itemDomain.setText(0, str(f"{i+1} - " + self.value[k*i]))
                    self.itemExpirationDate.setText(0, str(self.value[k*i+1]))
                    self.itemHttpOnly.setText(0, str(self.value[k*i+2]))
                    self.itemName.setText(0, str(self.value[k*i+3]))
                    self.itemPath.setText(0, str(self.value[k*i+4]))
                    self.itemSecure.setText(0, str(self.value[k*i+5]))
                    self.itemValue.setText(0, str(self.value[k*i+6]))

            self.count = 0
        else:
            print("ERROR")
            self.label.setText("Выберите другой файл")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainClass()
    q = settingscall.SettingsWindow()
    if q.acceptSettings() == "light": 
        window.show()
        app.exec()
    elif q.acceptSettings() == "dark":
        app.setStyleSheet(qdarktheme.load_stylesheet())
        window.show()
        app.exec() 

if __name__ == '__main__':
    main()