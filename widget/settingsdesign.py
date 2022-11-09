# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        SettingsWindow.resize(402, 407)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1904675-configuration-edit-gear-options-preferences-setting-settings_122525.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        SettingsWindow.setWindowIcon(icon)
        SettingsWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 384))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl2.sizePolicy().hasHeightForWidth())
        self.lbl2.setSizePolicy(sizePolicy)
        self.lbl2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.lbl2.setFont(font)
        self.lbl2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.lbl2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl2.setObjectName("lbl2")
        self.verticalLayout.addWidget(self.lbl2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.bttn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.bttn.setFont(font)
        self.bttn.setObjectName("bttn")
        self.gridLayout.addWidget(self.bttn, 0, 0, 1, 1)
        self.cbFont = QtWidgets.QFontComboBox(self.verticalLayoutWidget)
        self.cbFont.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.cbFont.setFont(font)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.cbFont.setCurrentFont(font)
        self.cbFont.setObjectName("cbFont")
        self.gridLayout.addWidget(self.cbFont, 1, 0, 1, 1)
        self.bttnSave = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.bttnSave.setFont(font)
        self.bttnSave.setObjectName("bttnSave")
        self.gridLayout.addWidget(self.bttnSave, 4, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spFontSize = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spFontSize.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.spFontSize.setFont(font)
        self.spFontSize.setMinimum(12)
        self.spFontSize.setMaximum(56)
        self.spFontSize.setProperty("value", 32)
        self.spFontSize.setObjectName("spFontSize")
        self.gridLayout_2.addWidget(self.spFontSize, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rbBold = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.rbBold.setFont(font)
        self.rbBold.setObjectName("rbBold")
        self.verticalLayout_2.addWidget(self.rbBold)
        self.rbItalic = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.rbItalic.setFont(font)
        self.rbItalic.setObjectName("rbItalic")
        self.verticalLayout_2.addWidget(self.rbItalic)
        self.rbDefault = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.rbDefault.setFont(font)
        self.rbDefault.setObjectName("rbDefault")
        self.verticalLayout_2.addWidget(self.rbDefault)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.vert = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.vert.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.vert.setObjectName("vert")
        self.horizontalLayout.addWidget(self.vert)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.horz = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horz.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horz.setObjectName("horz")
        self.horizontalLayout_2.addWidget(self.horz)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Окно настроек"))
        self.lbl2.setText(_translate("SettingsWindow", "PC-140"))
        self.bttn.setText(_translate("SettingsWindow", "Выбрать цвет"))
        self.bttnSave.setText(_translate("SettingsWindow", "Установить"))
        self.label.setText(_translate("SettingsWindow", "Размер шрифта"))
        self.label_2.setText(_translate("SettingsWindow", "Стиль шрифта"))
        self.rbBold.setText(_translate("SettingsWindow", "Жирный"))
        self.rbItalic.setText(_translate("SettingsWindow", "Курсив"))
        self.rbDefault.setText(_translate("SettingsWindow", "Обычный"))
        self.label_3.setText(_translate("SettingsWindow", "Расположение виджета"))
        self.label_4.setText(_translate("SettingsWindow", "Вертикально"))
        self.label_5.setText(_translate("SettingsWindow", "Горизонтально"))
        self.label_6.setText(_translate("SettingsWindow", "0"))
        self.label_7.setText(_translate("SettingsWindow", "0"))
        self.label_8.setText(_translate("SettingsWindow", "0"))
        self.label_9.setText(_translate("SettingsWindow", "0"))
