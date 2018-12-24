import pyprofiler

class Scores:
    scores = [3,7]
    scoresstr = "37"
    pos1 = 0
    pos2 = 1
    ll = 2

    def add_recipe(self):
        recipe = self.scores[self.pos1] + self.scores[self.pos2]
        #recipe = int(self.scoresstr[self.pos1])+int(self.scoresstr[self.pos2])
        (move1, move2) = divmod(recipe,10)
        if move1 > 0:
            self.scores.append(move1)
            #self.scoresstr += str(move1)
            self.ll += 1
        self.scores.append(move2)
        #self.scoresstr += str(move2)
        self.ll += 1
        ll = self.ll
        self.pos1 = (self.pos1 + self.scores[self.pos1] + 1) % ll
        self.pos2 = (self.pos2 + self.scores[self.pos2] + 1) % ll
        #self.pos1 = (self.pos1 + int(self.scoresstr[self.pos1]) + 1) % ll
        #self.pos2 = (self.pos2 + int(self.scoresstr[self.pos2]) + 1) % ll

    def get_str_at(self,pos, length):
        if (pos+length>self.ll):
            return ''
        else:
            return ''.join(map(str,self.scores[pos:pos+length]))

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


EXTR = 286051

EXTRSTR = str(EXTR)
EXTRL = len(EXTRSTR)
my_scores = Scores()
curPos = 0

profiler = pyprofiler.start_profile()
while (curPos <= 300000):
    if not (curPos % 100000):
        print(curPos)
    #print(my_scores.scoresstr[curPos:curPos+EXTRL], curPos) #,my_scores.scoresstr )
    while my_scores.ll < curPos + EXTRL +1:
        my_scores.add_recipe()
    curPos +=1
    if (my_scores.get_str_at(curPos,EXTRL) == EXTRSTR):
        print('Found :', curPos)

pyprofiler.end_profile(profiler)

#20195114