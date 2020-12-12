# the index into the memory array, aka location, address, pointer

# 1 - PRINT_HELLO
# 2 - HALT
# 3 - SAVE_REG store a val in a register
# 4 - PRINT_REG print the register val in decimal

ram = [  # think of as a big arrary of bytes, 8-bits per bytes
    1,  # PRINT_HELLO
    #
    3,  # SAVE_REG r4 37 are instruction itself, also called "opcode"
    4,  # 4 & 37 are args to SAVE_REG, also called "operands"
    37,
    #
    4,  # PRINT_REG r4
    4,
    #
    2,  # HALT
]

reg = [0] * 8

running = True

# keeps track of where we are
pc = 0  # program counter, the index into memory of the currently-executing instruction

while running:
    ir = ram[pc]  # instruction register

    if ir == 1:  # PRINT_HELLO
        print("HELLO")
        pc += 1  # 1 byte instruction

    elif ir == 2:  # HALT
        running = False
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
