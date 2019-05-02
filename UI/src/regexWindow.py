# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/Design/regexWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from regularExpression import RegularExpression
import fileManipulation


class Ui_RegexWindow(QtWidgets.QMainWindow):

    # Constructor
    def __init__(self, parent, regex = None, filename = None):
        super(Ui_RegexWindow, self).__init__()
        self.parent = parent
        self.REGEX = regex
        self.filename = filename
        self.saved = True

        self.setupUi()
        self.connectSignals()

        if regex:
            self.regexUpdated = True
            self.regex_entry.setText(regex.description)
        else:
            self.regexUpdated = False

        self.updateWindowTitle()
        self.parent.hide()
        self.show()

    #################################################################################3
    # QtDesigner auto-generated code
    def setupUi(self):
        self.setObjectName("RegexWindow")
        self.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.regex_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.regex_entry.setGeometry(QtCore.QRect(0, 180, 641, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.regex_entry.setFont(font)
        self.regex_entry.setObjectName("regex_entry")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 140, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
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
        self.convert_actionToNFA = QtWidgets.QAction(self)
        self.convert_actionToNFA.setObjectName("convert_actionToNFA")
        self.menuFile.addAction(self.file_actionNew)
        self.menuFile.addAction(self.file_actionOpen)
        self.menuFile.addAction(self.file_actionSave)
        self.menuFile.addAction(self.file_actionSaveAs)
        self.menuFile.addAction(self.file_actionClose)
        self.menuConvert.addAction(self.convert_actionToNFA)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuConvert.menuAction())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, RegexWindow):
        _translate = QtCore.QCoreApplication.translate
        RegexWindow.setWindowTitle(_translate("RegexWindow", "MainWindow"))
        self.label.setText(_translate("RegexWindow", "Edit the regular expression here:"))
        self.menuFile.setTitle(_translate("RegexWindow", "File"))
        self.menuConvert.setTitle(_translate("RegexWindow", "Convert"))
        self.file_actionNew.setText(_translate("RegexWindow", "New"))
        self.file_actionOpen.setText(_translate("RegexWindow", "Open"))
        self.file_actionSave.setText(_translate("RegexWindow", "Save"))
        self.file_actionSaveAs.setText(_translate("RegexWindow", "Save as..."))
        self.file_actionClose.setText(_translate("RegexWindow", "Close"))
        self.convert_actionToNFA.setText(_translate("RegexWindow", "Convert to NFA"))

    #############################################################################################

    # UI GENERAL FUNCTIONS
    # Connects the UI signals to it's respective functions
    def connectSignals(self):
        self.file_actionNew.triggered.connect(self.createNewRegex)
        self.file_actionOpen.triggered.connect(lambda: self.createFileDialog("load"))
        self.file_actionSave.triggered.connect(self.saveRegex)
        self.file_actionSaveAs.triggered.connect(lambda: self.createFileDialog("saveAs"))
        self.file_actionClose.triggered.connect(self.checkClose)
        self.convert_actionToNFA.triggered

        # editing_table cells_change connect
        self.regex_entry.textEdited.connect(self.markRegexModified)


    # Defines the standard behavior when user closes this window
    def closeEvent(self, event):
        if not(self.cleanRegexEntry()):
            event.ignore()
            return

        event.accept()
        self.parent.show()


    # updates the window title based on the file being manipulated and if it's saved or not
    def updateWindowTitle(self):
        if self.filename:
            if self.saved:
                self.setWindowTitle(self.filename + " - RegexWindow")
            else:
                self.setWindowTitle("* " + self.filename + " - RegexWindow")
        else:
            self.setWindowTitle("* new - RegexWindow")


    # marks that the regex was modified
    def markRegexModified(self):
        if self.saved:
            self.regexUpdated = False
            self.saved = False
            self.updateWindowTitle()


    # cleans the regex entry input
    def cleanRegexEntry(self):
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
                self.saveRegex()
            elif confirmation == QtWidgets.QMessageBox.Cancel:
                return False

        self.regex_entry.setText("")

        return True


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
    # FILE ACTION HANDLER FUNCTIONS
    # new
    def createNewRegex(self):
        if not(self.cleanRegexEntry()): return
        self.saved = True
        self.regexUpdated = False
        self.REGEX = None
        self.filename = None
        self.updateWindowTitle()

    # creates a file dialog to open or save files
    def createFileDialog(self, mode):
        if mode == "saveAs":
            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File","./", "DAT Files (*.dat)")
            if fileName:
                if fileName[-4:] != ".dat":
                    fileName += ".dat"

                self.createRegexFile(fileName)

        else:
            if not(self.cleanRegexEntry()): return

            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File","./", "DAT Files (*.dat)")
            if fileName:
                self.loadRegex(fileName)

    # load
    def loadRegex(self, filename):
        obj = fileManipulation.read_file(filename)

        if not(isinstance(obj, RegularExpression)):
            self.createErrorDialog("The selected file doesn't represent a Regular expression!")
            return
            
        self.regex_entry.setText(obj.description)
        self.REGEX = obj
        self.saved = True
        self.regexUpdated = True
        self.filename = filename

        self.updateWindowTitle()

    # save
    def saveRegex(self):
        if not(self.saved):
            if self.filename:
                if self.regexUpdated:
                    fileManipulation.write_file(self.filename, self.REGEX)
                else:
                    fileManipulation.write_file(self.filename, self.getRegex())

                self.saved = True
                self.updateWindowTitle()

            else:
                self.createFileDialog("saveAs")

    # save as
    def createRegexFile(self, filename):
        if self.regexUpdated:
            fileManipulation.write_file(filename, self.REGEX)
        else:
            fileManipulation.write_file(filename, self.getRegex())

        self.saved = True
        self.filename = filename

        self.updateWindowTitle()

    # close
    def checkClose(self):
        if len(self.regex_entry.text()) == 0:
            self.close()
        else:
            self.cleanRegexEntry()

        self.saved = True
        self.regexUpdated = False
        self.filename = False
        self.updateWindowTitle()

    ####################################################################################
    # CONVERT ACTION HANDLER FUNCTIONS


    #####################################################################################
    # REGEX MANIPULATION FUNCTIONS
    # gets the regular expression from the editing table
    def getRegex(self):
        if self.regexUpdated:
            return self.REGEX

        description = self.regex_entry.text()

        self.REGEX = RegularExpression(description)
        self.regexUpdated = True
        return self.REGEX
