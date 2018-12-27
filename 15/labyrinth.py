import collections

def get_elem_list():
    elem_list = []
    file = open('input', 'r')
    for line in file:
        elem_list.append(line.rstrip('\n'))
    return elem_list

class Labyrinth:
    lab = None
    sizeX = None
    sizeY = None
    def __init__(self, input):
        self.lab = input
        self.sizeX = len(input[0])
        self.sizeY = len(input)

    def __copy__(self):
        newL = Labyrinth(self.lab.copy())
        return newL

    def get_cell(self, x, y):
        return self.lab[y][x]

    def get_neighbours(self, x, y):
        n_list = []
        if y > 0:
            n_list.append((x, y-1))
        if x > 0:
            n_list.append((x-1, y))
        if x < self.sizeX-1:
            n_list.append((x+1, y))
        if y < self.sizeY-1:
            n_list.append((x, y+1))
        return n_list

    def is_free_cell(self, x, y):
        return self.get_cell(x, y) == '.'

    def is_goblin_cell(self, x, y):
        return self.get_cell(x, y) == 'G'

    def is_wall_cell(self, x, y):
        return self.get_cell(x, y) == '#'

    def is_elf_cell(self, x, y):
        return self.get_cell(x, y) == 'E'

    def get_free_neighbours(self, x, y):
        n_list = self.get_neighbours(x, y)
        res_list = []
        for cell in n_list:
            (x, y) = cell
            if self.is_free_cell(x, y):
                res_list.append(cell)
        return res_list

my_labyrinth = Labyrinth(get_elem_list())

print(my_labyrinth.get_cell(17, 4))
print(my_labyrinth.get_free_neighbours(16,3))

newL = my_labyrinth.__copy__()
newL.lab[0] = 'Grou'
print(my_labyrinth.lab[0][0])
print(newL.lab[0][0])