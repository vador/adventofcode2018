# 426 players; last marble is worth 72058 points

tests = [
    (10,1618,8317),
    (13,7999,146373),
    (17,1104,2764),
    (21,6111,54718),
    (30,5807,37305)]

PLAYERS = 426
MARBLES = (72058*1)+1

class circle():
    marbles = None
    current = 0

    def __init__(self):
        self.marbles = []
        self.current = 0

    def addNormalMarble(self,value):
        if  len(self.marbles) == 0:
            self.marbles.append(value)
            self.current = 0
        elif len(self.marbles) == 1:
            self.marbles.append(value)
            self.current = 1
        else:
            self.current = (self.current + 1) % (len(self.marbles)) + 1
            self.marbles.insert(self.current, value)
        return 0

    def addSpecialMarble(self, value):
        self.current = (self.current - 7) % len(self.marbles)
        score = self.marbles.pop(self.current)
        return score+value

def playGame(nbplayers, marbles):
    m = circle()
    players = [0 for i in range(nbplayers)]
    curplayer = 0
    for marble in range(marbles):
        if (marble == 0) or (marble % 23):
            score = m.addNormalMarble(marble)
        else:
            score = m.addSpecialMarble(marble)

        players[curplayer] += score
        curplayer = (curplayer+1) % nbplayers
    return players

m = circle()

for i in range(23):
    m.addNormalMarble(i)

    print(m.marbles, m.current)

ss = m.addSpecialMarble(23)
print(m.marbles, m.current)
ss = m.addNormalMarble(24)
print(m.marbles, m.current)
ss = m.addNormalMarble(25)
print(m.marbles, m.current, m.marbles[m.current])

print(ss)

res = (playGame(PLAYERS,MARBLES))
print(max(res))