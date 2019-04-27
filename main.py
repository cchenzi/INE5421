import sys
from UI.src.mainWindow import Ui_MainWindow
from PySide2.QtWidgets import QApplication


# Criacao da aplicacao principal
app = QApplication(sys.argv)

# Instanciacao da classe que define a mainWindow
principal = Ui_MainWindow()
sys.exit(app.exec_())
