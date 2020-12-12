"""CPU functionality."""

import sys

"""Constants"""
SP = 7


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 7 + [0xF4]
        self.ram = [0] * 256
        self.pc = 0
        self.fl = 0b00000000  # 00000LGE
        self.halted = True
        self.disp = {
            0b00000000: self.nop,
            0b00000001: self.hlt,
            0b10000010: self.ldi,
            0b01000111: self.prn,
            0b10100000: self.add,
            0b10100111: self.compare,
            0b10100010: self.mul,
            0b01000101: self.push,
            0b01000110: self.pop,
            0b01010000: self.call,
            0b00010001: self.ret,
            0b10000100: self.st,
            0b01010100: self.jmp,
            0b01010101: self.jeq,
            0b01010110: self.jne,
        }

    def nop():
        pass

    def hlt(self):
        self.halted = True

    def jmp(self, reg_num):
        self.pc = self.reg[reg_num]

    def jne(self, reg_num):
        if self.fl != 0b00000001:
            self.jmp(reg_num)
        else:
            self.pc += 2

    def jeq(self, reg_num):
        if self.fl == 0b00000001:
            self.jmp(reg_num)
        else:
            self.pc += 2

    def compare(self, reg_a, reg_b):
        if self.reg[reg_a] < self.reg[reg_b]:
            # 00000L00
            self.fl = 0b00000100
        elif self.reg[reg_a] > self.reg[reg_b]:
            # 000000G0
            self.fl = 0b00000010
        else:
            # 0000000E
            self.fl = 0b00000001

    def ldi(self, reg_num, reg_val):
        self.reg[reg_num] = reg_val

    def prn(self, reg_num):
        print(self.reg[reg_num])

    def push(self, reg_num):
        self.reg[SP] -= 1
        value = self.reg[reg_num]
        top_stack_addr = self.reg[SP]
        self.ram[top_stack_addr] = value

    def pop(self, reg_num):
        top_stack_addr = self.reg[SP]
        value = self.ram[top_stack_addr]
        self.reg[reg_num] = value
        self.reg[SP] += 1

    def call(self, reg_num):
        # decrement stack pointer
        self.reg[SP] -= 1
        # copy value onto the stack
        top_stack_addr = self.reg[SP]
        # get addr of next instruct
        return_addr = self.pc + 2
        # push it onto the stack
        self.ram[top_stack_addr] = return_addr  # return_addr
        # get subroutine address from register
        subroutine_addr = self.reg[reg_num]
        # jump to it
        self.pc = subroutine_addr

    def ret(self):
        # get value from top of stack
        top_stack_addr = self.reg[SP]
        value = self.ram[top_stack_addr]
        self.reg[SP] += 1
        # return_address from top of stack
        return_addr = value
        # store addr in prog_counter
        self.pc = return_addr

    def add(self, reg_a, reg_b):
        self.reg[reg_a] += self.reg[reg_b]

    def mul(self, reg_a, reg_b):
        self.reg[reg_a] *= self.reg[reg_b]

    def st(self, reg_a, reg_b):
        addr = self.reg[reg_a]
        val = self.reg[reg_b]
        self.ram[addr] = val

    def load(self):
        """Load a program into memory."""

        if len(sys.argv) != 2:
            print("Usage: ls8.py prog_name")
            sys.exit()

        address = 0

        try:
            with open(sys.argv[1]) as f:
                for line in f:
                    line = line.strip()

                    if line == "" or line[0] == "#":
                        continue

                    str_val = line.split("#")[0]

                    try:
                        value = int(str_val, 2)
                    except ValueError:
                        print(f"Invalid number: {str_val}")
                        sys.exit()

                    self.ram[address] = value
                    address += 1

        except FileNotFoundError:
            print(f"File not found: {sys.argv[1]}")
            sys.exit()

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(
            f"pc: {self.pc:08b} fl: {self.fl:08b} | {self.ram_read(self.pc):08b} {self.ram_read(self.pc + 1):08b} {self.ram_read(self.pc + 2):08b} |",
            end="",
        )

        for i in range(8):
            print(" %02X" % self.reg[i], end="")

        print()

    def ram_write(self, value, address):
        self.ram[address] = value

    def ram_read(self, address):
        return self.ram[address]

    def run(self):
        """Run the CPU."""
        self.halted = False
        while not self.halted:
            # self.trace()
            ir = self.ram[self.pc]
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            # to be safe, use the bitwise `AND` to
            # mask bits we don't care about before right shift
            num_operands = (ir & 0b11000000) >> 6

            if num_operands == 0:
                self.disp[ir]()

            elif num_operands == 1:
                self.disp[ir](operand_a)

            elif num_operands == 2:
                self.disp[ir](operand_a, operand_b)

            else:
                print(f"Unknown op_code: {ir}")
                sys.exit()

            # check if opcode will set pc directly
            # using bitwise `AND` mask to filter extras
            sets_pc = (ir & 0b00010000) >> 4

            if not sets_pc:
                # add 1 for the op code
                instruction_len = num_operands + 1
                # increment the prog_counter dynamically
                self.pc += instruction_len
