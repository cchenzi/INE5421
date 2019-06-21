# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/Design/firstFollowWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QTableWidgetItem


class Ui_FirFolWindow(QtWidgets.QMainWindow):
    # constructor
    def __init__(self, parent, firsts, follows):
        super(Ui_FirFolWindow, self).__init__()
        self.parent = parent

        self.setupUi()

        self.populate_table(firsts, follows)
        # adjust table sizes

        self.show()


    ##########################################################################################
    # QtDesigner auto generated code
    def setupUi(self):
        self.setObjectName("FirFolWindow")
        self.resize(362, 328)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.ff_table = QtWidgets.QTableWidget(self.centralwidget)
        self.ff_table.setGeometry(QtCore.QRect(10, 10, 341, 311))
        self.ff_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ff_table.setDragDropOverwriteMode(False)
        self.ff_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ff_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ff_table.setWordWrap(False)
        self.ff_table.setObjectName("ff_table")
        self.ff_table.setColumnCount(3)
        self.ff_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.ff_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ff_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ff_table.setHorizontalHeaderItem(2, item)
        self.ff_table.horizontalHeader().setVisible(True)
        self.ff_table.horizontalHeader().setHighlightSections(True)
        self.ff_table.verticalHeader().setVisible(False)
        self.ff_table.verticalHeader().setHighlightSections(False)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


    # QtDesigner auto generated code
    def retranslateUi(self, FirFolWindow):
        _translate = QtCore.QCoreApplication.translate
        FirFolWindow.setWindowTitle(_translate("FirFolWindow", "MainWindow"))
        item = self.ff_table.horizontalHeaderItem(1)
        item.setText(_translate("FirFolWindow", "FIRST"))
        item = self.ff_table.horizontalHeaderItem(2)
        item.setText(_translate("FirFolWindow", "FOLLOW"))

    # END OF QT DESIGNER AUTO-GENERATED CODE
    ##########################################################################################

    # populates the table with the given firsts and follows
    def populate_table(self, firsts, follows):
        for key in follows.keys():
            newRow_index = self.ff_table.rowCount()
            self.ff_table.insertRow(newRow_index)

            item = QTableWidgetItem(key)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.ff_table.setItem(newRow_index, 0, item)

            label = "{"
            for item in firsts[key]:
                label = label + item + ", "
            label = label[:-2]
            label += "}"
            self.ff_table.setItem(newRow_index, 1, QTableWidgetItem(label))

            label = "{"
            for item in follows[key]:
                label = label + item + ", "
            label = label[:-2]
            label += "}"
            self.ff_table.setItem(newRow_index, 2, QTableWidgetItem(label))

        self.ff_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.ff_table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)


    # adjusts the size of the columns to the content of the table
    def adjustSize(self):
        self.ff_table.setFixedWidth(self.ff_table.verticalHeader().width() + self.ff_table.horizontalHeader().length() + self.ff_table.frameWidth()*2)
        self.ff_table.setMinimumSize(280, 240)
        self.setFixedWidth(self.ff_table.width() + 200)
