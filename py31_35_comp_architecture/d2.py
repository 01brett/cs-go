import sys

# the index into the memory array, aka location, address, pointer

# 1 - PRINT_HELLO
# 2 - HALT
# 3 - SAVE_REG store a val in a register
# 4 - PRINT_REG print the register val in decimal

# memory
ram = [0] * 256

# registers on our cpu
reg = [0] * 8

address = 0

if len(sys.argv) != 2:
    print("Usage: d2.py prog_name")
    sys.exit()

# error codes you pass to sys.exit() mean something to bash scripting
# sys.exit(0) successful error
# sys.exit(1) or 2 means something weird happened error

try:
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()

            if line == "" or line[0] == "#":
                continue

            str_val = line.split("#")[0]

            try:
                value = int(str_val, 10)
            except ValueError:
                print(f"Invalid number: {str_val}")
                sys.exit()

            ram[address] = value
            address += 1
except FileNotFoundError:
    print(f"File not found: {sys.argv[1]}")
    sys.exit()

halted = False

# keeps track of where we are
pc = 0  # program counter, the index into memory of the currently-executing instruction

while not halted:
    ir = ram[pc]  # instruction register

    if ir == 1:  # PRINT_HELLO
        print("HELLO")
        pc += 1  # 1 byte instruction

    elif ir == 2:  # HALT
        halted = True
        pc += 1  # 1 byte instruction

    elif ir == 3:  # SAVE_REG
        reg_num = ram[pc + 1]
        reg_val = ram[pc + 2]
        reg[reg_num] = reg_val
        pc += 3  # 3 byte instruction, so we increment by 3 (3 indexes in mem array)

    elif ir == 4:  # PRINT_REG
        reg_num = ram[pc + 1]
        print(reg[reg_num])
        pc += 2  # 2 byte instruction
