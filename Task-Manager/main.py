import sys
from PyQt5.QtWidgets import QApplication
from interface import LoginWindow


# Cria e inicia a janela de login 
app = QApplication(sys.argv)
login_window = LoginWindow()
login_window.show()
sys.exit(app.exec_())

