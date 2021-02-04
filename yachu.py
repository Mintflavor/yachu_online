# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
from PyQt5.QtGui import *
import random
from yachupkg.MyLabel import *

yachu = '.\\Yachu.ui'


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(yachu, self)
        self.pushButton.clicked.connect(self.rolldice)
        self.tableWidget.cellClicked.connect(self.inputrank)
        self.actionCreate_Game.triggered.connect(self.createServer)
        self.actionJoin_Game.triggered.connect(self.createServer)
        self.dice = [self.label1, self.label2, self.label3, self.label4, self.label5]
        self.ran_num = [0, 0, 0, 0, 0]
        for i in self.dice:
            i.clicked.connect(self.keep)
        self.qp = QPixmap()
        for i in range(0, 5):
                self.qp.load(f'dice{i+1}.png')
                self.dice[i].setPixmap(self.qp)
        self.show()

    def rolldice(self):
        self.qp = QPixmap()
        for i in range(0, 5):
            if self.dice[i].frameShape() == QFrame.NoFrame:
                self.ran_num[i] = random.randrange(1, 7)
                self.qp.load(f'dice{self.ran_num[i]}.png')
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
            print(csDialog.getInputs())

    def joinServer(self):
        jsDialog = InputDialog()
        if jsDialog.exec():
            print(jsDialog.getInputs())

def main():
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()