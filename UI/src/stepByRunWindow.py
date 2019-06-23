# -*- coding: utf-8 -*-

# description: "Projeto da disciplina de Linguagens Formais 2019.1"
# authors:
#     "Arthur Mesquita Pickcius",
#     "Francisco Luiz Vicenzi",
#     "Joao Fellipe Uller"
# Copyright 2019

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StepByRunWindow(QtWidgets.QWidget):
    # Constructor
    def __init__(self, parent, word_input):
        super(Ui_StepByRunWindow, self).__init__()
        self.parent = parent
        self.FA = self.parent.FA
        self.actualIndex = 0
        self.word = word_input
        self.status = "Running"

        self.setupUi()
        self.prepareUI()

        self.step_pushButton.clicked.connect(self.makeStep)
        self.reset_pushButton.clicked.connect(self.resetRun)

        self.show()


    ####################################################################
    # QtDesigner auto generated code
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(329, 318)
        self.entry_label = QtWidgets.QLabel(self)
        self.entry_label.setGeometry(QtCore.QRect(0, 30, 321, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.entry_label.setFont(font)
        self.entry_label.setAlignment(QtCore.Qt.AlignCenter)
        self.entry_label.setObjectName("entry_label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(60, 170, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(60, 210, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.step_pushButton = QtWidgets.QPushButton(self)
        self.step_pushButton.setGeometry(QtCore.QRect(60, 270, 89, 25))
        self.step_pushButton.setObjectName("step_pushButton")
        self.reset_pushButton = QtWidgets.QPushButton(self)
        self.reset_pushButton.setGeometry(QtCore.QRect(170, 270, 89, 25))
        self.reset_pushButton.setObjectName("reset_pushButton")
        self.currentState_out = QtWidgets.QLabel(self)
        self.currentState_out.setGeometry(QtCore.QRect(180, 90, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currentState_out.setFont(font)
        self.currentState_out.setObjectName("currentState_out")
        self.lastState_out = QtWidgets.QLabel(self)
        self.lastState_out.setGeometry(QtCore.QRect(180, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lastState_out.setFont(font)
        self.lastState_out.setObjectName("lastState_out")
        self.lastSymbol_out = QtWidgets.QLabel(self)
        self.lastSymbol_out.setGeometry(QtCore.QRect(180, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lastSymbol_out.setFont(font)
        self.lastSymbol_out.setObjectName("lastSymbol_out")
        self.status_out = QtWidgets.QLabel(self)
        self.status_out.setGeometry(QtCore.QRect(180, 210, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.status_out.setFont(font)
        self.status_out.setObjectName("status_out")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    # QtDesigner auto generated code
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Step by step run..."))
        self.label_2.setText(_translate("Form", "Current State:"))
        self.label_3.setText(_translate("Form", "Last state:"))
        self.label_4.setText(_translate("Form", "Last Symbol: "))
        self.label_5.setText(_translate("Form", "Status:"))
        self.step_pushButton.setText(_translate("Form", "Step"))
        self.reset_pushButton.setText(_translate("Form", "Reset"))


    # end of QtDesigner auto-generated code
    ############################################################################

    # prepares the UI to the step-by-step execution
    def prepareUI(self):
        self.openFontColor = "<font color=\"gray\">"
        self.entry_label.setText(self.word)
        self.currentState_out.setText(self.FA.init_state)
        self.lastState_out.setText("-")
        self.lastSymbol_out.setText("-")
        self.status_out.setText(self.status)
        self.step_pushButton.setEnabled(True)

    ###########################################################################3

    # RUN CONTROL
    # goes a step ahead on the running
    def makeStep(self):
        if len(self.word) > 0:
            symbol = (self.word)[self.actualIndex]
            self.lastState_out.setText(self.FA.current_state)
            self.FA.make_transition(symbol)
            self.lastSymbol_out.setText(symbol)
            self.actualIndex += 1

        state = self.FA.current_state
        if self.actualIndex == len(self.word):
            if state in self.FA.final_states:
                self.status = "Accepted"
            else:
                self.status = "Rejected"

        elif state == self.FA.dead_state:
            self.status = "Rejected"

        self.updateUIActualState()


    # resets the running to the initial state
    def resetRun(self):
        self.actualIndex = 0
        self.status = "Running"
        self.FA.reset_init_state()
        self.prepareUI()


    # updates the UI interaction
    def updateUIActualState(self):
        word = self.word
        if self.status != "Running":
            self.step_pushButton.setEnabled(False)

            if self.status == "Accepted":
                self.status_out.setText("<font color=\"green\">" + self.status + "</font>")
            else:
                self.status_out.setText("<font color=\"red\">" + self.status + "</font>")

            self.entry_label.setText(self.openFontColor + word + "</font>")

        else:
            # updates entry_label colorization
            word = word[:self.actualIndex] + "</font>" + word[self.actualIndex:]
            self.entry_label.setText(self.openFontColor + word)
            self.currentState_out.setText(self.FA.current_state)
