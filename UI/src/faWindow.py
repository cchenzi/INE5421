# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/Design/faWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QTableWidgetItem
from UI.src.newNFATransitionDialog import Ui_NFATransitionDialog
from UI.src.newFADialog import Ui_NewFADialog
import fileManipulation
from model import NFA, DFA


class Ui_FAWindow(QtWidgets.QMainWindow):
    # Constructs an empty window until user defines the FA to be edited
    def __init__(self, parent):
        super(Ui_FAWindow, self).__init__()
        self.parent = parent
        self.opened = False

        self.setupUi()
        self.connectSignals()

        self.parent.hide()
        self.show()

    # Constructs the window and the editor based on the FA passed as argument
    def __init__(self, parent, fa, filename):
        super(Ui_FAWindow, self).__init__()
        self.parent = parent

        self.setupUi()
        self.connectSignals()
        self.createEditor(fa)

        self.fileName = filename
        self.saved = True
        self.updateWindowTitle()

        self.parent.hide()
        self.show()


    ##########################################################################################
    # QtDesigner auto generated code
    def setupUi(self):
        self.setObjectName("FAWindow")
        self.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setEnabled(False)
        self.transition_table = QtWidgets.QTableWidget(self.centralwidget)
        self.transition_table.setGeometry(QtCore.QRect(150, 10, 481, 441))
        self.transition_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.transition_table.setDragDropOverwriteMode(False)
        self.transition_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.transition_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.transition_table.setWordWrap(False)
        self.transition_table.setObjectName("transition_table")
        self.transition_table.horizontalHeader().setVisible(True)
        self.transition_table.horizontalHeader().setHighlightSections(True)
        self.transition_table.verticalHeader().setVisible(False)
        self.transition_table.verticalHeader().setHighlightSections(False)
        self.setTransitionTable()
        self.statesMan_container = QtWidgets.QWidget(self.centralwidget)
        self.statesMan_container.setGeometry(QtCore.QRect(19, 50, 111, 121))
        self.statesMan_container.setObjectName("statesMan_container")
        self.label = QtWidgets.QLabel(self.statesMan_container)
        self.label.setGeometry(QtCore.QRect(30, 10, 51, 17))
        self.label.setObjectName("label")
        self.pushButton_insertState = QtWidgets.QPushButton(self.statesMan_container)
        self.pushButton_insertState.setGeometry(QtCore.QRect(10, 40, 89, 25))
        self.pushButton_insertState.setObjectName("pushButton_insertState")
        self.pushButton_removeState = QtWidgets.QPushButton(self.statesMan_container)
        self.pushButton_removeState.setGeometry(QtCore.QRect(10, 80, 89, 25))
        self.pushButton_removeState.setObjectName("pushButton_removeState")
        self.transMan_container = QtWidgets.QWidget(self.centralwidget)
        self.transMan_container.setGeometry(QtCore.QRect(20, 200, 111, 121))
        self.transMan_container.setObjectName("transMan_container")
        self.pushButton_removeTransition = QtWidgets.QPushButton(self.transMan_container)
        self.pushButton_removeTransition.setGeometry(QtCore.QRect(10, 80, 89, 25))
        self.pushButton_removeTransition.setObjectName("pushButton_removeTransition")
        self.label_2 = QtWidgets.QLabel(self.transMan_container)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 81, 17))
        self.label_2.setObjectName("label_2")
        self.pushButton_insertTransition = QtWidgets.QPushButton(self.transMan_container)
        self.pushButton_insertTransition.setGeometry(QtCore.QRect(10, 40, 89, 25))
        self.pushButton_insertTransition.setObjectName("pushButton_insertTransition")
        self.transMan_container.raise_()
        self.statesMan_container.raise_()
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuInput = QtWidgets.QMenu(self.menubar)
        self.menuInput.setObjectName("menuInput")
        self.menuConvert = QtWidgets.QMenu(self.menubar)
        self.menuConvert.setObjectName("menuConvert")
        self.setMenuBar(self.menubar)
        self.file_actionNew = QtWidgets.QAction(self)
        self.file_actionNew.setObjectName("file_actionNew")
        self.file_actionOpen = QtWidgets.QAction(self)
        self.file_actionOpen.setObjectName("file_actionOpen")
        self.file_actionSave = QtWidgets.QAction(self)
        self.file_actionSave.setObjectName("file_actionSave")
        self.file_actionSaveAs = QtWidgets.QAction(self)
        self.file_actionSaveAs.setObjectName("file_actionSaveAs")
        self.file_actionClose = QtWidgets.QAction(self)
        self.file_actionClose.setObjectName("file_actionClose")
        self.convert_actionToDFA = QtWidgets.QAction(self)
        self.convert_actionToDFA.setObjectName("convert_actionToDFA")
        self.convert_actionToGramm = QtWidgets.QAction(self)
        self.convert_actionToGramm.setObjectName("convert_actionToGramm")
        self.input_actionFastRun = QtWidgets.QAction(self)
        self.input_actionFastRun.setObjectName("input_actionFastRun")
        self.input_actionStep = QtWidgets.QAction(self)
        self.input_actionStep.setObjectName("input_actionStep")
        self.input_actionMultipleRun = QtWidgets.QAction(self)
        self.input_actionMultipleRun.setObjectName("input_actionMultipleRun")
        self.menuFile.addAction(self.file_actionNew)
        self.menuFile.addAction(self.file_actionOpen)
        self.menuFile.addAction(self.file_actionSave)
        self.menuFile.addAction(self.file_actionSaveAs)
        self.menuFile.addAction(self.file_actionClose)
        self.menuInput.addAction(self.input_actionFastRun)
        self.menuInput.addAction(self.input_actionStep)
        self.menuInput.addAction(self.input_actionMultipleRun)
        self.menuConvert.addAction(self.convert_actionToDFA)
        self.menuConvert.addAction(self.convert_actionToGramm)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInput.menuAction())
        self.menubar.addAction(self.menuConvert.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    # QtDesigner auto generated code
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("FAWindow", "MainWindow"))
        self.label.setText(_translate("FAWindow", "States"))
        self.pushButton_insertState.setText(_translate("FAWindow", "Insert"))
        self.pushButton_removeState.setText(_translate("FAWindow", "Remove"))
        self.pushButton_removeTransition.setText(_translate("FAWindow", "Remove"))
        self.label_2.setText(_translate("FAWindow", "Transitions"))
        self.pushButton_insertTransition.setText(_translate("FAWindow", "Insert"))
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
        self.input_actionFastRun.setText(_translate("FAWindow", "Fast Run"))
        self.input_actionStep.setText(_translate("FAWindow", "Step by State..."))
        self.input_actionMultipleRun.setText(_translate("FAWindow", "Multiple Run"))


    ######################## GENERAL WINDOW MANIPULATION FUNCTIONS ###########################
    # Connect signals with their respective actions
    def connectSignals(self):
        self.pushButton_insertState.clicked.connect(self.createInsertStateDialog)
        self.pushButton_removeState.clicked.connect(self.removeState)
        self.file_actionNew.triggered.connect(self.createNewFA)
        self.file_actionOpen.triggered.connect(lambda: self.createFileDialog("open"))
        self.file_actionSave.triggered.connect(self.saveFA)
        self.file_actionSaveAs.triggered.connect(lambda: self.createFileDialog("saveAs"))
        self.file_actionClose.triggered.connect(self.closeEditor)
        self.convert_actionToDFA.triggered.connect(self.convertToDFA)
        self.convert_actionToGramm.triggered.connect(self.convertToGrammar)
        self.input_actionFastRun.triggered
        self.input_actionStep.triggered
        self.input_actionMultipleRun.triggered
        self.pushButton_insertTransition.clicked.connect(self.createInsertTransitionDialog)
        self.pushButton_removeTransition.clicked.connect(self.createRemoveTransitionDialog)


    # initializes the editor based on the entry automaton
    def createEditor(self, obj):
        self.newStateDialog = None
        self.fileName = None
        self.saved = False
        self.opened = True

        self.updateWindowTitle()

        self.setTransitionTable()

        self.nfa = isinstance(obj, NFA)
        if self.nfa:
            self.epsilonEnabled = obj.epsilonEnabled
        else:
            self.epsilonEnabled = False

        self.alphabet = obj.alphabet

        self.initialState_radioGroup = QtWidgets.QButtonGroup()
        self.finalStates_checkGroup = QtWidgets.QButtonGroup()
        self.finalStates_checkGroup.setExclusive(False)
        self.transition_table.insertColumn(0)
        self.transition_table.insertColumn(1)
        self.transition_table.insertColumn(2)

        for i in range(len(self.alphabet)):
            self.transition_table.insertColumn(i+3)

        if self.epsilonEnabled:
            self.transition_table.insertColumn(self.transition_table.columnCount())
            self.transition_table.setHorizontalHeaderLabels(["->", "*", "State"] + self.alphabet + ["&"])
        else:
            self.transition_table.setHorizontalHeaderLabels(["->", "*", "State"] + self.alphabet)

        self.transition_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.transition_table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)
        self.transMan_container.setEnabled(self.nfa)

        # insert the obj states on the transition table
        for s in obj.states:
            self.insertState(s)

        # sets the final states
        for s in obj.final_states:
            self.finalStates_checkGroup.button(obj.states.index(s)).setChecked(True)

        # mark the initial state if there's one
        if obj.init_state != '':
            self.initialState_radioGroup.button(obj.states.index(obj.init_state)).setChecked(True)

        # insert the transitions
        if self.nfa:
            for i in range(len(obj.states)):
                for j in range(len(obj.alphabet)):
                    self.transition_table.item(i, j+3).setText(self.setToString(obj.transitions[obj.states[i]][obj.alphabet[j]]))

        else:
            for i in range(len(obj.states)):
                for j in range(len(obj.alphabet)):
                    destination = obj.transitions[obj.states[i]][obj.alphabet[j]]
                    if destination != "-":
                        self.transition_table.cellWidget(i, j+3).setCurrentIndex(obj.states.index(destination) + 1)  # Fator de correcao do primeiro elemento do comboBox

        self.centralwidget.setEnabled(True)
    # end of createEditor


    # sets the transition table to be used
    def setTransitionTable(self):
        self.transition_table.setColumnCount(0)
        self.transition_table.setRowCount(0)
        self.transition_table.raise_()
        self.transition_table.setVisible(True)


    # Defines the standard behavior when user closes this window
    def closeEvent(self, event):
        if self.opened:
            if not(self.closeEditor()):
                event.ignore()
                return

        event.accept()
        self.parent.show()


    # updates the window title based on the file being manipulated and if it's saved or not
    def updateWindowTitle(self):
        if self.opened:
            if self.fileName:
                if self.saved:
                    self.setWindowTitle(self.fileName + " - FAWindow")
                else:
                    self.setWindowTitle("* " + self.fileName + " - FAWindow")
            else:
                self.setWindowTitle("* new - FAWindow")
        else:
            self.setWindowTitle("FAWindow")

    ##########################################################################################
    # TRANSITION TABLE MANIPULATION FUNCTIONS
    # Creates a dialog to the user insert a new state label
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

        self.buttonBox.accepted.connect(lambda: self.insertState(self.stateLabel_input.text()))
        self.buttonBox.rejected.connect(dialog.close)
        self.newStateDialog = dialog
        self.newStateDialog.show()

    # creates a dialog to insert a new transition on NFAs (code in another file due to it's complexity)
    def createInsertTransitionDialog(self):
        states = self.get_faStates()
        if len(states) == 0:
            self.createErrorDialog("You don't have states to create a transition!")
            return

        self.newTransitionDialog = Ui_NFATransitionDialog(self.insertTransition, states, self.alphabet)


    # Creates a dialog to remove an existing transition from a NFA
    def createRemoveTransitionDialog(self):
        dialog = QtWidgets.QDialog()
        dialog.resize(236, 149)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 100, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 191, 17))
        self.comboBox = QtWidgets.QComboBox(dialog)
        self.comboBox.setGeometry(QtCore.QRect(40, 50, 161, 25))
        self.buttonBox.accepted.connect(self.removeTransition)
        self.buttonBox.rejected.connect(dialog.close)
        self.label_2.setText("Select an existing transition")

        selected = self.transition_table.selectedItems()
        if len(selected) == 0:
            self.createErrorDialog("Select the source state of the transition to be removed")
            return

        row = selected[0].row()
        state = self.transition_table.item(row, 2).text()

        for i in range(len(self.alphabet)):
            conj = self.getTransitionSet(row, i)
            input = self.alphabet[i]

            for t in conj:
                if t != "":
                    self.comboBox.addItem("(" + state + ", " + input + ") -> " + t)

        if self.comboBox.count() == 0:
            self.createErrorDialog("This state doesn't have existing transitions to remove!!")
            return

        self.dialog = dialog
        self.dialog.show()


    # Creates a simple error dialog
    def createErrorDialog(self, msg):
        dialog = QtWidgets.QDialog()
        dialog.resize(253, 137)
        self.errorLabel = QtWidgets.QLabel(dialog)
        self.errorLabel.setText(msg)
        self.errorDialog = dialog
        self.errorLabel.setWordWrap(True)
        self.errorDialog.show()


    ####################################################################################
    # Insert a new state on the transition table
    def insertState(self, label):
        if label in self.get_faStates():
            self.createErrorDialog("This state already exists!!")
            return

        new_index = self.transition_table.rowCount()
        self.transition_table.insertRow(new_index)

        radio = QtWidgets.QRadioButton()
        self.initialState_radioGroup.addButton(radio, new_index)
        self.transition_table.setCellWidget(new_index, 0, radio)

        checkBox = QtWidgets.QCheckBox()
        self.finalStates_checkGroup.addButton(checkBox, new_index)
        self.transition_table.setCellWidget(new_index, 1, checkBox)

        item = QTableWidgetItem(label)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.transition_table.setItem(new_index, 2, item)

        if (self.nfa):
            for i in range(3, self.transition_table.columnCount()):
                item = QTableWidgetItem("{}")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.transition_table.setItem(new_index, i, item)
        else:
            for i in range(3, self.transition_table.columnCount()):
                combo = QtWidgets.QComboBox()
                self.transition_table.setCellWidget(new_index, i, combo)

            self.updateComboBoxes()

        if self.newStateDialog:
            self.newStateDialog.close()
            self.newStateDialog = None

        if self.saved:
            self.saved = False
            self.updateWindowTitle()

    # end of insertState


    # Remove the selected state from the transition table
    def removeState(self):
        selected = self.transition_table.selectedItems()
        if len(selected) == 0:
            self.createErrorDialog("Select the state to be removed!!")
            return

        row = selected[0].row()
        state = self.transition_table.item(row, 2).text()
        self.transition_table.removeRow(row)

        if self.nfa:
            self.updateTransitionSets(state)
        else:
            self.updateComboBoxes()

        if self.saved:
            self.saved = False
            self.updateWindowTitle()


    # Insert a new transition in a Non-deterministic FA
    def insertTransition(self):
        dialog = self.newTransitionDialog
        source = dialog.comboBox_Src.currentIndex()
        destination = dialog.comboBox_Dst.currentText()
        char = dialog.comboBox_Input.currentIndex()

        item = self.transition_table.item(source, char+3)
        conj = self.getTransitionSet(source, char)
        conj.add(destination)
        data = self.setToString(conj)
        item.setText(data)

        if self.saved:
            self.saved = False
            self.updateWindowTitle()
        self.newTransitionDialog.close()


    # Remove the selected transition from a Non-deterministic FA
    def removeTransition(self):
        i = self.transition_table.selectedItems()[0].row()
        transition = self.comboBox.currentText().split(" -> ")
        element = transition[1]
        j = self.alphabet.index((transition[0].split(", "))[1][-2])

        conj = self.getTransitionSet(i, j)
        conj.remove(element)
        data = self.setToString(conj)
        self.transition_table.item(i, j+3).setText(data)

        if self.saved:
            self.saved = False
            self.updateWindowTitle()
        self.dialog.close()


    ####################################################################################
    # CONVERT ACTION HANDLERS
    # convert to dfa
    def convertToDFA(self):
        print("Determinize")

    # convert to grammar
    def convertToGrammar(self):
        print("to Grammar")


    ####################################################################################
    # FILE ACTION HANDLER FUNCTIONS
    # new
    def createNewFA(self):
        self.newFADialog = Ui_NewFADialog(self)

    # creates a file dialog to open or save files
    def createFileDialog(self, mode):
        if mode == "saveAs":
            if not(self.opened):
                self.createErrorDialog("You are not manipulating a file to save it.")
                return

            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File","./", "DAT Files (*.dat)")
            if fileName:
                if fileName[-4:] != ".dat":
                    fileName += ".dat"

                self.createFAFile(fileName)

        else:
            if self.opened and not(self.closeEditor()): return

            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File","./", "DAT Files (*.dat)")
            if fileName:
                self.loadFA(fileName)

    # load
    def loadFA(self, fileName):
        obj = fileManipulation.read_file(fileName)
        self.createEditor(obj)
        self.saved = True
        self.fileName = fileName

        self.updateWindowTitle()

    # save
    def saveFA(self):
        if not(self.opened):
            self.createErrorDialog("You are not manipulating a file to save it.")
            return

        if not(self.saved):
            if self.fileName:
                fileManipulation.write_file(self.fileName, self.getFA())
                self.saved = True
                self.updateWindowTitle()

            else:
                self.createFileDialog("saveAs")


    # save as
    def createFAFile(self, fileName):
        fileManipulation.write_file(fileName, self.getFA())
        self.saved = True
        self.fileName = fileName

        self.updateWindowTitle()

    # close editor
    def closeEditor(self):
        if self.opened:
            if not(self.saved):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("If you leave now you will lose all unsaved changes! Do you want to save them?")
                msg.setWindowTitle("Warning!")
                msg.setStandardButtons(QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Save )
                msg.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                msg.setDefaultButton(QtWidgets.QMessageBox.Save)
                self.confirmQuitMessage = msg
                confirmation = self.confirmQuitMessage.exec_()

                if confirmation == QtWidgets.QMessageBox.Save:
                    self.saveFA()
                elif confirmation == QtWidgets.QMessageBox.Cancel:
                    return False

            self.opened = False
            self.cleanTransitionTable()

            self.updateWindowTitle()
            return True

        else:
            self.close()  # closes the window
            return True


    # cleans all the data off the transition table
    def cleanTransitionTable(self):
        for i in range(self.transition_table.columnCount()):
            self.transition_table.removeColumn(0)
        self.setTransitionTable()
        self.centralwidget.setEnabled(False)


    ####################################################################################
    # INPUT ACTION HANDLERS
    # Creates a dialog to execute a single fast run
    def createFastRunDialog(self):
        print("Fast run")

    # Creates a dialog to execute a single fast run
    def createMultipleRunWindow(self):
        print("Multiple run")

    # Creates a dialog to execute a single fast run
    def createStepByRunWindow(self):
        print("Step by step run")


    ####################################################################################
    # AUXILIARY FUNCTIONS
    # Retrieves the list of states from the transition table
    def get_faStates(self):
        states = []
        for i in range(self.transition_table.rowCount()):
            states.append(self.transition_table.item(i,2).text())

        return states

    # Update the options list of transition table's combo boxes
    def updateComboBoxes(self):
         states = self.get_faStates()
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


    # updates the transition sets from the transition table, deleting the removed state
    def updateTransitionSets(self, removeState):
        for i in range(self.transition_table.rowCount()):
            for j in range(len(self.alphabet)):
                conj = self.getTransitionSet(i, j)
                conj.discard(removeState)
                self.transition_table.item(i, j+3).setText(self.setToString(conj))


    # return a string that represents the content of a set
    def setToString(self, set):
        string = "{"
        remove = False
        for a in set:
            if a != "":
                string += a + ","
                remove = True

        if remove: string = string[:-1]
        string += "}"

        return string

    # return a set that contains all transitions from a given state and a given input
    def getTransitionSet(self, stateIndex, alphabetIndex):
        item = self.transition_table.item(stateIndex, alphabetIndex+3)
        data = (item.text())[1:-1]
        if (not data == "-"):
            return set(data.split(","))

        return set()


    # return a Finite Automaton object from the editor
    def getFA(self):
        states = self.get_faStates()
        alphabet = self.alphabet

        # Get the initial state if there's one defined as
        index = 0
        checked = False
        for b in self.initialState_radioGroup.buttons():
            if b.isChecked():
                checked = True
                break

            index += 1

        if checked:
            init_state = states[index]
        else:
            init_state = ""

        # Get the list of final states if there are any defined as
        final_states = []
        i = 0
        for b in self.finalStates_checkGroup.buttons():
            if b.isChecked():
                final_states.append(states[i])
            i+=1

        # Get the dictionary of transitions
        transitions = {k: {} for k in states}

        if self.nfa:
            for i in range(len(states)):
                aux = {}
                for j in range(len(alphabet)):
                    aux[alphabet[j]] = self.getTransitionSet(i, j)

                transitions[states[i]] = aux

            return NFA(states, alphabet, init_state, final_states, transitions, self.epsilonEnabled)

        else:
            for i in range(len(states)):
                aux = {}
                for j in range(len(alphabet)):
                    aux[alphabet[j]] = self.transition_table.cellWidget(i, j+3).currentText()

                transitions[states[i]] = aux

            return DFA(states, alphabet, init_state, final_states, transitions)

        #end if
    # end of getFA
