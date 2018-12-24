import re
import collections

def getElem():
    elem_list = []
    file = open('input', 'r')
    for line in file:
        elem_list.append(line)
    return elem_list

class point():
    x = None
    y = None
    dx = None
    dy = None

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def get_coord_at_second(self,s):
        return (self.x + self.dx*s, self.y + self.dy*s)


def convert_elem_list_to_points(elem_list):
    point_list = []
    #position=< 52672,  52690> velocity=<-5, -5>
    #0123456789012345678901234567890123456789012
    #0000000000111111111122222222223333333333444
    for elem in elem_list:
        x = int(elem[10:16])
        y = int(elem[17:24])
        dx = int(elem[36:38])
        dy = int(elem[39:42])
        point_list.append(point(x, y, dx, dy))
    return point_list


def get_bounded_box(p_list, s):
    (minX, minY) =  p_list[0].get_coord_at_second(s)
    (maxX, maxY) = (minX, minY)
    for p in p_list:
        (curX, curY) = p.get_coord_at_second(s)
        if curX < minX:
            minX = curX
        if curY < minY:
            minY = curY
        if curX > maxX:
            maxX = curX
        if curY > maxY:
            maxY = curY

    return ((minX, minY), (maxX, maxY))


el = getElem()
pl = convert_elem_list_to_points(el)
print(get_bounded_box(pl,10000))
print(get_bounded_box(pl,10100))
print(get_bounded_box(pl,10200))
print(get_bounded_box(pl,10511))

for i in range(20000):
    None
    #((a,b),(c,d)) = get_bounded_box(pl, i)
    #print(i,c-a, d-b)

map = [[' '] * 200 for j in range(400)]
i = 10511
for p in pl:
    (x, y) = p.get_coord_at_second(i)
    map[y][x - 250] = '*'
for m in map:
    print(''.join(m))