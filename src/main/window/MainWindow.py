import datetime

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QDesktopWidget, QTableWidget, \
    QTableWidgetItem, QDateEdit, QComboBox

from service.CommonService import getComboData_select
from service.SlipSearchService import SearchDataByPeriod
from window.sub.InsertWindow import InsertWindow
from window.sub.TabbedWidget import TabbedWidget

FIXED_WIDTH = 85
FIXED_HEIGHT = 25


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("가계부")
        self.setGeometry(300, 300, 850, 750)  # 창위치x 창위치y 창크기x 창크기y
        self.center()
        self.setWindowIcon(QIcon("icon.png"))
        # self.initUI()
        self.tabbedInitUI()
        self.show()


    def tabbedInitUI(self):
        self.statusBar().showMessage('Ready')
        self.tab = TabbedWidget(self)
        self.tab.resize(845, 740)
        self.tab.move(5, 5)


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())