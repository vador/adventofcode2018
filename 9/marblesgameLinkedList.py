# 426 players; last marble is worth 72058 points

tests = [
    (10,1618,8317),
    (13,7999,146373),
    (17,1104,2764),
    (21,6111,54718),
    (30,5807,37305)]

PLAYERS = 426
MARBLES = (72058*100)+1

class node():
    value = None
    prev = None
    next = None

    def __init__(self,value):
        self.value = value
        self.next = self
        self.prev = self

    def insertNext(self, value):
        newNode = node(value)

        self.next.prev = newNode
        newNode.next = self.next
        newNode.prev = self
        self.next = newNode
        return newNode

    def removeNode(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self.next



class circle():
    marbles = None
    current = None


    def addNormalMarble(self,value):
        if self.marbles is None:
            self.marbles = node(value)
            self.current = self.marbles
        else:
            tmp = self.current.next.insertNext(value)
            self.current = tmp
        return 0

    def addSpecialMarble(self, value):
        self.current = self.current.prev.prev.prev.prev.prev.prev.prev
        score = self.current.value
        self.current = self.current.removeNode()
        return score+value

    def __repr__(self):
        tmpStr = '{} '.format(self.marbles.value)
        tmpMarble = self.marbles.next
        while tmpMarble != self.marbles:
            if tmpMarble == self.current:
                tmpStr += '(' + '{}'.format(tmpMarble.value) + ') '
            else:
                tmpStr += '{} '.format(tmpMarble.value)
            tmpMarble = tmpMarble.next
        return tmpStr


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
    print(m)

ss = m.addSpecialMarble(23)
print(m)
ss = m.addNormalMarble(24)
print(m)
ss = m.addNormalMarble(25)
print(m)

print(ss)

res = (playGame(PLAYERS,MARBLES))
print(max(res))