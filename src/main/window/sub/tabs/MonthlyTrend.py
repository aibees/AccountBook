import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from service.AnalyzeService import getTransitionByCreditCardData


class MonthlyTrend(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.figure = plt.Figure()
        # 캔버스 생성
        self.canvas = FigureCanvas(self.figure)
        self.fig = self.canvas.figure

        # 그래프 1 - 월별/카드 별 사용량 추이
        self.graph1 = self.fig.add_subplot(2, 1, 1)
        #self.drawGraph_1(self.graph1)

        # 그래프 2 - 월별 전체 사용량 추이
        self.graph2 = self.fig.add_subplot(2, 1, 2)
        self.drawGraph_2(self.graph2)

        self.canvas.draw()

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def drawData(self):
        resultData = getTransitionByCreditCardData()
        print(resultData)
        resultData = [
            ['2022/01', 'SAMSUNG', 210120],
            ['2022/02', 'SAMSUNG', 399600],
            ['2022/03', 'SAMSUNG', 220088],
            ['2022/01', 'HANA', 385020],
            ['2022/02', 'HANA', 232260],
            ['2022/03', 'HANA', 224660]
        ]
        # plotDict = {}
        # for data in resultData:
        #     card = data['name']
        #     if card in plotDict:
        #         # 이미 존재
        #         plots = plotDict['card']
        #         plots[0].append(data['ym'])
        #         plots[1].append(data['provamt'])
        #         plotDict[card] = plots
        #     else:
        #         # 새로 생성
        #         plotDict[card] = [[data['ym']], [data['provamt']]]
        #
        return resultData

    ## draw graph 1
    # def drawGraph_1(self, graph):
    #     graph.ticklabel_format(style='plain')
    #
    #     drawData = self.drawData()
    #
    #     for key in drawData:
    #         data = drawData[key]
    #         graph.plot(data[0], data[1], label=key)
    #         for i, v in enumerate(data[0]):
    #             graph.text(v, data[1][i], data[1][i],
    #                        fontsize=9,
    #                        color=('blue' if key == 'SAMSUNG' else 'black'),
    #                        horizontalalignment='center',  # horizontalalignment (left, center, right)
    #                        verticalalignment='bottom')  # verticalalignment (top, center, bottom))
    #
    #     graph.legend(loc='best', ncol=2)
    #     graph.set_title("Usage Transition By Credit Card")

    def drawGraph_2(self, graph):
        graph.ticklabel_format(style='plain')


        graph.legend(loc='best', ncol=2)
        graph.set_title("Usage Transition in All Data")
