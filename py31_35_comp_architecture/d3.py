import sys

PRINT_HELLO = 1
HALT = 2
SAVE_REG = 3
PRINT_REG = 4
PUSH = 5
POP = 6

ram = [0] * 256
reg = [0] * 8

SP = 7
reg[SP] = 0xF4  # stack pointer

address = 0

if len(sys.argv) != 2:
    print("Usage: day3.py prog_name")
    sys.exit()


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
sp = len(ram) - 1
pc = 0

while not halted:
    ir = ram[pc]
    operand_a = ram[pc + 1]
    operand_b = ram[pc + 2]

    if ir == PRINT_HELLO:
        print("HELLO")
        pc += 1

    elif ir == HALT:
        halted = True
        pc += 1

    elif ir == SAVE_REG:
        reg_num = operand_a
        reg_val = operand_b
        reg[reg_num] = reg_val
        pc += 3

    elif ir == PRINT_REG:
        reg_num = operand_a
        print(reg[reg_num])
        pc += 2

    elif ir == PUSH:
        # decrement stack pointer
        reg[SP] -= 1
        # grab val out of the given register
        reg_num = operand_a
        # this is what we want to push
        val = reg[reg_num]
        # copy val onto the stack
        top_stack_addr = reg[SP]
        ram[top_stack_addr] = val

        pc += 2
        # print(ram[0xF0:0xF4])  # visual of our stack for troubleshooting

    elif ir == POP:
        # get val from top of stack
        top_stack_addr = reg[SP]
        # this is what we want to put in a register
        val = ram[top_stack_addr]
        # store in register
        reg_num = operand_a
        reg[reg_num] = val
        # increment stack pointer
        reg[SP] += 1

        pc += 2

    else:
        print(f"Unknown op_code: {ir} at address: {pc}")
        sys.exit()