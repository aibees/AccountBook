from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel


class AnalyzeDataByCardTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.MonthEdit = QLabel("3월 목표액", self)
        self.resize(50, 20)
        self.move(5, 5)