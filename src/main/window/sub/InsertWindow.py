from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime, QDate
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QDialog, QLineEdit, QTimeEdit, QDateEdit, QLabel, QComboBox, QPushButton, QTableWidget, \
    QTableWidgetItem, QHeaderView, QMessageBox, QFileDialog

from service.CommonService import getComboData
from service.SlipSaveService import *

FIXED_WIDTH = 85
FIXED_HEIGHT = 25
FIXED_SPACE = 20
line_1_x = 20
line_1_y = 20
line_2_y = 50

column_header = ['일자', '입출코드', '입출여부', '구분코드', '구분값', '금액', '적요', '은행코드', '은행', '결제코드', '결제수단', '결제시간']


class InsertWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.dateEdit = None
        self.wayCombo = None
        self.timeEdit = None
        self.bankCombo = None
        self.remarkEdit = None
        self.amountEdit = None
        self.usageCombo = None
        self.entryCombo = None
        self.table = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("새로운 입력")
        self.setGeometry(100, 100, 950, 300)

        # ================== 일자 ========================
        dateX = line_1_x + 0 * (FIXED_WIDTH + FIXED_SPACE)
        dateLabel = QLabel("일자", self)
        dateLabel.move(dateX, line_1_y)
        dateLabel.setFixedWidth(FIXED_WIDTH)

        self.dateEdit = QDateEdit(self)
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setDisplayFormat('yyyy/MM/dd')
        self.dateEdit.move(dateX, line_2_y)
        self.dateEdit.setFixedWidth(FIXED_WIDTH)
        self.dateEdit.setFixedHeight(FIXED_HEIGHT)

        # =================== 입출여부 =======================
        entryX = line_1_x + 1 * (FIXED_WIDTH + FIXED_SPACE)
        entryLabel = QLabel("입출여부", self)
        entryLabel.move(entryX, line_1_y)
        entryLabel.setFixedWidth(FIXED_WIDTH)

        self.entryCombo = self.getComboValue(QComboBox(self), "ENTRY")
        self.entryCombo.move(entryX, line_2_y)

        # =================== 구분값 =======================
        usageX = line_1_x + 2 * (FIXED_WIDTH + FIXED_SPACE)
        usageLabel = QLabel("구분값", self)
        usageLabel.move(usageX, line_1_y)
        usageLabel.setFixedWidth(FIXED_WIDTH)

        self.usageCombo = self.getComboValue(QComboBox(self), "USAGE")
        self.usageCombo.move(usageX, line_2_y)

        # =================== 금액 =======================
        amountX = line_1_x + 3 * (FIXED_WIDTH + FIXED_SPACE)
        amountLabel = QLabel("금액", self)
        amountLabel.move(amountX, line_1_y)
        amountLabel.setFixedWidth(FIXED_WIDTH)

        self.amountEdit = QLineEdit(self)
        self.amountEdit.move(amountX, line_2_y)
        self.amountEdit.setValidator(QIntValidator())
        self.amountEdit.setFixedWidth(FIXED_WIDTH)
        self.amountEdit.setFixedHeight(FIXED_HEIGHT)

        # =================== 적요 =======================
        remarkX = line_1_x + 4 * (FIXED_WIDTH + FIXED_SPACE)
        remarkLabel = QLabel("적요", self)
        remarkLabel.move(remarkX, line_1_y)
        remarkLabel.setFixedWidth(FIXED_WIDTH)

        self.remarkEdit = QLineEdit(self)
        self.remarkEdit.move(remarkX, line_2_y)
        self.remarkEdit.setFixedWidth(FIXED_WIDTH)
        self.remarkEdit.setFixedHeight(FIXED_HEIGHT)

        # =================== 은행 =======================
        bankX = line_1_x + 5 * (FIXED_WIDTH + FIXED_SPACE)
        bankLabel = QLabel("은행", self)
        bankLabel.move(bankX, line_1_y)
        bankLabel.setFixedWidth(FIXED_WIDTH)

        self.bankCombo = self.getComboValue(QComboBox(self), "BANK")
        self.bankCombo.move(bankX, line_2_y)

        # =================== 결제수단 =======================
        wayX = line_1_x + 6 * (FIXED_WIDTH + FIXED_SPACE)
        wayLabel = QLabel("결제수단", self)
        wayLabel.move(wayX, line_1_y)
        wayLabel.setFixedWidth(FIXED_WIDTH)

        self.wayCombo = self.getComboValue(QComboBox(self), "PAYWAY")
        self.wayCombo.move(wayX, line_2_y)

        # =================== 결제시간 =======================
        timeX = line_1_x + 7 * (FIXED_WIDTH + FIXED_SPACE)
        timeLabel = QLabel("결제시간", self)
        timeLabel.move(timeX, line_1_y)
        timeLabel.setFixedWidth(FIXED_WIDTH)

        self.timeEdit = QTimeEdit(self)
        self.timeEdit.setTime(QTime.currentTime())
        self.timeEdit.setTimeRange(QTime(0, 00, 00), QTime(23, 59, 59))
        self.timeEdit.setDisplayFormat('hh:mm:ss')
        self.timeEdit.move(timeX, line_2_y)
        self.timeEdit.setFixedWidth(FIXED_WIDTH)
        self.timeEdit.setFixedHeight(FIXED_HEIGHT)

        # =================== 추가버튼 =======================
        addBtn = QPushButton("추  가", self)
        addBtn.move(line_1_x + 8 * (FIXED_WIDTH + FIXED_SPACE), line_1_y)
        addBtn.setFixedWidth(FIXED_WIDTH)
        addBtn.setFixedHeight(FIXED_HEIGHT * 2)
        addBtn.clicked.connect(self.insertDataToTable)

        # =================== 업로드버튼 =======================
        deleteBtn = QPushButton("엑셀 업로드", self)
        deleteBtn.move(line_1_x + 6 * (FIXED_WIDTH + FIXED_SPACE) - 2, line_1_y * 5)
        deleteBtn.setFixedWidth(FIXED_WIDTH)
        deleteBtn.setFixedHeight(FIXED_HEIGHT)
        deleteBtn.clicked.connect(self.uploadDataToTable)

        # =================== 삭제버튼 =======================
        deleteBtn = QPushButton("삭  제", self)
        deleteBtn.move(line_1_x + 7 * (FIXED_WIDTH + FIXED_SPACE) - 8, line_1_y * 5)
        deleteBtn.setFixedWidth(FIXED_WIDTH)
        deleteBtn.setFixedHeight(FIXED_HEIGHT)
        deleteBtn.clicked.connect(self.deleteDataInTable)

        # =================== 저장버튼 =======================
        saveBtn = QPushButton("저  장", self)
        saveBtn.move(line_1_x + 8 * (FIXED_WIDTH + FIXED_SPACE) - 14, line_1_y * 5)
        saveBtn.setFixedWidth(FIXED_WIDTH)
        saveBtn.setFixedHeight(FIXED_HEIGHT)
        saveBtn.clicked.connect(self.saveDataOfTable)

        # 테이블 추가
        self.setTable()

    def setTable(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(len(column_header))
        self.table.move(line_1_x, line_2_y * 2 + FIXED_HEIGHT)
        self.table.setHorizontalHeaderLabels(column_header)
        self.table.setFixedWidth(FIXED_WIDTH * 10 + FIXED_SPACE * 3)
        self.table.setFixedHeight(FIXED_HEIGHT * 6)
        self.table.horizontalHeader().setSectionsClickable(False)
        self.table.setStyleSheet("QHeaderView::section {color:white; background-color: grey}")

        self.table.hideColumn(1)
        self.table.hideColumn(3)
        self.table.hideColumn(7)
        self.table.hideColumn(9)
        self.table.setColumnWidth(0, 90)
        self.table.setColumnWidth(6, 150)
        self.table.setColumnWidth(11, 145)

    def show(self):
        super().exec()

    def getComboValue(self, combo, category):
        result = getComboData(category)

        for data in result:
            combo.addItem(data['name'], data['code'])

        combo.setMinimumHeight(FIXED_HEIGHT)
        combo.setFixedWidth(FIXED_WIDTH)
        combo.setFixedHeight(FIXED_HEIGHT)
        return combo

    def insertDataToTable(self):
        amount = self.amountEdit.text().replace(",", "")
        remark = self.remarkEdit.text()
        if len(amount) == 0:
            self.showMessageBox("금액은 필수값입니다.")
            return

        if len(remark) == 0:
            if self.showConfirmBox("적요가 공란인데, 진행해?") == QMessageBox.No:
                return

        row = [self.dateEdit.text().replace("/", "")
            , self.entryCombo.currentData()
            , self.entryCombo.currentText()
            , self.usageCombo.currentData()
            , self.usageCombo.currentText()
            , amount
            , self.remarkEdit.text()
            , self.bankCombo.currentData()
            , self.bankCombo.currentText()
            , self.wayCombo.currentData()
            , self.wayCombo.currentText(),
               (self.dateEdit.text().replace("/", "-") + "T" + self.timeEdit.text())
               ]

        insertRow = self.table.rowCount()
        self.table.setRowCount(insertRow + 1)
        curCol = 0
        for item in row:
            self.table.setItem(insertRow, curCol, QTableWidgetItem(str(item)))
            curCol += 1

    def uploadDataToTable(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open file', '', 'All Files(*);; Excel Files(*.xlsx)', '')
        result = excelDataParse(fileName[0])

        for row in result:
            insertRow = self.table.rowCount()
            curCol = 0
            self.table.setRowCount(insertRow + 1)
            for item in row:
                self.table.setItem(insertRow, curCol, QTableWidgetItem(str(item)))
                curCol += 1


    def deleteDataInTable(self):
        # print("deleteDataInTable : ", self.table.currentRow())
        self.table.removeRow(self.table.currentRow())

    def saveDataOfTable(self):
        header = ['ymd', 'entry', 'usage', 'amount', 'remark', 'bankcd', 'payway', 'recode', 'seq']
        rows = []
        for r in range(self.table.rowCount()):
            row = {}
            colCnt = 0
            for c in range(len(column_header)):
                if c == 2 or c == 4 or c == 8 or c == 10:
                    continue
                else:
                    row[header[colCnt]] = self.table.item(r, c).text()
                    colCnt += 1
            rows.append(row)
        result = saveInsertData(rows)

        self.showMessageBox(result if result != '000' else '정상적으로 저장되었습니다.')
        if result == '000':
            self.close()
        else:
            self.table.setRowCount(0)

    def showMessageBox(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("메세지")
        msg.setText(text)
        msg.exec_()

    def showConfirmBox(self, msg):
        return QMessageBox.question(self, '안내창', msg, QMessageBox.Yes | QMessageBox.No)
