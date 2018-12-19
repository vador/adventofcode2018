
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


point_list = elemListToPointList(getElem())
for i in range(len(point_list)):
    point_list[i].name = chr(ord('a')+i)

areaCount = 0
refDist = 10000
xMax = max([point.x for point in point_list])
yMax = max([point.y for point in point_list])
for j in range(yMax+1):
    print(j, ' ', end='')
    for i in range(xMax+1):
        q = point(i,j)
        tempDist = 0
        for p in point_list:
            tempDist += q.manDistance(p)

        if tempDist < refDist:
            areaCount +=1
        print(q, end='')
    print()
print(areaCount)