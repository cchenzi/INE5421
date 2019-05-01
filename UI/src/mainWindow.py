# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/Design/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets
from UI.src.faWindow import Ui_FAWindow
import fileManipulation
from model import NFA, DFA, RegularGrammar
from regularExpression import RegularExpression


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi()
        self.connectSignals()
        self.show()


    ##########################################################################################
    # QtDesigner auto generated code
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(320, 246)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 0, 181, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.pushButton_fcg = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_fcg.setGeometry(QtCore.QRect(0, 140, 181, 31))
        self.pushButton_fcg.setObjectName("pushButton_fcg")
        self.pushButton_re = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_re.setGeometry(QtCore.QRect(0, 100, 181, 31))
        self.pushButton_re.setObjectName("pushButton_re")
        self.pushButton_rg = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_rg.setGeometry(QtCore.QRect(0, 60, 181, 31))
        self.pushButton_rg.setObjectName("pushButton_rg")
        self.pushButton_fa = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_fa.setGeometry(QtCore.QRect(0, 20, 181, 31))
        self.pushButton_fa.setObjectName("pushButton_fa")
        self.pushButton_pa = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_pa.setGeometry(QtCore.QRect(0, 180, 181, 31))
        self.pushButton_pa.setObjectName("pushButton_pa")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 22))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)
        self.actionLoad = QtWidgets.QAction(self)
        self.actionLoad.setObjectName("actionLoad")
        self.actionAbout = QtWidgets.QAction(self)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionLoad)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    # QtDesigner auto generated code
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_fcg.setText(_translate("MainWindow", "Free-Context Grammar"))
        self.pushButton_re.setText(_translate("MainWindow", "Regular Expression"))
        self.pushButton_rg.setText(_translate("MainWindow", "Regular Grammar"))
        self.pushButton_fa.setText(_translate("MainWindow", "Finite Automaton"))
        self.pushButton_pa.setText(_translate("MainWindow", "Pushdown Automaton"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
    # end of QtDesigner auto-generated code


    ##########################################################################################
    # connect all actions to it's respective signals (ADDED)
    def connectSignals(self):
        self.pushButton_fa.clicked.connect(self.createFAWindow)
        self.pushButton_pa.clicked.connect(self.createPAWindow)
        self.pushButton_re.clicked.connect(self.createREWindow)
        self.pushButton_rg.clicked.connect(lambda state: self.createGrammarWindow("regular"))
        self.pushButton_fcg.clicked.connect(lambda state: self.createGrammarWindow("context-free"))
        self.actionAbout.triggered.connect(self.showAbout)
        self.actionLoad.triggered.connect(self.createFileDialog)


    # SIGNAL FUNCTION HANDLERS
    # Creates a Finite Automaton manipulation window
    def createFAWindow(self):
        self.faWindow = Ui_FAWindow(self)

    # Creates a Pushdown Automaton manipulation window
    def createPAWindow(self):
        print("Pushdown Automaton")

    # Creates a Regular expression manipulation window
    def createREWindow(self):
        print("Regular Expression")

    # Creates a grammar manipulation window
    def createGrammarWindow(self, type):
        print(type)

    # Creates the AboutUs dialog window
    def showAbout(self):
        print("About us")

    # Creates the LoadFile window
    def createFileDialog(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File","./", "DAT Files (*.dat)")
        if fileName:
            self.loadFile(fileName)


    # opens a valid file and redirects it to the right path
    def loadFile(self, filename):
        obj = fileManipulation.read_file(filename)

        if isinstance(obj, NFA) or isinstance(obj, DFA):
            self.faWindow = Ui_FAWindow(self, obj, filename)

        elif isinstance(obj, RegularGrammar):
            print("Regular grammar")

        #elif isinstance(obj, CFGrammar):

        elif isinstance(obj, RegularExpression):
            print("Regular expression")

        else:   # should be unreachable
            print("Deu ruim")
