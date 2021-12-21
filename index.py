# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from task1 import Ui_Dialog1
from task2 import Ui_Dialog2
import sys
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.frame.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(47, 40, 285, 16))
        font = QtGui.QFont()
        font.setFamily("Nasalization")
        font.setPointSize(16)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(40, 120, 101, 17))
        self.pushButton.clicked.connect(self.open_task1)
        self.pushButton.setStyleSheet("background-color: white;\n"
"border-radius:2px\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 120, 101, 16))
        self.pushButton_3.clicked.connect(self.open_task2)
        self.pushButton_3.setStyleSheet("background-color: white;\n"
"border-radius: 2px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 220, 56, 17))
        self.pushButton_4.clicked.connect(app.exit)
        self.pushButton_4.setStyleSheet("background-color: white;\n"
"border-radius: 2px")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">IMAGE FORENSIC PROJECT</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Task 1"))
        self.pushButton_3.setText(_translate("Dialog", "Task 2"))
        self.pushButton_4.setText(_translate("Dialog", "EXIT"))

    def open_task1(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    def open_task2(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

