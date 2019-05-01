# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/Design/newFADialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from model import NFA, DFA


class Ui_NewFADialog(QtWidgets.QDialog):
    # Added constructor (don't change!!!)
    def __init__(self, parent):
        super(Ui_NewFADialog, self).__init__()
        self.parent = parent
        self.setupUi()

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.close)

        self.nonDetermnstc_chkBox.stateChanged.connect(self.checkNonDeterminism)

        self.show()
    # end of the constructor


    ##########################################################################################
    # QtDesigner auto generated code
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(293, 224)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(50, 170, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(80, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.epsilonT_chkBox = QtWidgets.QCheckBox(self)
        self.epsilonT_chkBox.setEnabled(False)
        self.epsilonT_chkBox.setGeometry(QtCore.QRect(40, 120, 201, 31))
        self.epsilonT_chkBox.setObjectName("epsilonT_chkBox")
        self.entry_alphabet_input = QtWidgets.QLineEdit(self)
        self.entry_alphabet_input.setGeometry(QtCore.QRect(70, 50, 151, 25))
        self.entry_alphabet_input.setObjectName("entry_alphabet_input")
        self.nonDetermnstc_chkBox = QtWidgets.QCheckBox(self)
        self.nonDetermnstc_chkBox.setGeometry(QtCore.QRect(40, 90, 201, 31))
        self.nonDetermnstc_chkBox.setObjectName("nonDetermnstc_chkBox")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    # QtDesigner auto generated code
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Input Alphabet"))
        self.epsilonT_chkBox.setText(_translate("Dialog", "Enable Epsilon-transitions"))
        self.nonDetermnstc_chkBox.setText(_translate("Dialog", "Non-Deterministic"))

    ##########################################################################################
    # DIALOG BUTTONS FUNCTIONS
    # create a new FAWindow with a based model to the transition table based on this form
    def accept(self):
        # TESTAR SE A ENTRADA DADA EH UM ALFABETO VALIDO (setValidator)

        # Cria uma lista dos caracteres presentes no alfabeto
        alphabet = self.entry_alphabet_input.text().split(",")
        for i in range(len(alphabet)):
            alphabet[i] = alphabet[i].replace(" ", "")

        if (self.checkNonDeterminism()):
            epsilonEnabled = self.epsilonT_chkBox.isChecked()
            fa = NFA([], alphabet, '', [], {}, epsilonEnabled)
        else:
            fa = DFA([], alphabet, '', [], {})

        self.close()
        self.parent.createEditor(fa)


    # check if the non-determinism checkBox is checked and enable epsilonT_chkBox if true
    def checkNonDeterminism(self):
        bool = self.nonDetermnstc_chkBox.isChecked()
        self.epsilonT_chkBox.setEnabled(bool)

        return bool
