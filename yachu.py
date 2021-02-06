# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from PyQt5.QtGui import *
import random
from yachupkg.MyLabel import *
from yachupkg.Player import *
# from yachupkg.server import server

yachu = '.\\Yachu.ui'


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(yachu, self)

        self.pushButton.clicked.connect(self.rolldice)               # 주사위굴리기 버튼

        self.actionCreate_Game.triggered.connect(self.createServer)  # 상단메뉴바의 멀티게임생성 트리거
        self.actionJoin_Game.triggered.connect(self.joinServer)    # 상단메뉴바의 멀티게임참가 트리거

        self.gamestart()
        self.show()

    def gamestart(self):
        self.tableWidget.cellClicked.connect(self.turnEnd)  # 점수표 클릭 연결
        self.dice = [self.label1, self.label2, self.label3, self.label4, self.label5]  # 게임주사위들을 저장한 배열
        self.turncheck = 3                                   # Turn 의 Roll Dice 횟수를 위한 변수
        self.tempclick =[]                                    # 선택불가능한 셀 판별을 위한 리스트
        self.ran_num = [0, 0, 0, 0, 0]
        for i in self.dice:
            i.clicked.connect(self.keep)

        self.qp = QPixmap()
        for i in range(0, 5):
                self.qp.load(f'./img/dice{i+1}.png')
                self.dice[i].setPixmap(self.qp)

        self.PlayerStatus = Player()        # 플레이어 객체 생성
        self.loadingUI()

    def loadingUI(self):
        self.cancelbtn.clicked.connect(self.stopServer)              # 서버로딩창의 취소버튼
        self.loadgif = QMovie(f'./img/loading.gif')
        self.label_loading.setMovie(self.loadgif)
        self.frame.setStyleSheet("background-color:white;")
        self.frame.hide()

    def rolldice(self):
        self.qp = QPixmap()
        for i in range(0, 5):
            if self.dice[i].frameShape() == 0:
                self.ran_num[i] = random.randrange(1, 7)
                self.qp.load(f'./img/dice{self.ran_num[i]}.png')
                self.dice[i].setPixmap(self.qp)
        if self.checkTurn():
            self.pushButton.setText("Input Score!")
            self.pushButton.setDisabled(True)
        else:
            self.pushButton.setText("Roll Dice! (" + str(self.turncheck) + ")")
        self.printhandrank()

    def turnEnd(self):
        if self.inputrank():
            self.checkgameend()
            for i in self.dice:
                i.setFrameShape(QFrame.NoFrame)
            self.pushButton.setEnabled(True)
            self.pushButton.setText("Roll Dice!")
            self.turncheck = 3

    def checkTurn(self):
        if self.turncheck-1 is 0:
            return True
        else:
            self.turncheck -= 1
            return False

    def checkgameend(self):
        if all([self.tableWidget.item(i, 1).background() == QColor(232,245,171,96) for i in range(0, 6)]):
            if sum(self.PlayerStatus.myscore[0:6]) > 63:
                self.PlayerStatus.myscore.append(35)
            if all([self.tableWidget.item(i, 1).background() == QColor(232,245,171,96) for i in range(8, 15)]):
                self.tableWidget.setItem(15, 1, QTableWidgetItem(str(sum(self.PlayerStatus.myscore))))


    def keep(self):
        sender = self.sender()
        if sender.frameShape() == QFrame.Box:
            sender.setFrameShape(QFrame.NoFrame)
        else:
            sender.setFrameShape(QFrame.Box)

    def inputrank(self):
        try:
            row, column = self.tableWidget.currentRow(), self.tableWidget.currentColumn()
            if self.tempclick == [row, column] or self.turncheck == 3 \
                    or self.tableWidget.item(row, column).background() == QColor(232,245,171,96):
                raise NoClickError
            self.tempclick = [row, column]
            index = row
            if row > 6:
                index = row-2
            self.PlayerStatus.myscore[index] = self.PlayerStatus.handrank[index]
            if self.PlayerStatus.myscore[index] == -1:
                self.PlayerStatus.myscore[index] = 0
                self.tableWidget.setItem(row, column, QTableWidgetItem("0"))
            self.tableWidget.item(row, column).setBackground(QColor(232,245,171,96))
            self.tableWidget.item(row, column).selectable = False
            return True
        except Exception as e:
            print(e)
            return False

    def printhandrank(self):
        self.PlayerStatus.checkHandrank(self.ran_num)
        index = 0
        for i in range(0, 15):
            if i in [6, 7]:
                continue
            currentscore = self.PlayerStatus.handrank[index]
            if self.PlayerStatus.myscore[index] is -1:
                if currentscore is not -1 and currentscore is not 0:
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(currentscore)))
                else:
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(""))
            index += 1

    def gameend(self):
        self.tableWidget.setItem(15, 1, QTableWidgetItem(str(self.PlayerStatus.gameend())))

    def createServer(self):
        csDialog = InputDialog()
        if csDialog.exec():
            if csDialog.check is True:
                self.loadgif.start()
                self.frame.show()

    def joinServer(self):
        jsDialog = InputDialog()
        if jsDialog.exec():
            self.loadgif.start()
            self.frame.show()

    def stopServer(self):
        self.loadgif.stop()
        self.frame.hide()


def main():
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()