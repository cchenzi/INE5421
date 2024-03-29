# -*- coding: utf-8 -*-

# description: "Projeto da disciplina de Linguagens Formais 2019.1"
# authors:
#     "Arthur Mesquita Pickcius",
#     "Francisco Luiz Vicenzi",
#     "Joao Fellipe Uller"
# Copyright 2019

from PySide2 import QtCore, QtWidgets, QtGui
from model import RegularGrammar
from cfLang import ContextFreeGrammar
from UI.src.firstFollowWindow import Ui_FirFolWindow
from UI.src.parsingTableWindow import Ui_ParsingTableWindow
import fileManipulation
import re
import copy


class Ui_GrammarWindow(QtWidgets.QMainWindow):

    # Constructor
    def __init__(self, parent, gramm = None, filename = None, type = None):
        super(Ui_GrammarWindow, self).__init__()
        self.parent = parent
        self.filename = filename
        self.GRAMM = gramm
        self.type = type
        self.filenameRE = re.compile('([\w]|/)*\w')  # regular expression to evaluate filenames
        self.runDialog = None
        self.firFolWindow = None
        self.parsingTableWindow = None

        self.setupUi()
        self.connectSignals()

        if gramm:
            self.populateEditor(gramm)
            self.grammUpdated = True
        else:
            self.grammUpdated = False
            self.lockActions()

        if gramm and not filename:
            self.saved = False
        else:
            self.saved = True

        self.updateWindowTitle()

        self.parent.hide()
        self.show()


    ####################################################################################3
    # QtDesigner auto-generated code
    def setupUi(self):
        self.setObjectName("GrammarWindow")
        self.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.editing_table = QtWidgets.QTableWidget(self.centralwidget)
        self.editing_table.setGeometry(QtCore.QRect(10, 20, 621, 431))
        self.editing_table.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.editing_table.setTabKeyNavigation(False)
        self.editing_table.setDragDropOverwriteMode(False)
        self.editing_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.editing_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.editing_table.setWordWrap(False)
        self.editing_table.setRowCount(0)
        self.editing_table.setColumnCount(3)
        self.editing_table.setObjectName("editing_table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.editing_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.editing_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.editing_table.setHorizontalHeaderItem(2, item)

        # CHANGED
        header = self.editing_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.resizeSection(1, 20)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.insertRowEditor()
        # END OF CHANGES

        self.editing_table.horizontalHeader().setVisible(True)
        self.editing_table.horizontalHeader().setHighlightSections(True)
        self.editing_table.verticalHeader().setVisible(False)
        self.editing_table.verticalHeader().setHighlightSections(False)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        self.menuConvert = QtWidgets.QMenu(self.menubar)
        self.menuConvert.setObjectName("menuConvert")
        self.menuInput = QtWidgets.QMenu(self.menubar)
        self.menuInput.setObjectName("menuInput")
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
        self.convert_actionRGToNFA = QtWidgets.QAction(self)
        self.convert_actionRGToNFA.setObjectName("convert_actionRGToNFA")
        self.test_actionTestType = QtWidgets.QAction(self)
        self.test_actionTestType.setObjectName("test_actionTestType")
        self.input_actionSentence_Recogn = QtWidgets.QAction(self)
        self.input_actionSentence_Recogn.setObjectName("input_actionSentence_Recogn")
        self.input_actionBuild_LL1_PT = QtWidgets.QAction(self)
        self.input_actionBuild_LL1_PT.setObjectName("input_actionBuild_LL1_PT")
        self.convert_actionCNF = QtWidgets.QAction(self)
        self.convert_actionCNF.setObjectName("convert_actionCNF")
        self.convert_actionRecursionRem = QtWidgets.QAction(self)
        self.convert_actionRecursionRem.setObjectName("convert_actionRecursionRem")
        self.convert_actionFatoration = QtWidgets.QAction(self)
        self.convert_actionFatoration.setObjectName("convert_actionFatoration")
        self.menuFile.addAction(self.file_actionNew)
        self.menuFile.addAction(self.file_actionOpen)
        self.menuFile.addAction(self.file_actionSave)
        self.menuFile.addAction(self.file_actionSaveAs)
        self.menuFile.addAction(self.file_actionClose)
        self.menuTest.addAction(self.test_actionTestType)
        self.menuConvert.addAction(self.convert_actionRGToNFA)
        self.menuConvert.addAction(self.convert_actionCNF)
        self.menuConvert.addAction(self.convert_actionRecursionRem)
        self.menuConvert.addAction(self.convert_actionFatoration)
        self.menuInput.addAction(self.input_actionSentence_Recogn)
        self.menuInput.addAction(self.input_actionBuild_LL1_PT)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInput.menuAction())
        self.menubar.addAction(self.menuTest.menuAction())
        self.menubar.addAction(self.menuConvert.menuAction())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    # QtDesigner auto-generated code
    def retranslateUi(self, GrammarWindow):
        _translate = QtCore.QCoreApplication.translate
        GrammarWindow.setWindowTitle(_translate("GrammarWindow", "MainWindow"))
        item = self.editing_table.horizontalHeaderItem(0)
        item.setText(_translate("GrammarWindow", "LS"))
        item = self.editing_table.horizontalHeaderItem(2)
        item.setText(_translate("GrammarWindow", "RS"))
        self.editing_table.setSortingEnabled(False)
        self.menuFile.setTitle(_translate("GrammarWindow", "File"))
        self.menuTest.setTitle(_translate("GrammarWindow", "Test"))
        self.menuConvert.setTitle(_translate("GrammarWindow", "Convert"))
        self.menuInput.setTitle(_translate("GrammarWindow", "Input"))
        self.file_actionNew.setText(_translate("GrammarWindow", "New"))
        self.file_actionOpen.setText(_translate("GrammarWindow", "Open"))
        self.file_actionSave.setText(_translate("GrammarWindow", "Save"))
        self.file_actionSaveAs.setText(_translate("GrammarWindow", "Save as..."))
        self.file_actionClose.setText(_translate("GrammarWindow", "Close"))
        self.convert_actionRGToNFA.setText(_translate("GrammarWindow", "Convert Regular Gram. to NFA"))
        self.test_actionTestType.setText(_translate("GrammarWindow", "Test Grammar Type"))
        self.input_actionSentence_Recogn.setText(_translate("GrammarWindow", "Sentence Recognition"))
        self.input_actionBuild_LL1_PT.setText(_translate("GrammarWindow", "Build LL(1) Parse Table"))
        self.convert_actionCNF.setText(_translate("GrammarWindow", "CFG to Chomsky Normal Form"))
        self.convert_actionRecursionRem.setText(_translate("GrammarWindow", "Left Recursion Removal"))
        self.convert_actionFatoration.setText(_translate("GrammarWindow", "Left Fatoration"))

    ##############################################################################################

    # GENERAL UI FUNCTIONS
    # Connects the UI signals to it's respective functions
    def connectSignals(self):
        self.file_actionNew.triggered.connect(self.createNewGramm)
        self.file_actionOpen.triggered.connect(lambda: self.createFileDialog("load"))
        self.file_actionSave.triggered.connect(self.saveGramm)
        self.file_actionSaveAs.triggered.connect(lambda: self.createFileDialog("saveAs"))
        self.file_actionClose.triggered.connect(self.checkClose)
        self.convert_actionRGToNFA.triggered.connect(self.regGrammToNFA)
        self.test_actionTestType.triggered.connect(self.testGrammType)
        self.input_actionSentence_Recogn.triggered.connect(self.createRunInputDialog)
        self.input_actionBuild_LL1_PT.triggered.connect(self.build_LL1_PT)
        self.convert_actionCNF.triggered.connect(self.cnf_conversion)
        self.convert_actionRecursionRem.triggered.connect(self.removeLeftRecursion)
        self.convert_actionFatoration.triggered.connect(self.leftFatoration)

        # editing_table cells_change connect
        self.editing_table.itemChanged.connect(self.handleCellChanges)


    # Populates the editing_table based on the passed grammar
    def populateEditor(self, gramm):
        i = 0
        for head in gramm.nonterminals:
            self.editing_table.item(i, 0).setText(head)
            productionMembers = gramm.productions[head]
            self.editing_table.item(i, 2).setText(self.printProductionMembers(productionMembers))
            i += 1

        self.lockActions()


    # enable the valid actions based on grammar type
    def lockActions(self):
        if self.type == "regular":
            self.convert_actionRGToNFA.setEnabled(True)
        else:
            self.convert_actionRGToNFA.setEnabled(False)

        self.test_actionTestType.setEnabled(False)


    # inserts a new row in editing table
    def insertRowEditor(self):
        row = self.editing_table.rowCount()
        self.editing_table.insertRow(row)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.editing_table.setItem(row, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.editing_table.setItem(row, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.editing_table.setItem(row, 2, item)


    # handles the editing table behavior with inserting new rows
    def handleCellChanges(self, item):
        column = item.column()
        row = item.row()
        try:
            if self.editing_table.item(row, 0).text() == "" and self.editing_table.item(row, 1).text() != "":
                self.editing_table.removeRow(row)
                self.markGrammModified()
                return
        except AttributeError:
            pass

        if column == 2 and self.editing_table.item(row, 0).text() == "":
            self.editing_table.item(row, 2).setText("")
            return

        if self.editing_table.item(row, 0).text() == "":
            return

        if column == 0 and item.text() != "":
            self.editing_table.item(row, 1).setText("->")
        elif column == 1:
            aux = self.editing_table.item(row, 2)
            if aux.text() == "":
                aux.setText("&")
        else:
            if item.text() == "": item.setText("&")
            if row == self.editing_table.rowCount()-1: self.insertRowEditor()

        self.markGrammModified()


    # Defines the standard behavior when user closes this window
    def closeEvent(self, event):
        if not(self.cleanEditingTable()):
            event.ignore()
            return

        if self.runDialog: self.runDialog.close()
        if self.firFolWindow: self.firFolWindow.close()
        if self.parsingTableWindow: self.parsingTableWindow.close()

        event.accept()

        self.parent.childWindows.remove(self)
        if not len(self.parent.childWindows):
            self.parent.show()


    # updates the window title based on the file being manipulated and if it's saved or not
    def updateWindowTitle(self):
        if self.filename:
            if self.saved:
                self.setWindowTitle(self.filename + " - GrammarWindow")
            else:
                self.setWindowTitle("* " + self.filename + " - GrammarWindow")
        else:
            self.setWindowTitle("* new - GrammarWindow")


    # cleans all the data off the editing table
    def cleanEditingTable(self):
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
                self.saveGramm()
            elif confirmation == QtWidgets.QMessageBox.Cancel:
                return False

        for i in range(self.editing_table.rowCount()):
            self.editing_table.removeRow(0)

        self.editing_table.setRowCount(0)
        self.insertRowEditor()

        return True


    # marks that the grammar was modified
    def markGrammModified(self):
        self.grammUpdated = False
        self.saved = False
        self.updateWindowTitle()

    #################################################################################

    # AUXILIARY DIALOGS CREATION
    # creates a simple dialog to present a result for the user
    def createResultDialog(self, result):
        dialog = QtWidgets.QDialog()
        layout = QtWidgets.QVBoxLayout()
        dialog.resize(180, 120)
        label = QtWidgets.QLabel(dialog)
        label.setFixedWidth(120)
        label.setGeometry(QtCore.QRect(50, 30, 67, 17))
        buttonBox = QtWidgets.QDialogButtonBox(dialog)
        buttonBox.setGeometry(QtCore.QRect(40, 70, 81, 25))
        buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        buttonBox.accepted.connect(dialog.close)
        dialog.setWindowTitle("Result")
        label.setText(result)
        label.setWordWrap(True)
        label.adjustSize()
        layout.addWidget(label)
        layout.addWidget(buttonBox)
        dialog.adjustSize()
        dialog.setLayout(layout)
        self.resultForm = dialog
        self.resultForm.show()


    # Creates a simple error dialog
    def createErrorDialog(self, msg):
        dialog = QtWidgets.QDialog()
        dialog.resize(253, 137)
        self.errorLabel = QtWidgets.QLabel(dialog)
        self.errorLabel.setText(msg)
        self.errorDialog = dialog
        self.errorLabel.setWordWrap(True)
        self.errorDialog.show()


    # create runInput dialog
    def createRunInputDialog(self):
        self.getGramm()
        if not(self.GRAMM.start_symbol):
            self.createErrorDialog("You need a valid grammar to run inputs over")
            return

        dialog = QtWidgets.QDialog()
        dialog.resize(253, 137)
        dialog.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        dialog.buttonBox.setGeometry(QtCore.QRect(40, 90, 171, 32))
        dialog.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        dialog.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        dialog.label = QtWidgets.QLabel(dialog)
        dialog.label.setGeometry(QtCore.QRect(100, 20, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        dialog.label.setFont(font)
        dialog.entry_input = QtWidgets.QLineEdit(dialog)
        dialog.entry_input.setGeometry(QtCore.QRect(30, 50, 191, 25))
        dialog.buttonBox.accepted.connect(self.recognizeInput)
        dialog.buttonBox.rejected.connect(dialog.close)
        dialog.setWindowTitle("FastRun_Dialog")
        dialog.label.setText("Input")
        self.runDialog = dialog

        self.runDialog.show()


    ####################################################################################
    # FILE ACTION HANDLER FUNCTIONS
    # new
    def createNewGramm(self):
        self.parent.createGrammarWindow(type=self.type)

    # creates a file dialog to open or save files
    def createFileDialog(self, mode):
        if mode == "saveAs":
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File","./", "DAT Files (*.dat)")
            if filename:
                filename = self.filenameRE.match(filename).group()
                if filename:
                    filename += ".dat"

                    self.createGrammFile(filename)

                else:
                    self.createErrorDialog("Invalid filename!!!")
                    return

        else:
            if not(self.cleanEditingTable()): return

            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File","./", "DAT Files (*.dat)")
            if fileName:
                self.loadGramm(fileName)

    # load
    def loadGramm(self, filename):
        obj = fileManipulation.read_file(filename)
        if isinstance(obj, RegularGrammar):
            self.type = "regular"
        elif isinstance(obj, ContextFreeGrammar):
            self.type = "context-free"
        else:
            self.createErrorDialog("The selected file doesn't represent a grammar!")
            return

        self.populateEditor(obj)
        self.GRAMM = obj
        self.saved = True
        self.grammUpdated = True
        self.filename = filename

        self.updateWindowTitle()

    # save
    def saveGramm(self):
        if not(self.saved):
            if self.filename:
                if self.grammUpdated:
                    fileManipulation.write_file(self.filename, self.GRAMM)
                else:
                    fileManipulation.write_file(self.filename, self.getGramm())

                self.saved = True
                self.updateWindowTitle()

            else:
                self.createFileDialog("saveAs")

    # save as
    def createGrammFile(self, filename):
        if self.grammUpdated:
            fileManipulation.write_file(filename, self.GRAMM)
        else:
            fileManipulation.write_file(filename, self.getGramm())

        self.saved = True
        self.filename = filename

        self.updateWindowTitle()

    # close
    def checkClose(self):
        if self.editing_table.rowCount() == 1:
            self.close()
        else:
            self.cleanEditingTable()

        self.saved = True
        self.grammUpdated = False
        self.filename = False
        self.updateWindowTitle()

    ####################################################################################
    # TEST ACTION HANDLER FUNCTIONS
    # tests the grammar type and shows it for the user
    def testGrammType(self):
        nonterminals = self.get_nonTerminals()
        productions = self.get_productions(nonterminals)
        terminals = self.get_terminals(nonterminals, productions)

        if checkGrammTypeRegular(productions, terminals, nonterminals):
            self.createResultDialog("Regular")
        # elif checkGrammTypeContextFree(productions, terminals, nonterminals):  # IMPLEMENT
        #     self.createResultDialog("Context-Free")
        else:
            self.createResultDialog("Grammar type above Context-Free (Unknown)")


    ####################################################################################
    # CONVERT ACTION HANDLER FUNCTIONS
    # converts a regular grammar to a finite automaton and creates a faWindow to show it
    def regGrammToNFA(self):
        if not self.grammUpdated:
            self.getGramm()

        if not self.GRAMM.start_symbol:
            self.createErrorDialog("You don't have a grammar to be converted!!")
            return

        if not checkGrammTypeRegular(self.GRAMM.productions, self.GRAMM.terminals, self.GRAMM.nonterminals):
            self.createErrorDialog("This grammar isn't regular to be converted into a finite automaton!")
            return

        newFA = self.GRAMM.toNFA()
        self.parent.createFAWindow(newFA)


    # converts a CF Grammar to it's Chomsky Normal Form
    def cnf_conversion(self):
        gramm = self.prepareManipulation()
        if not gramm:
            self.createErrorDialog("You need a valid grammar to run manipulations")
            return

        normalized_gramm = copy.deepcopy(gramm)
        normalized_gramm.to_normal_form()

        self.parent.createGrammarWindow(normalized_gramm)


    # remove left recursion from a context-free grammar
    def removeLeftRecursion(self):
        gramm = self.prepareManipulation()
        if not gramm:
            self.createErrorDialog("You need a valid grammar to run manipulations")
            return

        normalized_gramm = copy.deepcopy(gramm)
        normalized_gramm.remove_left_recursion()

        self.parent.createGrammarWindow(normalized_gramm)


    # left-fatorate the context-free grammar
    def leftFatoration(self):
        gramm = self.prepareManipulation()
        if not gramm:
            self.createErrorDialog("You need a valid grammar to run manipulations")
            return

        normalized_gramm = copy.deepcopy(gramm)
        normalized_gramm.do_left_factoring()

        self.parent.createGrammarWindow(normalized_gramm)


    #####################################################################################
    # INPUT ACTION HANDLER FUNCTIONS
    # return to the user if a given sentence is generated by the actual grammar using a PA simulation
    def recognizeInput(self):
        gramm = self.prepareManipulation()
        if not gramm:
            self.createErrorDialog("You need a valid grammar to run inputs over")
            return

        gramm.remove_left_recursion()

        sentence = self.runDialog.entry_input.text()
        result = gramm.pa_sentence_recognition(sentence)
        if result: str = "Accepted"
        else: str = "Rejected"
        self.createResultDialog(str)


    # build and show for the user the LL(1) parse table generated by the actual grammar
    def build_LL1_PT(self):
        gramm = self.prepareManipulation()
        if not gramm:
            self.createErrorDialog("You need a valid grammar to build a parsing table")
            return

        self.firFolWindow = Ui_FirFolWindow(self, gramm.calc_firsts(), gramm.calc_follows())
        try:
            table = gramm.ll_one_table()
        except:
            self.createErrorDialog("This grammar is not LL(1)")
            return

        self.parsingTableWindow = Ui_ParsingTableWindow(self, table, gramm.terminals, gramm.nonterminals)


    # returns a context-free grammar to be manipulated or None if it doesn't exists
    def prepareManipulation(self):
        if not self.grammUpdated:
            self.getGramm()

        if not self.GRAMM.start_symbol:
            return None

        if isinstance(self.GRAMM, RegularGrammar):
            gramm = ContextFreeGrammar(self.GRAMM.nonterminals, self.GRAMM.terminals, self.GRAMM.productions, self.GRAMM.start_symbol)
        else:
            gramm = self.GRAMM

        return gramm


    ####################################################################################
    # GRAMMAR/UI MANIPULATION FUNCTIONS
    # returns a string that represents a list of a production members
    def printProductionMembers(self, list):
        string = ""
        for i in range(len(list) - 1):
            string += list[i] + " | "

        if len(list) > 0:
            string += list[-1]

        return string


    # get non-terminals list from editing table
    def get_nonTerminals(self):
        if self.grammUpdated:
            return self.GRAMM.nonterminals

        nonterminals = []
        for i in range(self.editing_table.rowCount()):
            item = self.editing_table.item(i, 0)
            if item.text() != "":
                nonterminals.append(item.text())
            else:
                break

        return nonterminals

    # get productions dictionary from editing table
    def get_productions(self, nonterminals = None):
        if self.grammUpdated:
            return self.GRAMM.productions

        if not(nonterminals):
            nonterminals = self.get_nonTerminals()

        productions = {k: [] for k in nonterminals}
        for i in range(len(nonterminals)):
            data = self.editing_table.item(i, 2).text()
            data = data.replace(" ", "")
            data = data.split("|")

            productions[nonterminals[i]] = data

        return productions

    # get terminals list from editing table
    def get_terminals(self, nonterminals = None, productions = None):
        if self.grammUpdated:
            return self.GRAMM.terminals

        if not(nonterminals):
            nonterminals = self.get_nonTerminals()
        if not(productions):
            productions = self.get_productions(nonterminals)

        terminals = []
        for head in nonterminals:
            for escape in productions[head]:
                if escape not in nonterminals:
                    for c in escape:
                        if c not in nonterminals and c not in terminals:
                            terminals.append(c)


        return terminals

    # generates the grammar based on the editing table
    def getGramm(self):
        if self.grammUpdated:
            return self.GRAMM

        nonterminals = self.get_nonTerminals()
        productions = self.get_productions(nonterminals)
        terminals = self.get_terminals(nonterminals, productions)
        if len(nonterminals) > 0:
            start_symbol = nonterminals[0]
        else:
            start_symbol = None

        if self.type == "regular":
            self.GRAMM = RegularGrammar(nonterminals, terminals, productions, start_symbol)
        else:
            self.GRAMM = ContextFreeGrammar(nonterminals, terminals, productions, start_symbol)
        self.grammUpdated = True
        return self.GRAMM


# GRAMMAR TYPE TESTS
# Retorna true se for regular, falso caso contrário
def checkGrammTypeRegular(productions, terminals, nonterminals):
    error = False
    for non, prods in productions.items():
        for x in prods:
            if len(x) > 2:
                error = True
                print(x)
                break
            if len(x) > 1:
                if x[0] not in terminals:
                    error = True
                    print(x)
                    break
                if x[1] not in nonterminals:
                    error = True
                    print(x)
                    break
            else:
                if x not in terminals:
                    error = True
                    print(x)
                    break
    return not error
