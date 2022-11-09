# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.resize(281, 241)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.PreventContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iico.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("#Widget{\n"
"background-color: blue;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 264, 227))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bttnImage = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.bttnImage.setMaximumSize(QtCore.QSize(16777215, 50))
        self.bttnImage.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bttnImage.setStyleSheet("#bttnImage{\n"
"background-color: transparent;\n"
"}")
        self.bttnImage.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.bttnImage.setIcon(icon1)
        self.bttnImage.setIconSize(QtCore.QSize(250, 250))
        self.bttnImage.setObjectName("bttnImage")
        self.verticalLayout_2.addWidget(self.bttnImage)
        self.lbl1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl1.sizePolicy().hasHeightForWidth())
        self.lbl1.setSizePolicy(sizePolicy)
        self.lbl1.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.lbl1.setFont(font)
        self.lbl1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.lbl1.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.lbl1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl1.setObjectName("lbl1")
        self.verticalLayout_2.addWidget(self.lbl1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(16, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bttn1 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bttn1.sizePolicy().hasHeightForWidth())
        self.bttn1.setSizePolicy(sizePolicy)
        self.bttn1.setMaximumSize(QtCore.QSize(235, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.bttn1.setFont(font)
        self.bttn1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bttn1.setObjectName("bttn1")
        self.verticalLayout.addWidget(self.bttn1)
        self.bttnConvert = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bttnConvert.sizePolicy().hasHeightForWidth())
        self.bttnConvert.setSizePolicy(sizePolicy)
        self.bttnConvert.setMaximumSize(QtCore.QSize(235, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.bttnConvert.setFont(font)
        self.bttnConvert.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bttnConvert.setObjectName("bttnConvert")
        self.verticalLayout.addWidget(self.bttnConvert)
        self.bttnFromDocxToPdf = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bttnFromDocxToPdf.sizePolicy().hasHeightForWidth())
        self.bttnFromDocxToPdf.setSizePolicy(sizePolicy)
        self.bttnFromDocxToPdf.setMaximumSize(QtCore.QSize(235, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.bttnFromDocxToPdf.setFont(font)
        self.bttnFromDocxToPdf.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bttnFromDocxToPdf.setObjectName("bttnFromDocxToPdf")
        self.verticalLayout.addWidget(self.bttnFromDocxToPdf)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(440, 80, 218, 33))
        self.image.setMaximumSize(QtCore.QSize(16777215, 50))
        self.image.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.image.setMouseTracking(True)
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("image.png"))
        self.image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.image.setObjectName("image")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Виджет"))
        self.lbl1.setText(_translate("MainWindow", "PC-140"))
        self.bttn1.setText(_translate("MainWindow", "Папка скан"))
        self.bttnConvert.setText(_translate("MainWindow", "↓"))
        self.bttnFromDocxToPdf.setText(_translate("MainWindow", "↺"))
