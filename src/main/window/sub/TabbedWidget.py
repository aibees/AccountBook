from PyQt5.QtWidgets import QTabWidget
from PyQt5 import QtWidgets, QtCore

from window.sub.tabs.AnalyzeDataByCardTab import AnalyzeDataByCardTab
from window.sub.tabs.SearchTab import SearchTab
from window.sub.tabs.MonthlyTrend import MonthlyTrend


class TabbedWidget(QTabWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTabWidget.__init__(self, *args, **kwargs)
        self.setTabBar(TabBar(self))
        self.addTab(SearchTab(), "건별 사용내역 조회")
        self.addTab(AnalyzeDataByCardTab(), "구분 별 지출액 분석")
        self.addTab(MonthlyTrend(), "월별 추이")

        # set Layout
        # self.setTabBar(TabBar(self))
        self.setTabPosition(QTabWidget.West)
        self.setStyleSheet('''
            QTabBar::tab{padding: 3px 20px;}
            QTabBar::tab { height: 150px; border: 1px solid #FFFFFF;}
            QTabBar::tab {background-color: rgb(34, 137, 163);color: white;}

            QTabBar::tab:selected {background-color: rgb(48, 199, 184,);
                color: #000000
            }

            QTabWidget>QWidget>QWidget{background: WHITE;}
            QTabWidget>{background: WHITE;}

            QTabWidget::pane {top: 0px;}
            QTabWidget::tab-bar {right: 0px;}
            QTabBar { background: transparent; }
        ''')


class TabBar(QtWidgets.QTabBar):
    def tabSizeHint(self, index):
        s = QtWidgets.QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt);
            painter.restore()