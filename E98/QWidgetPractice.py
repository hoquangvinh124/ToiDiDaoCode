# Form implementation generated from reading ui file 'D:\TDT!!!\E98\QWidgetPractice.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 412)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.number_input = QtWidgets.QLineEdit(parent=self.groupBox)
        self.number_input.setObjectName("number_input")
        self.horizontalLayout.addWidget(self.number_input)
        self.update_button = QtWidgets.QPushButton(parent=self.groupBox)
        self.update_button.setObjectName("update_button")
        self.horizontalLayout.addWidget(self.update_button)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.numbers_list = QtWidgets.QListWidget(parent=self.groupBox_2)
        self.numbers_list.setObjectName("numbers_list")
        self.verticalLayout_2.addWidget(self.numbers_list)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_sum = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btn_sum.setObjectName("btn_sum")
        self.verticalLayout_3.addWidget(self.btn_sum)
        self.btn_remove_ends = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btn_remove_ends.setObjectName("btn_remove_ends")
        self.verticalLayout_3.addWidget(self.btn_remove_ends)
        self.btn_remove_selected = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btn_remove_selected.setObjectName("btn_remove_selected")
        self.verticalLayout_3.addWidget(self.btn_remove_selected)
        self.btn_double = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btn_double.setObjectName("btn_double")
        self.verticalLayout_3.addWidget(self.btn_double)
        self.btn_square = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btn_square.setObjectName("btn_square")
        self.verticalLayout_3.addWidget(self.btn_square)
        self.btn_highlight_even = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btn_highlight_even.setObjectName("btn_highlight_even")
        self.verticalLayout_3.addWidget(self.btn_highlight_even)
        self.btn_highlight_odd = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btn_highlight_odd.setObjectName("btn_highlight_odd")
        self.verticalLayout_3.addWidget(self.btn_highlight_odd)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.exit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exit_button.setObjectName("exit_button")
        self.verticalLayout.addWidget(self.exit_button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.exit_button.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Number Processor"))
        self.groupBox.setTitle(_translate("MainWindow", "Input Number:"))
        self.update_button.setText(_translate("MainWindow", "Update"))
        self.groupBox_2.setTitle(_translate("MainWindow", "List of Numbers:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Functions:"))
        self.btn_sum.setText(_translate("MainWindow", "Sum of all numbers"))
        self.btn_remove_ends.setText(_translate("MainWindow", "Remove first and last element"))
        self.btn_remove_selected.setText(_translate("MainWindow", "Remove selected element"))
        self.btn_double.setText(_translate("MainWindow", "Increment double value"))
        self.btn_square.setText(_translate("MainWindow", "Change selected element to square"))
        self.btn_highlight_even.setText(_translate("MainWindow", "High-light even elements"))
        self.btn_highlight_odd.setText(_translate("MainWindow", "High-light odd elements"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
