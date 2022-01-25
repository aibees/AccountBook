import sys

from PyQt5.QtWidgets import *
from window.MainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    app.exec_()
