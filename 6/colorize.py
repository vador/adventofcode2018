
def getElem():
    elem_list = []
    file = open('input', 'r')
    for line in file:
        elem_list.append(line)
    return elem_list

def elemListToPointList(elem_list):
    point_list = []
    for elem in elem_list:
        [x,y] = elem.split(',')
        x = int(x)
        y = int(y)
        point_list.append(point(x,y))
    return point_list

def buildKDTree(point_list):
    root = nodeH(point_list.pop(0))
    for point in point_list:
        root.addChild(point)
    return root

class point:
    x = None
    y = None
    name = None
    def __init__(self,x,y, name=None):
        self.x = x
        self.y = y
        self.name = name

    def manDistance(self, point2):
        return abs(self.x - point2.x) + abs(self.y - point2.y)

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def __str__(self):
        if self.name is None:
            return "({}, {})".format(self.x, self.y)
        else:
            return self.name

class nodeH:
    parent = None
    point = None
    childU = None
    childD = None

    def __init__(self,point, parent=None):
        self.point = point
        self.parent = parent

    def addChild(self,newPoint):
        if (newPoint.y <= self.point.y):
            if self.childU is None:
                self.childU = nodeV(newPoint, self)
            else:
                self.childU.addChild(newPoint)
        else:
            if self.childD is None:
                self.childD = nodeV(newPoint, self)
            else:
                self.childD.addChild(newPoint)

    def __repr__(self):
        return "H{} ({}|{})".format(self.point, self.childU, self.childD)

class nodeV:
    point = None
    parent = None
    childL = None
    childR = None

    def __init__(self, point, parent=None):
        self.point = point
        self.parent = parent

    def addChild(self, newPoint):
        if (newPoint.x > self.point.x):
            if self.childR is None:
                self.childR = nodeH(newPoint, self)
            else:
                self.childR.addChild(newPoint)
        else:
            if self.childL is None:
                self.childL = nodeH(newPoint, self)
            else:
                self.childL.addChild(newPoint)

    def __repr__(self):
        return "V{} ({}|{})".format(self.point, self.childL, self.childR)

def nearestPoints(curNearest, candidates):
    for item in candidates:
        curNearest = nearestTwoPoints(curNearest, candidates)
    return curNearest

def nearestTwoPoints(curNearest, candidate):
    if curNearest is None or len(curNearest)==0:
        return [candidate]
    if len(curNearest) == 1:
        if curNearest[0][1] < candidate[1]:
            curNearest.append(candidate)
        else:
            curNearest = [candidate, curNearest[0]]
        return curNearest
    [first, second] = curNearest
    if candidate[1] > second[1]:
        return curNearest
    if candidate[1] < first[1]:
        return [candidate, first]
    else:
        return [first, candidate]

def findClosestFromH(point, node_h, closestPoints = None):
    curPoint = [node_h.point, point.manDistance(node_h.point)]
    if closestPoints is None:
        closestPoints = [curPoint]
    else:
        closestPoints = nearestTwoPoints(closestPoints, curPoint)
    minDist = closestPoints[-1][1]
    if node_h.childU is not None:
        if (point.y <= node_h.point.y) or ((point.y > node_h.point.y) and (point.y - minDist <= node_h.point.y)):
            closestPoints = findClosestFromV(point, node_h.childU, closestPoints)
            minDist = closestPoints[-1][1]
    if node_h.childD is not None:
        if (point.y > node_h.point.y) or ((point.y <= node_h.point.y) and (point.y + minDist >= node_h.point.y)):
            closestPoints = findClosestFromV(point, node_h.childD, closestPoints)
            minDist = closestPoints[-1][1]
    return closestPoints

def findClosestFromV(point, node_h, closestPoints = None):
    curPoint = [node_h.point, point.manDistance(node_h.point)]
    if closestPoints is None:
        closestPoints = [curPoint]
    else:
        closestPoints = nearestTwoPoints(closestPoints, curPoint)
    minDist = closestPoints[-1][1]
    if node_h.childR is not None:
        if (point.x > node_h.point.x) or (point.x <= node_h.point.x) and (point.x + minDist > node_h.point.x):
            closestPoints = findClosestFromH(point, node_h.childR, closestPoints)
            minDist = closestPoints[-1][1]
    if node_h.childL is not None:
        if (point.x <= node_h.point.x) or (point.x > node_h.point.x) and (point.x - minDist <= node_h.point.x):
            closestPoints = findClosestFromH(point, node_h.childL, closestPoints)
            minDist = closestPoints[-1][1]
    return closestPoints

def getClosestTo(closestPoints):
    if closestPoints is None:
        return None
    if len(closestPoints) == 1:
        return closestPoints[0][0]
    [first, second] = closestPoints[0:2]
    if first[1] < second[1]:
        return first[0]
    else:
        if first[0] == second[0]:
            return first[0]
        else:
            return "."


point_list = elemListToPointList(getElem())
for i in range(len(point_list)):
    point_list[i].name = chr(ord('a')+i)

R = buildKDTree(point_list)

areaList = {}
excludeList = set()
xMax = max([point.x for point in point_list])
yMax = max([point.y for point in point_list])
for j in range(yMax+1):
    print(j, ' ', end='')
    for i in range(xMax+1):
        c = getClosestTo(findClosestFromH(point(i,j),R))
        if c not in areaList:
            areaList[c] = 1
        else:
            areaList[c] += 1
        if (i == 0) or (i == xMax) or (j==0) or (j==yMax):
            excludeList.add(c)

        print(c, end='')
    print()

print(excludeList)
areaList2 = areaList.copy()
for area in excludeList:
    areaList2.pop(area, None)

print(areaList2)
maxArea = 0
for area in areaList2:
    if areaList2[area]>maxArea:
        maxArea = areaList2[area]

print(maxArea)
p = point(271, 210)
print(findClosestFromH(p,R))