class Player:
    def __init__(self):
        self.myscore = [-1 for i in range(0, 13)]           # 실제 점수를 저장하는 배열
        self.handrank = [-1 for i in range(0, 13)]          # Roll Dice 시마다 변하는 점수를 저장하는 배열
        self.stlist = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}, {1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}]

# self.handrank index
# 0 = ONE / 1 = TWO / 2 = THREE / 3 = FOUR / 4 = FIVE / 5 = SIX
# 6 = 3ofKIND / 7 = 4ofKIND / 8 = FULLHOUSE / 9 = S.STRAIGHT / 10 = L.STRAIGHT
# 11 = CHANCE / 12 = YACHU
# self.myscore index <- 게임이 끝난후 append 로 추가함
# 13 = BONUS
    def checkHandrank(self, ran_num):
        self.handrank = self.myscore.copy()         # 호출시마다 현재 저장된 점수로 초기화
        checkcount = [0, 0, 0, 0, 0, 0]
        for i in range(0, 6):                       # 1~6까지 검사
            checkcount[i] = ran_num.count(i+1)
            total = sum(ran_num)
            self.handrank[i] = checkcount[i]*(i+1)
            self.handrank[11] = total
            if checkcount[i] > 2:                   # 3ofKIND 인지 검사
                self.handrank[6] = total

                if checkcount[i] > 3:               # 3ofKIND 에 해당될 경우 4ofKIND 인지 검사
                    self.handrank[7] = total

                    if checkcount[i] > 4:           # 4ofKIND 일 경우 YACHU 인지 검사
                        self.handrank[12] = 50
        if 2 in checkcount and 3 in checkcount:     # FULLHOUSE 검사
            self.handrank[8] = 25

        checkst = set(ran_num)
        for stset in self.stlist:                   # S,L STRAIGHT 인지 검사
            if checkst.issuperset(stset) and len(stset) < 5:
                self.handrank[9] = 30
            elif checkst.issuperset(stset) and len(stset) > 4:
                self.handrank[10] = 40

        self.handrank[11] = sum(ran_num)

    def gameend(self):
        if sum(self.myscore[0:6]) > 63:
            self.myscore.append(35)

        return sum(self.myscore)




