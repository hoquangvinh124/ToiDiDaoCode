# Form implementation generated from reading ui file 'D:\TDT!!!\E71\ui\BlueLock_Bank.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 581)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 181, 51))
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 90, 311, 461))
        self.groupBox.setObjectName("groupBox")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.groupBox)
        self.scrollArea.setGeometry(QtCore.QRect(9, 26, 291, 421))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 289, 419))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listWidget = QtWidgets.QListWidget(parent=self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 271, 401))
        self.listWidget.setObjectName("listWidget")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(370, 130, 301, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(14, 30, 101, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 171, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 70, 211, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(14, 70, 61, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 110, 211, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(14, 110, 61, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(80, 150, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 150, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(370, 370, 301, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 60, 111, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 100, 111, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 100, 111, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_6.setGeometry(QtCore.QRect(160, 60, 111, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 20, 111, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cuop Nha Bank"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#0055ff;\">BLUELOCK BANK</span></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Current Account"))
        self.groupBox_2.setTitle(_translate("MainWindow", "New Account/Authentication:"))
        self.label_2.setText(_translate("MainWindow", "Account number:"))
        self.label_3.setText(_translate("MainWindow", "Pin:"))
        self.label_4.setText(_translate("MainWindow", "Name:"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancelling"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Functions:"))
        self.pushButton_3.setText(_translate("MainWindow", "Withdraw"))
        self.pushButton_4.setText(_translate("MainWindow", "Transfer"))
        self.pushButton_5.setText(_translate("MainWindow", "Show Transaction"))
        self.pushButton_6.setText(_translate("MainWindow", "Balance"))
        self.pushButton_7.setText(_translate("MainWindow", "Deposit"))
