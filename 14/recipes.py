
class Scores:
    scores = [3,7]
    scoresstr = "37"
    pos1 = 0
    pos2 = 1

    def add_recipe(self):
        recipe = self.scores[self.pos1] + self.scores[self.pos2]
        (move1, move2) = divmod(recipe,10)
        if move1 > 0:
            self.scores.append(move1)
            self.scoresstr += str(move1)
        self.scores.append(move2)
        self.scoresstr += str(move2)
        ll = len(self.scores)
        self.pos1 = (self.pos1 + self.scores[self.pos1] + 1) % ll
        self.pos2 = (self.pos2 + self.scores[self.pos2] + 1) % ll

    def draw(self):
        tmpStr = []
        for (i,val) in enumerate(self.scores):
            curVal = str(val)
            if i == self.pos1:
                curVal = '('+curVal+')'
            else:
                curVal = ' ' + curVal + ' '
            if i == self.pos2:
                curVal = '[' + curVal + ']'
            else:
                curVal = ' ' + curVal + ' '
            tmpStr.append(curVal)
        return ''.join(tmpStr)

my_scores = Scores()

EXTR = 51589
while len(my_scores.scores) < (EXTR+10):
    #print(my_scores.draw())
    print(len(my_scores.scores))
    my_scores.add_recipe()

print(''.join(map(str,my_scores.scores[EXTR:EXTR+11])))

EXTRSTR = str(EXTR)

my_scores = Scores()
curPos = 0
my_scores.add_recipe()
my_scores.add_recipe()
my_scores.add_recipe()
my_scores.add_recipe()
while my_scores.scoresstr[curPos:curPos+5] != EXTRSTR:
    print(my_scores.scoresstr[curPos:curPos+5],my_scores.scoresstr )
    my_scores.add_recipe()
    curPos +=1

print(curPos)