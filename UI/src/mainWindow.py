# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/Design/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets
from UI.src.newFADialog import Ui_NewFADialog


class Ui_MainWindow(object):
    # Added constructor (don't change!!!)
    def __init__(self):
        self.window = QtWidgets.QMainWindow()
        self.setupUi(self.window)
        self.connectSignals()
        self.window.show()
    # end of constructor

    ##########################################################################################
    # QtDesigner auto generated code
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 246)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 22))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionLoad)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # QtDesigner auto generated code
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_fcg.setText(_translate("MainWindow", "Free-Context Grammar"))
        self.pushButton_re.setText(_translate("MainWindow", "Regular Expression"))
        self.pushButton_rg.setText(_translate("MainWindow", "Regular Grammar"))
        self.pushButton_fa.setText(_translate("MainWindow", "Finite Automaton"))
        self.pushButton_pa.setText(_translate("MainWindow", "Pushdown Automaton"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
    # end from QtDesigner auto-generated code


    ##########################################################################################
    # connect all actions to it's respective signals (ADDED)
    def connectSignals(self):
        self.pushButton_fa.clicked.connect(self.createNewFADialog)
        self.pushButton_pa.clicked.connect(self.createPAWindow)
        self.pushButton_re.clicked.connect(self.createREWindow)
        self.pushButton_rg.clicked.connect(self.createRGWindow)
        self.pushButton_fcg.clicked.connect(self.createFCGWindow)
        self.actionAbout.triggered.connect(self.showAbout)
        self.actionLoad.triggered.connect(self.createLoadFileWindow)

    # SIGNAL FUNCTION HANDLERS
    # Creates a Finite Automaton manipulation window
    def createNewFADialog(self):
        self.newFaDialog = Ui_NewFADialog()

    # Creates a Pushdown Automaton manipulation window
    def createPAWindow(self):
        print("Pushdown Automaton")

    # Creates a Regular expression manipulation window
    def createREWindow(self):
        print("Regular Expression")

    # Creates a Regular grammar manipulation window
    def createRGWindow(self):
        print("Regular Grammar")

    # Creates a Free-Context Grammar manipulation window
    def createFCGWindow(self):
        print("Free-Context Grammar")

    # Creates the AboutUs dialog window
    def showAbout(self):
        print("About us")

    # Creates the LoadFile window
    def createLoadFileWindow(self):
        self.fileDialog = QtWidgets.QFileDialog()
        self.fileDialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        self.fileDialog.AcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        self.fileDialog.fileSelected.connect(self.loadFile)
        self.fileDialog.setNameFilter("JSON Files (*.json)")
        self.fileDialog.show()


    # opens a valid file and redirects it to the right path
    def loadFile(self, filename):
        print(filename)
        # IMPLEMENT
        # Definir os passos necessarios para abrir e restaurar um arquivo salvo
