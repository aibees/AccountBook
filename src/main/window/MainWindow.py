import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QDesktopWidget

from window.function.ClickFunction import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("가계부")
        self.setGeometry(300, 300, 500, 600)  # 창위치x 창위치y 창크기x 창크기y
        self.center()
        self.setWindowIcon(QIcon("icon.png"))
        self.initUI()
        self.show()

    def initUI(self):
        self.statusBar().showMessage('Ready')
        layout = QVBoxLayout()

        # 가계부 입력버튼
        insert_btn = QPushButton("가계부 입력하기", self)
        insert_btn.clicked.connect(self.main_open_insertWidget)
        insert_btn.move(20, 20)

    def main_open_insertWidget(self):
        sub = InsertWindow()
        sub.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())