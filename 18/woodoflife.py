def get_elem_list():
    elem_list = []
    file = open('input', 'r')
    for line in file:
        elem_list.append(line.rstrip('\n'))
    return elem_list

OPEN = '.'
WOOD = '|'
LUMBERYARD ="#"

class Wood:
    wood = None
    maxX = None
    maxY = None

    def __init__(self, wood):
        self.wood = wood.copy()
        self.maxX = len(self.wood[0])
        self.maxY = len(self.wood)

    def __repr__(self):
        return '\n'.join(self.wood)

    def get_acre(self,x, y):
        if (x<0) or (y<0) or (x>= self.maxX) or(y>=self.maxY):
            return OPEN
        else:
            return self.wood[y][x]

    def count_neighbours(self,x,y):
        ngb = {}
        ngb[OPEN] = 0
        ngb[WOOD] = 0
        ngb[LUMBERYARD] = 0
        for (dx,dy)in [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]:
            ngb[self.get_acre(x+dx,y+dy)] += 1
        return ngb

    def get_new_acre(self,cur_acre, neighbours):
        if cur_acre == OPEN:
            if neighbours[WOOD]>=3:
                return WOOD
            else:
                return OPEN
        if cur_acre == WOOD:
            if neighbours[LUMBERYARD]>=3:
                return LUMBERYARD
            else:
                return WOOD
        if cur_acre == LUMBERYARD:
            if neighbours[LUMBERYARD]>=1 and neighbours[WOOD]>=1:
                return LUMBERYARD
            else:
                return OPEN

    def next_gen(self):
        new_wood = [[OPEN for x in range(self.maxX)] for y in range(self.maxY)]
        for y in range(self.maxY):
            for x in range(self.maxX):
                new_wood[y][x] = self.get_new_acre(self.get_acre(x,y), self.count_neighbours(x,y))
            new_wood[y] = ''.join(new_wood[y])
        self.wood = new_wood

    def count_acres(self):
        ngb = {}
        ngb[OPEN] = 0
        ngb[WOOD] = 0
        ngb[LUMBERYARD] = 0
        for y in range(self.maxY):
            for x in range(self.maxX):
                ngb[self.get_acre(x, y)] += 1
        return ngb


wd = get_elem_list()
wood = Wood(wd)
print(wood)
print()

for i in range(10):
    wood.next_gen()
print(wood)

xx = wood.count_acres()
print(xx)
print(xx[WOOD]* xx[LUMBERYARD])

wd = get_elem_list()
wood = Wood(wd)
print(wood)
print()

# Try to find repetitions ...
xx_dict = {}
for i in range(1000):
    wood.next_gen()
    if i>500:
        xxc = (wood.count_acres())
        xx = (xxc[OPEN], xxc[WOOD], xxc[LUMBERYARD])
        if xx in xx_dict:
            xx_dict[xx].append(i)
        else:
            xx_dict[xx] = [i]

print(xx_dict)
print(wood)

# from 564 we have a 28 periodicity
# 1000000000 - 564 mod 28 = 16
#--> calculate for 564 + 16
wd = get_elem_list()
wood = Wood(wd)
print(wood)
print()

for i in range(564+16):
    wood.next_gen()
print(wood)

xx = wood.count_acres()
print(xx)
print(xx[WOOD]* xx[LUMBERYARD])
