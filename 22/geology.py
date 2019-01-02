import collections
import math


depth= 11991
target= (6,797)
#depth = 510
#target = (10,10)

maxX = target[0]+50
maxY = target[1]+50


class Cavern:
    cavern = None
    maxX = None
    maxY = None
    depth = None

    def __init__(self, depth, maxX, maxY):
        self.maxY = maxY
        self.maxX = maxX
        self.depth = depth
        self.cavern = [[-1 for x in range(self.maxX)] for y in range(self.maxY)]
        for y1 in range(self.maxY):
            for x1 in range(self.maxX):
                self.calculate_erosion(x1, y1)


    def calculate_erosion(self, xx, yy):
        if self.cavern[yy][xx] > -1:
            return self.cavern[yy][xx]
        if (xx, yy) == (0, 0):
            ind = self.get_erosion_value(0)
        elif (xx, yy) == target:
            ind = self.get_erosion_value(0)
        elif yy == 0:
            ind = self.get_erosion_value(xx * 16807)
        elif xx == 0:
            ind = self.get_erosion_value(yy * 48271)
        else:
            #ind = (self.calculate_index(xx - 1, yy) * self.calculate_index(xx, yy - 1)) #% 20183
            ind = self.get_erosion_value(self.cavern[yy][xx-1]*self.cavern[yy-1][xx])
        self.cavern[yy][xx] = ind
        return ind

    def get_erosion_value(self, geological_index):
        return (geological_index + self.depth) % 20183

    def get_region_risk(self, xx, yy):
        return self.cavern[yy][xx] % 3

    def get_region_type(self, xx, yy):
        return ['.', '=', '|'][self.get_region_risk(xx, yy)]

    def print_map(self, target=(0,0)):
        for yy in range(self.maxY):
            for xx in range(self.maxX):
                if (xx == 0 and yy== 0):
                    print("M", end='')
                elif (xx,yy) == target:
                    print("T", end='')
                else:
                    print(self.get_region_type(xx, yy), end='')
            print()

TORCH = 0
CLIMB = 1
NEITHER = 2
ROCKY = 0
WET = 1
NARROW = 2

class Graph:
    graph = None
    cavern = None
    target = None
    to_relax = None
    to_relax_set = None

    def __init__(self, cavern, target):
        self.graph = [[[(math.inf, (-1,-1), False) for z in range(3)] for x in range(cavern.maxX)] for y in range(cavern.maxY)]
        self.cavern = cavern
        self.target = target
        self.graph[0][0][0] = (0, True)
        self.to_relax = collections.deque()
        self.to_relax_set = set()


    def isPassable(self, region_type, tool):
        if region_type == ROCKY:
            if (tool == TORCH) or (tool == CLIMB):
                return True
            else:
                return False
        if region_type == WET:
            if (tool == NEITHER) or (tool == CLIMB):
                return True
            else:
                return False
        if region_type == NARROW:
            if (tool == TORCH) or (tool == NEITHER):
                return True
            else:
                return False
        return None

    def neighbour_edges(self, cur_node):
        (x, y, z) = cur_node
        nb = [(x-1, y, z), (x, y+1, z), (x+1, y, z), (x, y -1, z)]
        valid_nb = []
        for neighbour in nb:
            (xa, ya, za) = neighbour
            if (xa >= 0) and (xa < maxX) and (ya >= 0) and  (ya < maxY):
                if self.isPassable(self.cavern.get_region_risk(xa, ya), za):
                        valid_nb.append((neighbour, 1))
        valid_nb.append(((x, y, (z+1) % 3), 7))
        valid_nb.append(((x, y, (z+2) % 3), 7))
        return valid_nb

    def BFS(self):
        self.graph[0][0][0] = (0, (0,0,0), False)
        self.to_relax.append((0,0,0))
        curShortest = (self.target[0] + self.target[1])*8
        while len(self.to_relax) > 0:
            cur_node = self.to_relax.popleft()
            (x, y, tool) = cur_node
            (cur_dist, orig_node, visited) = self.graph[y][x][tool]
            self.graph[y][x][tool] = (cur_dist, orig_node, True)
            neighbours = self.neighbour_edges(cur_node)
            for (nb, dist) in neighbours:
                (xa, ya, za) = nb
                (nb_dist, orig_node, nb_visited) = self.graph[ya][xa][za]
                if (cur_dist + dist < nb_dist):
                    nb_visited = False
                    if nb in self.to_relax_set:
                        self.to_relax_set.remove(nb)
                    self.graph[ya][xa][za] = (cur_dist + dist, cur_node, nb_visited)
                if (cur_dist + dist < curShortest) and (nb_visited is False):
                    if nb not in self.to_relax_set:
                        self.to_relax.append(nb)
                        self.to_relax_set.add(nb)
                if (xa, ya) == self.target and za == TORCH:
                    curShortest = self.graph[ya][xa][za][0]
        return curShortest+1

    def print_path_from(self,target):
        (xx, yy) = target
        cur_node = (xx, yy, 0)
        path = []
        while cur_node != (0,0,0):
            (xx, yy, tool) = cur_node
            (dist, prev_node, visited) = self.graph[yy][xx][tool]
            path.append((cur_node, dist))
            cur_node = prev_node
        path.reverse()
        return path




cc = Cavern(depth, maxX, maxY)

cc.print_map(target)

#cavern_map = [[get_erosion_level(x, y, cavern, depth) for x in range(maxX)] for y in range(maxY)]
#cavern_risk = [[get_region_risk(cavern_map, x, y) for x in range(maxX)] for y in range(maxY)]

rr = 0
for x1 in range(target[0]+1):
    for y1 in range(target[1]+1):
        rr += cc.get_region_risk(x1, y1)
print(rr)

gg = Graph(cc, target)
print(gg.BFS())
print(gg.print_path_from(target))
#print(gg.graph)