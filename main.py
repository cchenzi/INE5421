import sys
from UI.src.mainWindow import Ui_MainWindow
from PySide2.QtWidgets import QApplication
from PySide2 import QtWidgets


# Criacao da aplicacao principal
app = QApplication(sys.argv)

# Instanciacao da classe que define a mainWindow
principal = Ui_MainWindow()
w = QtWidgets.QMainWindow()
principal.setupUi(w)
w.show()
sys.exit(app.exec_())
