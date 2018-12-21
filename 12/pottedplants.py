import re

class Field:
    field = None
    offset = None

    def __init__(self, offset, init_map):
        self.field = init_map
        self.offset = offset

    def get_value_at(self, position):
        if position < self.offset or position >= self.offset+len(self.field):
            return '.'
        else:
            return self.field[self.offset+position]

    def get_unit(self, offset, length):
        realoffset = offset - self.offset
        if offset >= self.offset:
            tmpUnit = self.field[realoffset:realoffset+length]
            if len(tmpUnit) < length:
                tmpUnit += '.' * length
                tmpUnit = tmpUnit[:length]
        else:
            tmpUnit = '.' * length
            tmpUnit += self.field[:length+realoffset]
            tmpUnit = tmpUnit[-length:]
        return tmpUnit

    def get_bounds(self):
        return (self.offset, self.offset+len(self.field))

    def push_value(self, value):
        if len(self.field)==0 and value == '.':
            self.offset += 1
        else:
            self.field += value

    def trim_field(self):
        while self.field[-1] == '.' and len(self.field)>2:
            self.field = self.field[:-1]

    def score_field(self):
        tmpVal = 0
        for i in range(len(self.field)):
            if self.field[i] == '#':
                tmpVal += i + self.offset
        return tmpVal

def get_elem():
    elem_list = []
    file = open('input', 'r')
    for line in file:
        elem_list.append(line)
    return elem_list


def get_init_map(elem):
    print(elem)
    mapre = re.compile('initial state: (.+)\n')
    init_map = mapre.match(elem).group(1)
    return init_map

def get_rules(elem_list):
    rule_re = re.compile('(.+) => (.)\n')
    rules_list = {}
    for line in elem_list:
        m = rule_re.match(line)
        (src, dst) = (m.group(1), m.group(2))
        rules_list[src] = dst
    return rules_list


def calculate_nextgen(oldField, rules, rule_size):
    (min,max) = oldField.get_bounds()
    newField = Field(min-int((rule_size-1)/2)-1,'')
    for i in range(min-rule_size, max+rule_size):
        unit = myField.get_unit(i, rule_size)
        if unit in rules:
            val = rules[unit]
        else:
            val = '.'
        newField.push_value(val)
    newField.trim_field()
    return newField

elem_list = get_elem()
initial_map = get_init_map(elem_list[0])
elem_list.pop(0)
elem_list.pop(0)

rules = get_rules(elem_list)
for i in rules:
    rule_size = len(i)

print(initial_map)
myField = Field(0 ,initial_map)
for i in range(100):
    newField = calculate_nextgen(myField, rules, rule_size)
    if not (i % 1):
        #print(i, newField.field)
        print(i,newField.score_field(), myField.field == newField.field)
    myField = newField
print(myField.offset)
print(myField.score_field())

print(4184+38*(50000000000-100))