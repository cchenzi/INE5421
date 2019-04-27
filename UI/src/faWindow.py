# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/Design/faWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QTableWidgetItem


class Ui_FAWindow(object):
    # Added constructor (don't overwrite)
    def __init__(self, alphabet):
        self.window = QtWidgets.QMainWindow()
        self.initialState_radioGroup = QtWidgets.QButtonGroup()
        self.setupUi(self.window)
        self.connectSignals()

        self.transition_table.insertColumn(0)
        self.transition_table.setColumnWidth(0, 20)
        self.transition_table.insertColumn(1)
        self.transition_table.setColumnWidth(1, 20)

        alphabet.insert(0, "state")
        for i in range(len(alphabet)):
            self.transition_table.insertColumn(i+2)
            self.transition_table.setColumnWidth(i+2, 50)
        self.transition_table.setHorizontalHeaderLabels(["->", "*"] + alphabet)

        self.window.show()
    # end of contructor

    ##########################################################################################
    # QtDesigner auto generated code
    def setupUi(self, FAWindow):
        FAWindow.setObjectName("FAWindow")
        FAWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(FAWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.transition_table = QtWidgets.QTableWidget(self.centralwidget)
        self.transition_table.setGeometry(QtCore.QRect(150, 10, 481, 441))
        self.transition_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.transition_table.setDragDropOverwriteMode(False)
        self.transition_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.transition_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.transition_table.setWordWrap(False)
        self.transition_table.setObjectName("transition_table")
        self.transition_table.setColumnCount(0)
        self.transition_table.setRowCount(0)
        self.transition_table.horizontalHeader().setVisible(True)
        self.transition_table.horizontalHeader().setHighlightSections(True)
        self.transition_table.verticalHeader().setVisible(False)
        self.transition_table.verticalHeader().setHighlightSections(False)
        self.pushButton_insertState = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_insertState.setGeometry(QtCore.QRect(30, 90, 89, 25))
        self.pushButton_insertState.setObjectName("pushButton_insertState")
        self.pushButton_removeState = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_removeState.setGeometry(QtCore.QRect(30, 130, 89, 25))
        self.pushButton_removeState.setObjectName("pushButton_removeState")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 51, 17))
        self.label.setObjectName("label")
        FAWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FAWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuInput = QtWidgets.QMenu(self.menubar)
        self.menuInput.setObjectName("menuInput")
        self.menuConvert = QtWidgets.QMenu(self.menubar)
        self.menuConvert.setObjectName("menuConvert")
        FAWindow.setMenuBar(self.menubar)
        self.file_actionNew = QtWidgets.QAction(FAWindow)
        self.file_actionNew.setObjectName("file_actionNew")
        self.file_actionOpen = QtWidgets.QAction(FAWindow)
        self.file_actionOpen.setObjectName("file_actionOpen")
        self.file_actionSave = QtWidgets.QAction(FAWindow)
        self.file_actionSave.setObjectName("file_actionSave")
        self.file_actionSaveAs = QtWidgets.QAction(FAWindow)
        self.file_actionSaveAs.setObjectName("file_actionSaveAs")
        self.file_actionClose = QtWidgets.QAction(FAWindow)
        self.file_actionClose.setObjectName("file_actionClose")
        self.convert_actionToDFA = QtWidgets.QAction(FAWindow)
        self.convert_actionToDFA.setObjectName("convert_actionToDFA")
        self.convert_actionToGramm = QtWidgets.QAction(FAWindow)
        self.convert_actionToGramm.setObjectName("convert_actionToGramm")
        self.menuFile.addAction(self.file_actionNew)
        self.menuFile.addAction(self.file_actionOpen)
        self.menuFile.addAction(self.file_actionSave)
        self.menuFile.addAction(self.file_actionSaveAs)
        self.menuFile.addAction(self.file_actionClose)
        self.menuConvert.addAction(self.convert_actionToDFA)
        self.menuConvert.addAction(self.convert_actionToGramm)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInput.menuAction())
        self.menubar.addAction(self.menuConvert.menuAction())

        self.retranslateUi(FAWindow)
        QtCore.QMetaObject.connectSlotsByName(FAWindow)

    # QtDesigner auto generated code
    def retranslateUi(self, FAWindow):
        _translate = QtCore.QCoreApplication.translate
        FAWindow.setWindowTitle(_translate("FAWindow", "MainWindow"))
        self.pushButton_insertState.setText(_translate("FAWindow", "Insert"))
        self.pushButton_removeState.setText(_translate("FAWindow", "Remove"))
        self.label.setText(_translate("FAWindow", "States"))
        self.menuFile.setTitle(_translate("FAWindow", "File"))
        self.menuInput.setTitle(_translate("FAWindow", "Input"))
        self.menuConvert.setTitle(_translate("FAWindow", "Convert"))
        self.file_actionNew.setText(_translate("FAWindow", "New"))
        self.file_actionOpen.setText(_translate("FAWindow", "Open"))
        self.file_actionSave.setText(_translate("FAWindow", "Save"))
        self.file_actionSaveAs.setText(_translate("FAWindow", "Save as..."))
        self.file_actionClose.setText(_translate("FAWindow", "Close"))
        self.convert_actionToDFA.setText(_translate("FAWindow", "Determinize to DFA"))
        self.convert_actionToGramm.setText(_translate("FAWindow", "Convert to Grammar"))


    ##########################################################################################
    # Connect signals with their respective actions
    def connectSignals(self):
        self.pushButton_insertState.clicked.connect(self.createInsertStateDialog)
        self.pushButton_removeState.clicked.connect(self.removeState)
        self.file_actionNew.triggered.connect(self.createNewFA)
        self.file_actionOpen.triggered.connect(self.loadFA)
        self.file_actionSave.triggered.connect(self.saveFA)
        self.file_actionSaveAs.triggered.connect(self.createFAFile)
        self.file_actionClose.triggered.connect(self.closeWindow)
        self.convert_actionToDFA.triggered.connect(self.convertToDFA)
        self.convert_actionToGramm.triggered.connect(self.convertToGrammar)

    # TRANSITION TABLE MANIPULATION FUNCTIONS
    # Creates a dialog for user insert new state label
    def createInsertStateDialog(self):
        dialog = QtWidgets.QDialog()
        dialog.resize(253, 137)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 90, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 91, 17))
        self.label.setText("State Label:")
        self.stateLabel_input = QtWidgets.QLineEdit(dialog)
        self.stateLabel_input.setGeometry(QtCore.QRect(30, 50, 191, 25))

        self.buttonBox.accepted.connect(self.insertState)
        self.buttonBox.rejected.connect(dialog.close)
        self.newStateDialog = dialog
        self.newStateDialog.show()


    # Insert a new state on the transition table
    def insertState(self):
        label = self.stateLabel_input.text()

        if label in self.get_afStates():
            dialog = QtWidgets.QDialog()
            dialog.resize(253, 137)
            self.errorLabel = QtWidgets.QLabel(dialog)
            self.errorLabel.setText("This state already exists!!")
            self.errorDialog = dialog
            self.errorDialog.show()

        else:
            new_index = self.transition_table.rowCount()
            self.transition_table.insertRow(new_index)

            radio = QtWidgets.QRadioButton()
            self.initialState_radioGroup.addButton(radio)
            self.transition_table.setCellWidget(new_index, 0, radio)
            self.transition_table.setCellWidget(new_index, 1, QtWidgets.QCheckBox())
            self.transition_table.setItem(new_index, 2, QTableWidgetItem(label))

            for i in range(3, self.transition_table.columnCount()):
                combo = QtWidgets.QComboBox()
                self.transition_table.setCellWidget(new_index, i, combo)

            self.updateComboBoxes()
        #end if

        self.newStateDialog.close()


    # Remove the selected state from the transition table
    def removeState(self):
        row = self.transition_table.selectedItems()[0].row()
        self.transition_table.removeRow(row)
        self.updateComboBoxes()


    # MENU CONVERT ACTION HANDLERS
    # convert to dfa
    def convertToDFA(self):
        print("Determinize")

    # convert to grammar
    def convertToGrammar(self):
        print("to Grammar")


    # FILE ACTION HANDLER FUNCTIONS
    # new
    def createNewFA(self):
        print("New file")

    # open
    def loadFA(self):
        print("Open file")

    # save
    def saveFA(self):
        print("Save")

    # save as
    def createFAFile(self):
        print("Save As")

    # close
    def closeWindow(self):
        print("Close window")


    # AUXILIARY FUNCTIONS
    # Retrieves the list of states from the transition table
    def get_afStates(self):
        states = []
        for i in range(self.transition_table.rowCount()):
            states.append(self.transition_table.item(i,2).text())

        return states

    # Update the options list of transition table's combo boxes
    def updateComboBoxes(self):
         states = self.get_afStates()
         states.insert(0, "-")
         for i in range(self.transition_table.rowCount()):
             for j in range(3, self.transition_table.columnCount()):
                 cb = self.transition_table.cellWidget(i, j)
                 selected = cb.currentText()
                 cb.clear()
                 cb.addItems(states)
                 index = cb.findText(selected, QtCore.Qt.MatchExactly)
                 if index != -1:
                    cb.setCurrentIndex(index)
