
SIZE = 300
SERIAL = 7315

def fuelValue(x,y,d):
    val = ((x+10)*y)*(x+10)+ d*(x+10)
    #(div,rem) = divmod(val % 1000,100)
    (div,rem) = divmod(val,100)
    (div,rem) = divmod(div,10)
    return rem-5

grid = [[fuelValue(x,y, SERIAL) for x in range(1,SIZE+1)] for y in range(1,SIZE+1)]

def getCellValue(grid, x,y):
    return grid[x][y]+grid[x+1][y]+grid[x+2][y]+\
           grid[x][y+1]+grid[x+1][y+1]+grid[x+2][y+1]+\
           grid[x][y+2]+grid[x+1][y+2]+grid[x+2][y+2]

def extendCellValue(grid, val, x, y,size):
    cell = val
    for i in range(size):
        cell += grid[x+i][y+size]
        cell += grid[x + size][y + i]
    cell += grid[x+size][y+size]
    return cell

def printGrid(grid, x, y):
    for i in range(x-1,x+5):
        for j in range(y - 1, y + 5):
            print(grid[i][j],' ', end='')
        print()

def findMaxCell(grid):
    curMax = getCellValue(grid,0,0)
    curX = 0
    curY = 0

    for x in range(SIZE-2):
        for y in range(SIZE-2):
            tmpVal = getCellValue(grid,x,y)
            if tmpVal >= curMax:
                curMax = tmpVal
                curX = x
                curY = y

    return [(curX+1, curY+1), curMax]

def findCoordOfMax(grid):
    curMax = grid[0][0]
    maxX = 0
    maxY = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            curVal = grid[i][j]
            if curVal > curMax:
                curMax = curVal
                maxX = i
                maxY = j
    return (maxX, maxY, curMax)

print((grid[299][299]))
printGrid(grid,71,20)
print(getCellValue(grid,297,297))
print(findMaxCell(grid))

result = [[0 for x in range(SIZE)] for y in range(SIZE)]
maxVal = grid[0][0]
maxX = 0
maxY = 0
maxS = 0
for k in range(0,300):
    for i in range(SIZE-k):
        for j in range(SIZE-k):
            result[i][j] = extendCellValue(grid, result[i][j], i, j, k)
    (curX, curY, curM) = (findCoordOfMax(result))
    print((curX+1, curY+1, curM, k+1))
    if (curM)> maxVal:
        (maxX, maxY, maxVal, maxS) = (curX, curY, curM, k+1)

print("Max :",(maxY+1, maxX+1, maxS, maxVal))