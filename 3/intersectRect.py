import re

class Rect:
    def __init__(self, idNum, iLeft, iTop, iWidth, iHeigth):
        self.idNum = idNum
        self.iLeft = iLeft
        self.iTop = iTop
        self.iWidth = iWidth
        self.iHeigth = iHeigth

    def isCoordInRect(self, x, y):
        if (x >= self.iLeft) and (x< self.iLeft+self.iWidth) and (y >= self.iTop)and (y< self.iTop + self.iHeight):
            return True
        return False

    def maxHorizCoord(self):
        return (self.iLeft + self.iWidth)

    def maxVertCoord(self):
        return (self.iTop + self.iHeight)

    def isIntersecting(self, rect):
        if self.iLeft < rect.iLeft:
            rect1 = self
            rect2 = rect
        else:
            rect1 = rect
            rect2 = self

        # rect1 is left of rect2
        if (rect1.iLeft + rect1.iWidth) < rect2.iLeft:
            return False

        if self.iTop < rect.iTop:
            rect1 = self
            rect2 = rect
        else:
            rect1 = rect
            rect2 = self

        # rect1 is top of rect2
        if (rect1.iTop + rect1.iHeigth) < rect2.iTop:
            return False
        return True



    def report(self):
        print('#{} @ {},{}: {}x{}'.format(self.idNum, self.iLeft, self.iTop, self.iWidth, self.iHeigth))


def getList():
    rectList = []
    file = open('input', 'r')
    for line in file:
        rectList.append(parseRectangle(line))
    return rectList

def parseRectangle(msg):
        rectangle = re.compile(r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$")
        rectm = rectangle.match(msg)
        tempRect =  Rect(int(rectm.group(1)), int(rectm.group(2)), int(rectm.group(3)), int(rectm.group(4)), int(rectm.group(5)))
        return tempRect

listRect = getList()

nbRect = len(listRect)
interRect = [False for x in range(nbRect)]
for i in range(nbRect):
    for j in range(i+1, nbRect):
        if listRect[i].isIntersecting(listRect[j]):
            interRect[i] = True
            interRect[j] = True

print(interRect)

for i in range(nbRect):
    if interRect[i] == False:
        print(listRect[i].report())