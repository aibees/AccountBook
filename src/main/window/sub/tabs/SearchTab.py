import datetime

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QDateEdit, QComboBox, QTableWidgetItem, QTableWidget, QDesktopWidget, \
    QLineEdit, QLabel

from service.CommonService import getComboData_select
from service.SlipSearchService import SearchDataByPeriod
from window.sub.InsertWindow import InsertWindow

FIXED_WIDTH = 85
FIXED_HEIGHT = 25


class SearchTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # ================ 가계부 입력버튼 ====================
        insert_btn = QPushButton("가계부 입력하기", self)
        insert_btn.clicked.connect(self.main_open_insertWidget)
        insert_btn.resize(110, 30)
        insert_btn.move(565, 190)

        # ================== FRDATE ========================
        self.frdateEdit = QDateEdit(self)
        self.frdateEdit.setDate(
            datetime.date(year=QDate.currentDate().year(), month=QDate.currentDate().month(), day=1))
        self.frdateEdit.setDisplayFormat('yyyy/MM/dd')
        self.frdateEdit.setFont(QFont("malgun Gothic", 11))
        # self.frdateEdit.setButtonSymbols(QSpinBox.NoButtons)
        self.frdateEdit.move(15, 190)
        self.frdateEdit.setFixedWidth(105)
        self.frdateEdit.setFixedHeight(30)

        # ================== TODATE ========================
        self.todateEdit = QDateEdit(self)
        self.todateEdit.setDate(QDate.currentDate())
        self.todateEdit.setDisplayFormat('yyyy/MM/dd')
        self.todateEdit.setFont(QFont("malgun Gothic", 11))
        self.todateEdit.move(130, 190)
        self.todateEdit.setFixedWidth(105)
        self.todateEdit.setFixedHeight(30)

        # =================== 구분값 =======================
        self.usageCombo = self.getComboValue(QComboBox(self), "USAGE")
        self.usageCombo.move(245, 190)

        # =================== 은행 =======================
        self.bankCombo = self.getComboValue(QComboBox(self), "BANK")
        self.bankCombo.move(345, 190)

        # =================== 결제수단 =======================
        self.wayCombo = self.getComboValue(QComboBox(self), "PAYWAY")
        self.wayCombo.move(445, 190)

        # ==================================================
        self.searchLabel = QLabel("검색어 입력 : ", self)
        self.searchLabel.resize(75, 30)
        self.searchLabel.move(245, 225)

        # ==================== 검색어 =======================
        self.searchText = QLineEdit(self)
        self.searchText.move(345, 225)
        self.searchText.setFont(QFont("malgun Gothic", 11))
        self.searchText.setFixedWidth(185)
        self.searchText.setFixedHeight(30)

        # =================== 검색버튼 =======================
        search_btn = QPushButton("검색", self)
        search_btn.clicked.connect(self.insertToTable)
        search_btn.resize(110, 30)
        search_btn.move(565, 225)

        self.mainTable = QTableWidget(self)
        self.tableHeader = ["날짜", "적요", "입금", "출금", "항목", "결제수단", "은행"]
        self.mainTable.setColumnCount(len(self.tableHeader))
        self.mainTable.setHorizontalHeaderLabels(self.tableHeader)
        self.mainTable.resize(660, 450)
        self.mainTable.move(15, 260)
        self.insertToTable()

    # event def
    def main_open_insertWidget(self):
        sub = InsertWindow()
        sub.show()

    def getComboValue(self, combo, category):
        result = getComboData_select(category)

        for data in result:
            combo.addItem(data['name'], data['code'])

        combo.setMinimumHeight(FIXED_HEIGHT)
        combo.setFixedWidth(FIXED_WIDTH)
        combo.setFixedHeight(FIXED_HEIGHT)
        return combo

    def insertToTable(self):
        paramHeader = ['ymd', 'remark', 'input', 'output', 'usage', 'payway', 'bank']
        param = {
            'frdate': self.frdateEdit.text().replace("/", ""),
            'todate': self.todateEdit.text().replace("/", ""),
            'usage': ('' if self.usageCombo.currentData() == '-1' else self.usageCombo.currentData()),
            'bankcd': ('' if self.bankCombo.currentData() == '-1' else self.bankCombo.currentData()),
            'payway': ('' if self.wayCombo.currentData() == '-1' else self.wayCombo.currentData()),
            'search': '%' + self.searchText.text() + '%'
        }

        resultData = SearchDataByPeriod(param)
        self.mainTable.setRowCount(len(resultData))
        self.mainTable.setColumnCount(len(paramHeader))
        for i in range(len(resultData)):
            for j in range(len(paramHeader)):
                item = QTableWidgetItem(str(resultData[i][paramHeader[j]]))
                if j == 2 or j == 3:
                    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                self.mainTable.setItem(i, j, item)

        self.mainTable.setColumnWidth(0, 70)
        self.mainTable.setColumnWidth(1, 200)
        self.mainTable.setColumnWidth(2, 70)
        self.mainTable.setColumnWidth(3, 80)
        self.mainTable.setColumnWidth(4, 70)
        self.mainTable.setColumnWidth(5, 60)
        self.mainTable.setColumnWidth(6, 60)
