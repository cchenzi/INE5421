# -*- coding: utf-8 -*-

# description: "Projeto da disciplina de Linguagens Formais 2019.1"
# authors:
#     "Arthur Mesquita Pickcius",
#     "Francisco Luiz Vicenzi",
#     "Joao Fellipe Uller"
# Copyright 2019

from PySide2 import QtCore, QtWidgets


class Ui_MRunWindow(QtWidgets.QWidget):
    # added constructor
    def __init__(self, parent):
        super(Ui_MRunWindow, self).__init__()
        self.parent = parent

        self.setupUi()
        self.connectSignals()

        headers = self.result_table.horizontalHeader()
        headers.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.clearTable()

        self.show()


    ##############################################################################
    # QtDesigner auto-generated code
    def setupUi(self):
        self.setObjectName("MRunWindow")
        self.resize(342, 383)
        self.result_table = QtWidgets.QTableWidget(self)
        self.result_table.setGeometry(QtCore.QRect(10, 10, 321, 311))
        self.result_table.setDragDropOverwriteMode(False)
        self.result_table.setRowCount(0)
        self.result_table.setObjectName("result_table")
        self.result_table.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(1, item)
        self.result_table.verticalHeader().setVisible(False)
        self.result_table.verticalHeader().setHighlightSections(False)
        self.pushButton_run = QtWidgets.QPushButton(self)
        self.pushButton_run.setGeometry(QtCore.QRect(70, 340, 89, 25))
        self.pushButton_run.setObjectName("pushButton_run")
        self.pushButton_clear = QtWidgets.QPushButton(self)
        self.pushButton_clear.setGeometry(QtCore.QRect(180, 340, 89, 25))
        self.pushButton_clear.setObjectName("pushButton_clear")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    # QtDesigner auto-generated code
    def retranslateUi(self, MRunWindow):
        _translate = QtCore.QCoreApplication.translate
        MRunWindow.setWindowTitle(_translate("MRunWindow", "MRunWindow"))
        item = self.result_table.horizontalHeaderItem(0)
        item.setText(_translate("MRunWindow", "Input"))
        item = self.result_table.horizontalHeaderItem(1)
        item.setText(_translate("MRunWindow", "Result"))
        self.pushButton_run.setText(_translate("MRunWindow", "Run Inputs"))
        self.pushButton_clear.setText(_translate("MRunWindow", "Clear"))


    ##############################################################################
    # UI MANIPULATION FUNCTIONS
    # Connect the signals to their respective functions
    def connectSignals(self):
        self.result_table.cellChanged.connect(self.handleCellChanges)
        self.pushButton_run.clicked.connect(self.runInputs)
        self.pushButton_clear.clicked.connect(self.clearTable)


    # handle a cell change to add lines if necessary
    def handleCellChanges(self, i, j):
        if j == 0 and i == self.result_table.rowCount()-1:
            item = self.result_table.item(i, j)
            if item.text() != "":
                self.insertRowTable(i+1)


    # inserts a row on the result table
    def insertRowTable(self, row):
        self.result_table.insertRow(row)
        item = QtWidgets.QTableWidgetItem()
        #item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.result_table.setItem(row, 0, item)
        item = QtWidgets.QTableWidgetItem()
        #item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.result_table.setItem(row, 1, item)


    # Clear the run table
    def clearTable(self):
        rows = self.result_table.rowCount()
        for i in range(rows):
            self.result_table.removeRow(0)
        self.result_table.setRowCount(0)

        self.insertRowTable(0)


    # run the inputs and give their respective results
    def runInputs(self):
        fa = self.parent.FA
        for i in range(self.result_table.rowCount()):
            entry = self.result_table.item(i, 0).text()
            result = fa.is_word_input_valid(entry)
            if result: str = "Accepted"
            else: str = "Rejected"
            self.result_table.item(i, 1).setText(str)
