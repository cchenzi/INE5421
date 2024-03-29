# -*- coding: utf-8 -*-

# description: "Projeto da disciplina de Linguagens Formais 2019.1"
# authors:
#     "Arthur Mesquita Pickcius",
#     "Francisco Luiz Vicenzi",
#     "Joao Fellipe Uller"
# Copyright 2019

from PySide2 import QtCore, QtWidgets
from UI.src.faWindow import Ui_FAWindow
from UI.src.grammarWindow import Ui_GrammarWindow
from UI.src.regexWindow import Ui_RegexWindow
import fileManipulation
from model import NFA, DFA, RegularGrammar, RegularExpression
from cfLang import ContextFreeGrammar


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi()
        self.connectSignals()
        self.childWindows = []
        self.show()


    ##########################################################################################
    # QtDesigner auto generated code
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(320, 216)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 0, 181, 171))
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
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
    # end of QtDesigner auto-generated code


    ##########################################################################################
    # connect all actions to it's respective signals (ADDED)
    def connectSignals(self):
        self.pushButton_fa.clicked.connect(self.createFAWindow)
        self.pushButton_re.clicked.connect(self.createREWindow)
        self.pushButton_rg.clicked.connect(lambda: self.createGrammarWindow(type='regular'))
        self.pushButton_fcg.clicked.connect(lambda: self.createGrammarWindow(type='context-free'))
        self.actionAbout.triggered.connect(self.showAbout)
        self.actionLoad.triggered.connect(self.createFileDialog)


    # SIGNAL FUNCTION HANDLERS
    # Creates a Finite Automaton manipulation window
    def createFAWindow(self, fa = None, filename = None):
        self.childWindows.append(Ui_FAWindow(self, fa, filename))

    # Creates a Regular expression manipulation window
    def createREWindow(self, regex = None, filename = None):
        self.childWindows.append(Ui_RegexWindow(self, regex, filename))

    # Creates a grammar manipulation window
    def createGrammarWindow(self, gramm = None, filename = None, type = None):
        self.childWindows.append(Ui_GrammarWindow(self, gramm, filename, type))

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
            self.createFAWindow(obj, filename)

        elif isinstance(obj, RegularGrammar):
            self.createGrammarWindow(obj, filename, type='regular')

        elif isinstance(obj, ContextFreeGrammar):
            self.createGrammarWindow(obj, filename, type='context-free')

        elif isinstance(obj, RegularExpression):
            self.createREWindow(obj, filename)

        else:   # should be unreachable
            print("Deu ruim")
