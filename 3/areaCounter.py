import re

class Rect:
    def __init__(self, idNum, iLeft, iTop, iWidth, iHeigth):
        self.idNum = idNum
        self.iLeft = iLeft
        self.iTop = iTop
        self.iWidth = iWidth
        self.iHeight = iHeigth

    def isCoordInRect(self, x, y):
        if (x >= self.iLeft) and (x< self.iLeft+self.iWidth) and (y >= self.iTop)and (y< self.iTop + self.iHeight):
            return True
        return False

    def maxHorizCoord(self):
        return (self.iLeft + self.iWidth)

    def maxVertCoord(self):
        return (self.iTop + self.iHeight)

    def report(self):
        print('#{} @ {},{}: {}x{}'.format(self.idNum, self.iLeft, self.iTop, self.iWidth, self.iHeight))


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

maxX = 0
maxY = 0
for tmpRect in listRect:
    maxX = max(maxX, tmpRect.maxHorizCoord())
    maxY = max(maxY, tmpRect.maxVertCoord())

print(maxX, maxY)

def countByPixel():
    countArea = 0
    for i in range(maxX+1):
        print(i)
        for j in range(maxY+1):

            inRect = 0
            for tmpRect in listRect:
                if tmpRect.isCoordInRect(i,j):
                    inRect +=1
                if inRect >=2:
                    countArea+=1
                    break

    print(countArea)

def countByFilling():
    area = [[0 for x in range(maxX+1)] for y in range(maxY+1)]

    for tmpRect in listRect:
        for i in range(tmpRect.iLeft, tmpRect.iLeft + tmpRect.iWidth):
            for j in range(tmpRect.iTop, tmpRect.iTop + tmpRect.iHeight):
                area[i][j] +=1

    countArea = 0
    for i in range(maxY+1):
        for j in range(maxX+1):
            if area[i][j] >= 2:
                countArea += 1
    print(countArea)

countByFilling()
