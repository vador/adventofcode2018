
def get_elem_list():
    elem_list = []
    file = open('input', 'r')
    for line in file:
        elem_list.append(line.rstrip('\n'))
    return elem_list

def build_lists(elem_list):
    blind_operations = []
    intructions= []
    while len(elem_list)>0:
        line = elem_list.pop(0)
        if line[0:8] == 'Before: ':
            elem = line[9:-1]
            previous = (map(int,elem.split(',')))
            previous = list(previous)
            operation = tuple(map(int,elem_list.pop(0).split(' ')))
            after = list(map(int, elem_list.pop(0)[9:-1].split(',')))
            blind_operations.append([previous, operation, after])
        elif len(line)> 0:
            intructions.append(tuple(map(int,line.split(' '))))
    return (blind_operations, intructions)

class Registers:
    registers = None

    def __index__(self):
        self.registers = [0, 0, 0, 0]

    def set_registers(self, init_registers):
        self.registers = init_registers.copy()


    def addi(self, A, B, C):
        self.registers[C] = self.registers[A] + B

    def addr(self, A, B, C):
        self.registers[C] = self.registers[A] + self.registers[B]

    def muli(self, A, B, C):
        self.registers[C] = self.registers[A] * B

    def mulr(self, A, B, C):
        self.registers[C] = self.registers[A] * self.registers[B]

    def bani(self, A, B, C):
        self.registers[C] = self.registers[A] & B

    def banr(self, A, B, C):
        self.registers[C] = self.registers[A] & self.registers[B]

    def bori(self, A, B, C):
        self.registers[C] = self.registers[A] | B

    def borr(self, A, B, C):
        self.registers[C] = self.registers[A] | self.registers[B]

    def seti(self, A, B, C):
        self.registers[C] = A

    def setr(self, A, B, C):
        self.registers[C] = self.registers[A]

    def gtir(self, A, B, C):
        if A > self.registers[B]:
            self.registers[C] = 1
        else:
            self.registers[C] = 0

    def gtri(self, A, B, C):
        if self.registers[A] > B:
            self.registers[C] = 1
        else:
            self.registers[C] = 0

    def gtrr(self, A, B, C):
        if self.registers[A] > self.registers[B]:
            self.registers[C] = 1
        else:
            self.registers[C] = 0

    def eqir(self, A, B, C):
        if A == self.registers[B]:
            self.registers[C] = 1
        else:
            self.registers[C] = 0

    def eqri(self, A, B, C):
        if self.registers[A] == B:
            self.registers[C] = 1
        else:
            self.registers[C] = 0

    def eqrr(self, A, B, C):
        if self.registers[A] == self.registers[B]:
            self.registers[C] = 1
        else:
            self.registers[C] = 0

    #opcodes = [ addi, addr, muli, mulr, bani, banr, bori, borr, seti, setr, gtir, gtri, gtrr, eqri, eqir, eqrr]
    opcodes = [ addi, bani, gtir, borr, eqrr, bori, gtrr, setr, muli, seti, banr, gtri, eqir, eqri, addr, mulr]

    def apply_arbitrary_opcode(self, func, input_val):
        (opcode, A, B, C) = input_val
        func(A,B,C)
        return self.registers

    def apply_instruction(self, instruction):
        (opcode, A, B, C) = instruction
        self.opcodes[int(opcode)](self,A,B,C)

    def cmp_registers(self, outcome):
        return (self.registers[0] == outcome[0]) and (self.registers[1] == outcome[1]) and \
               (self.registers[2] == outcome[2]) and (self.registers[3] == outcome[3])

    def how_many_opcodes(self, initial, instruction, outcome):
        (opcode, input1, input2, output) = instruction
        nb_op = 0
        candidate = []
        for fun in self.opcodes:
            self.registers = initial.copy()
            fun(self, input1, input2, output)
            if self.cmp_registers(outcome):
                nb_op += 1
                candidate.append(fun.__name__)
        return (nb_op, (opcode, candidate))


RR = Registers()

before = [3,2,1,1]
after = [3,2,2,1]
print(RR.how_many_opcodes(before, (9,2,1,2), after))

(blind_operations, intructions) = build_lists(get_elem_list())
print(blind_operations)

count= 0

opcode_candidates = {}
for i in range(16):
    opcode_candidates[i] = set()
    for opc in RR.opcodes:
        opcode_candidates[i].add(opc.__name__)

all_opcodes = set([opc.__name__ for opc in RR.opcodes])


for operation in blind_operations:
    (nb, opcode_candidate) = RR.how_many_opcodes(operation[0], operation[1], operation[2])
    if nb>=3:
        count += 1
    (opc, candidates) = opcode_candidate
    candidates = set(candidates)
    to_remove = all_opcodes.difference(candidates)
    opcode_candidates[opc].difference_update(to_remove)

for opc in opcode_candidates:
    print(opc, opcode_candidates[opc])

RR.set_registers([0, 0, 0, 0])

for instruction in intructions:
    RR.apply_instruction(instruction)
print(RR.registers)