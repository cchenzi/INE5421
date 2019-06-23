# -*- coding: utf-8 -*-

# description: "Projeto da disciplina de Linguagens Formais 2019.1"
# authors:
#     "Arthur Mesquita Pickcius",
#     "Francisco Luiz Vicenzi",
#     "Joao Fellipe Uller"
# Copyright 2019

from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QTableWidgetItem


class Ui_ParsingTableWindow(QtWidgets.QMainWindow):
    # constructor
    def __init__(self, parent, table, terminals, nonterminals):
        super(Ui_ParsingTableWindow, self).__init__()
        self.parent = parent
        self.map = dict()

        self.setupUi()

        self.populate_table(table, terminals, nonterminals)
        # adjust table sizes

        self.show()


    ##########################################################################################
    # QtDesigner auto generated code
    def setupUi(self):
        self.setObjectName("ParsingTableWindow")
        self.resize(509, 328)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.parsing_table = QtWidgets.QTableWidget(self.centralwidget)
        self.parsing_table.setGeometry(QtCore.QRect(10, 10, 491, 311))
        self.parsing_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.parsing_table.setDragDropOverwriteMode(False)
        self.parsing_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.parsing_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.parsing_table.setWordWrap(False)
        self.parsing_table.setObjectName("parsing_table")
        self.parsing_table.setColumnCount(0)
        self.parsing_table.setRowCount(0)
        self.parsing_table.horizontalHeader().setVisible(True)
        self.parsing_table.horizontalHeader().setHighlightSections(True)
        self.parsing_table.verticalHeader().setVisible(False)
        self.parsing_table.verticalHeader().setHighlightSections(False)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self, ParsingTableWindow):
        _translate = QtCore.QCoreApplication.translate
        ParsingTableWindow.setWindowTitle(_translate("ParsingTableWindow", "LL(1) Parsing Table"))

    # END OF QT DESIGNER AUTO-GENERATED CODE
    ##########################################################################################

    # populates the table with the given firsts and follows
    def populate_table(self, table, terminals, nonterminals):
        self.parsing_table.insertColumn(0)
        for symbol in terminals:
            index = self.parsing_table.columnCount()
            self.parsing_table.insertColumn(index)
            self.map[symbol] = index

        self.parsing_table.setHorizontalHeaderLabels([""] + terminals + ["$"])

        for key in table.keys():
            row = self.parsing_table.rowCount()
            self.parsing_table.insertRow(row)

            item = QTableWidgetItem(key)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.parsing_table.setItem(row, 0, item)

            for sec_key in table[key].keys():
                column = self.map[sec_key]

                item = QTableWidgetItem(table[key][sec_key])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.parsing_table.setItem(row, column, item)


        self.parsing_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.parsing_table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)


    # adjusts the size of the columns to the content of the table
    def adjustSize(self):
        self.parsing_table.setFixedWidth(self.parsing_table.verticalHeader().width() + self.parsing_table.horizontalHeader().length() + self.parsing_table.frameWidth()*2)
        self.parsing_table.setMinimumSize(280, 240)
        self.setFixedWidth(self.parsing_table.width() + 200)
