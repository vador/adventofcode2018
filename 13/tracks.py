
SOUTH = 0
WEST = 1
NORTH = 2
EAST = 3

SYMBOLDIRECTION = {'v': SOUTH, '<': WEST, '^': NORTH, '>': EAST}
DIRECTIONSYMBOL = {SOUTH: 'v', WEST: '<', NORTH: '^', EAST: '>'}

def get_elem_list():
    elem_list = []
    file = open('input', 'r')
    for line in file:
        elem_list.append(line.rstrip('\n'))
    return elem_list

class Cart:
    cartno = None
    xpos = None
    ypos = None
    direction = None
    turn_no = None
    collided = False

    def __repr__(self):
        return("C" + str(self.cartno) + str(((self.xpos, self.ypos), self.direction)) )

    def __cmp__(self, other):
        if (self.ypos != other.ypos):
            return self.ypos - other.ypos
        else:
            return self.xpos - other.xpos

    def __lt__(self, other):
        if self.__cmp__(other) < 0:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.__cmp__(other) == 0:
            return True
        else:
            return False

    def __init__(self,x,y,direction, cartno):
        self.xpos = x
        self.ypos = y
        self.direction = direction
        self.turn_no = 0
        self.cartno = cartno

    def turn_right(self):
        self.direction = (self.direction+ 1) % 4

    def turn_left(self):
        self.direction = (self.direction - 1) % 4

    def move(self, track_map):
        if self.direction % 2:
            self.xpos += self.direction - 2
        else:
            self.ypos += 1 - self.direction
        next_symbol = track_map[self.xpos][self.ypos]
        if next_symbol == '/':
            if self.direction == EAST:
                self.direction = NORTH
            elif self.direction == SOUTH:
                self.direction = WEST
            elif self.direction == WEST:
                self.direction = SOUTH
            elif self.direction == NORTH:
                self.direction = EAST
        if next_symbol == '\\':
            if self.direction == EAST:
                self.direction = SOUTH
            elif self.direction == NORTH:
                self.direction = WEST
            elif self.direction == WEST:
                self.direction = NORTH
            elif self.direction == SOUTH:
                self.direction = EAST
        if next_symbol == '+':
            if self.turn_no == 0:
                self.turn_left()
            elif self.turn_no == 2:
                self.turn_right()
            self.turn_no = (self.turn_no + 1) % 3

def print_tracks(track_map, cart_list):
    newcart = cart_list.copy()
    newcart.sort(reverse=True)
    newtrack = track_map.copy()
    if len(newcart)>0:
        nw = newcart.pop()
    else:
        nw = Cart(-1,-1,0,-1)
    for y in range(len(newtrack[0])):
        for x in range(len(newtrack)):
            if nw.xpos == x and nw.ypos == y:
                print(DIRECTIONSYMBOL[nw.direction], end='')
                if len(newcart)>0:
                    nw = newcart.pop()
            else:
                print(newtrack[x][y], end='')
        print()


def build_carts(track_map):
    cart_list = []
    cartno = 1
    for x in range(len(track_map)):
        for y in range(len(track_map[0])):
            tmp = track_map[x][y]
            if tmp in SYMBOLDIRECTION:
                new_cart = Cart(x, y, SYMBOLDIRECTION[tmp], cartno)
                if tmp == '<' or tmp == '>':
                    track_map[x][y] = "-"
                else:
                    track_map[x][y] = "|"
                cart_list.append(new_cart)
                cartno += 1
    return cart_list



track_map_ = get_elem_list()
maxX = len(track_map_[0])
maxY = len(track_map_)
track_map = [[track_map_[y][x] for y in range(maxY)] for x in range(maxX)]
cart_list = build_carts(track_map)
cart_list.sort()
print(cart_list)

print_tracks(track_map,cart_list)
tick = 0
collision = False
collCart = None
print('-------------------')
while len(cart_list)>1:
    for cart in cart_list:
        cart.move(track_map)
        for cart2 in cart_list:
            if (cart == cart2) and (cart.cartno != cart2.cartno):
                cart.collided= True
                cart2.collided = True
                break
    cart_list = list(filter(lambda t: not t.collided, cart_list))
    tick += 1
    print(tick)
    cart_list.sort()
    print(cart_list)
    #print_tracks(track_map, cart_list)


    print(cart_list)

print_tracks(track_map, cart_list)
print(cart_list)