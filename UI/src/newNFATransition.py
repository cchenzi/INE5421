# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/Design/newTransitionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_NFATransitionDialog(object):
    # Constructor (don't change!!)
    def __init__(self, insertFunction, states, alphabet):
        self.dialog = QtWidgets.QDialog()
        self.setupUi(self.dialog)

        self.buttonBox.accepted.connect(insertFunction)
        self.buttonBox.rejected.connect(self.dialog.close)

        self.comboBox_Src.addItems(states)
        self.comboBox_Dst.addItems(states)
        self.comboBox_Input.addItems(alphabet)

        self.dialog.show()


    ##############################################################################
    # QtDesigner auto-generated code
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(236, 205)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 160, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 41, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 80, 81, 17))
        self.label_3.setObjectName("label_3")
        self.comboBox_Src = QtWidgets.QComboBox(Dialog)
        self.comboBox_Src.setGeometry(QtCore.QRect(10, 110, 86, 25))
        self.comboBox_Src.setObjectName("comboBox_Src")
        self.comboBox_Dst = QtWidgets.QComboBox(Dialog)
        self.comboBox_Dst.setGeometry(QtCore.QRect(140, 110, 86, 25))
        self.comboBox_Dst.setObjectName("comboBox_Dst")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 110, 16, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 10, 41, 17))
        self.label_5.setObjectName("label_5")
        self.comboBox_Input = QtWidgets.QComboBox(Dialog)
        self.comboBox_Input.setGeometry(QtCore.QRect(70, 40, 86, 25))
        self.comboBox_Input.setObjectName("comboBox_Input")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # QtDesigner auto-generated code
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NewTransition..."))
        self.label_2.setText(_translate("Dialog", "Origin"))
        self.label_3.setText(_translate("Dialog", "Destination"))
        self.label_4.setText(_translate("Dialog", "->"))
        self.label_5.setText(_translate("Dialog", "Input"))


    # Closes the window
    def close(self):
        self.dialog.close()
