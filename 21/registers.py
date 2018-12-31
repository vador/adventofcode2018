
def get_elem_list():
    elem_list = []
    file = open('input', 'r')
    for line in file:
        elem_list.append(line.rstrip('\n'))
    return elem_list

def get_instruction_list(elem_list):
    ip = int(elem_list.pop(0)[4:])
    operand_list = []
    for elem in elem_list:
        (operand, A, B, C) = elem.split(" ")
        A = int(A)
        B = int(B)
        C = int(C)
        operand_list.append((operand, A, B, C))
    return (ip, operand_list)


class Registers:
    registers = None
    intructions = None
    ip = None
    ipVal = None

    def __init__(self, ip):
        self.registers = [0, 0, 0, 0, 0, 0]
        self.intructions = {}
        self.ip = ip
        self.ipVal = 0


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
        (operand, A, B, C) = instruction
        getattr(self, operand)(A,B,C)

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

    def run(self, instruction_list, debug=False, stop = -1):
        last_instruction = len(instruction_list)
        while self.ipVal<last_instruction:
            if self.ipVal == 28:
                print("Hello")
            self.registers[ip] = self.ipVal
            if debug==True:
                print("ip=", self.registers[ip],self.registers, instruction_list[self.registers[ip]], end='')
            self.apply_instruction(instruction_list[self.registers[ip]])
            if debug == True:
                print(self.registers)
            self.ipVal = self.registers[ip]
            self.ipVal += 1

(ip, instruction_list) = get_instruction_list(get_elem_list())


RR = Registers(ip)
RR.registers[0]=10504829
RR.run(instruction_list, debug=False, stop=28)