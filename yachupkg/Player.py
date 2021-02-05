class Player:
    def __init__(self):
        self.myscore = [0 for i in range(0, 13)]
        self.handrank = [0 for i in range(0, 13)]
        self.turncheck = 0

    def checkTurn(self):
        if self.turncheck > 2:
            return True
        else:
            self.turncheck = self.turncheck+1
            return False

# self.handrank index
# 0 = ONE / 1 = TWO / 2 = THREE / 3 = FOUR / 4 = FIVE / 5 = SIX
# 6 = 3ofKIND / 7 = 4ofKIND / 8 = FULLHOUSE / 9 = S.STRAIGHT / 10 = L.STRAIGHT
# 11 = CHANCE / 12 = YACHU
# self.myscore index
# 13 = BONUS
    def checkHandrank(self, ran_num):
        self.handrank = self.myscore.copy()
        #ran_num.sort()
        checkcount = [0,0,0,0,0,0]
        for i in range(0, 6):                       # 1~6까지 검사
            checkcount[i] = ran_num.count(i+1)
            total = sum(ran_num)
            self.handrank[i] = checkcount[i]*(i+1)
            self.handrank[11] = total
            if checkcount[i] > 2:
                self.handrank[6] = total

                if checkcount[i] > 3:
                    self.handrank[7] = total

                    if checkcount[i] > 4:
                        self.handrank[12] = 50
        if 2 in checkcount and 3 in checkcount:
            print(checkcount)
            self.handrank[8] = 25

        if [1, 2, 3, 4] or [2, 3, 4, 5] or [3, 4, 5, 6] in ran_num:
            self.handrank[9] = 30
            if [1, 2, 3, 4, 5] or [2, 3, 4, 5, 6] in ran_num:
                self.handrank[10] = 40


    def gameend(self):
        if sum(self.myscore[0:6]) > 63:
            self.myscore.append(35)

        return sum(self.myscore)




