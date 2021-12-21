# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import progressbar
from time import sleep


class Ui_Dialog2(object):
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
        self.label.setGeometry(QtCore.QRect(70, 40, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Nasalization")
        font.setPointSize(12)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.clicked.connect(self.task1)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 220, 101, 17))
        self.pushButton_4.setStyleSheet("background-color: white;\n"
"border-radius: 2px")
        self.pushButton_4.setObjectName("pushButton_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 70, 301, 131))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#aa0000;\">image splicing detection</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Dialog", "START"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "Image splicing is an image editing method to copy a part of an image and paste it onto another image, and it is commonly followed by postprocessing such as local/global blurring, compression, and resizing. To detect this kind of forgery, the image rich models, a feature set successfully used in the steganalysis is evaluated on the splicing image dataset at first, and the dominant submodel is selected as the first kind of feature. The selected feature and the DCT Markov features are used together to detect splicing forgery in the chroma channel, which is convinced effective in splicing detection. The experimental results indicate that the proposed method can detect splicing forgeries with lower error rate compared to the previous literature."))

    def task1(self):
        for i in range(21):
            sys.stdout.write('\r')
            # the exact output you're looking for:
            sys.stdout.write("[%-20s] %d%%" % ('=' * i, 5 * i))
            sys.stdout.flush()
            sleep(0.95)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

