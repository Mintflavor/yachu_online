# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from PyQt5.QtGui import *
import random
from yachupkg.MyLabel import *
#from yachupkg.server import server

yachu = '.\\Yachu.ui'


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(yachu, self)

        self.pushButton.clicked.connect(self.rolldice)               # 주사위굴리기 버튼
        self.tableWidget.cellClicked.connect(self.inputrank)         # 점수표 클릭 연결

        self.actionCreate_Game.triggered.connect(self.createServer)  # 상단메뉴바의 멀티게임생성 트리거
        self.actionJoin_Game.triggered.connect(self.createServer)    # 상단메뉴바의 멀티게임참가 트리거

        self.dice = [self.label1, self.label2, self.label3, self.label4, self.label5]  # 게임주사위들을 저장한 배열
        self.ran_num = [0, 0, 0, 0, 0]
        for i in self.dice:
            i.clicked.connect(self.keep)

        self.qp = QPixmap()
        for i in range(0, 5):
                self.qp.load(f'./img/dice{i+1}.png')
                self.dice[i].setPixmap(self.qp)

        self.loadingUI()
        self.show()

    def loadingUI(self):
        self.cancelbtn.clicked.connect(self.stopServer)              # 서버로딩창의 취소버튼
        self.loadgif = QMovie(f'./img/loading.gif')
        self.label_loading.setMovie(self.loadgif)
        self.loadgif.start()
        self.frame.setStyleSheet("background-color:white;")
        self.frame.hide()

    def rolldice(self):
        self.qp = QPixmap()
        for i in range(0, 5):
            if self.dice[i].frameShape() == QFrame.NoFrame:
                self.ran_num[i] = random.randrange(1, 7)
                self.qp.load(f'./img/dice{self.ran_num[i]}.png')
                self.dice[i].setPixmap(self.qp)
        self.handrank()

    def keep(self):
        sender = self.sender()
        if sender.frameShape() == QFrame.Box:
            sender.setFrameShape(QFrame.NoFrame)
        else:
            sender.setFrameShape(QFrame.Box)

    def inputrank(self):
        self.tableWidget.setItem(self.tableWidget.currentRow(), self.tableWidget.currentColumn(), QTableWidgetItem('A'))

    def handrank(self):
        total = 0
        for i in self.ran_num:
            total = total + i
        for i in range(0, 15):
            if i in [6, 7]:
                continue
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(total)))

    def createServer(self):
        csDialog = InputDialog()
        if csDialog.exec():
            if csDialog.check is True:
                self.frame.show()

    def joinServer(self):
        jsDialog = InputDialog()
        if jsDialog.exec():
            print(jsDialog.getInputs())

    def stopServer(self):
        self.frame.hide()


def main():
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()