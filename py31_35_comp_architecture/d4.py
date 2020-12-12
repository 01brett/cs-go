import sys

PRINT_HELLO = 1
HALT = 2
SAVE_REG = 3
PRINT_REG = 4
PUSH = 5
POP = 6
CALL = 7
RET = 8

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


def push_val(value):
    # decrement stack pointer
    reg[SP] -= 1
    # copy value onto the stack
    top_stack_addr = reg[SP]
    ram[top_stack_addr] = value


def pop_val():
    # get val from top of stack
    top_stack_addr = reg[SP]
    value = ram[top_stack_addr]  # wanna put this in a register
    # increment the stack pointer
    reg[SP] += 1
    return value


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
        reg[SP] -= 1
        reg_num = operand_a
        val = reg[reg_num]
        top_stack_addr = reg[SP]
        ram[top_stack_addr] = val
        pc += 2

    elif ir == POP:
        top_stack_addr = reg[SP]
        val = ram[top_stack_addr]
        reg_num = operand_a
        reg[reg_num] = val
        reg[SP] += 1
        pc += 2

    elif ir == CALL:
        # get addr of the next instruction after the CALL
        return_addr = pc + 2
        # push it onto the stack
        push_val(return_addr)
        # get subroutine address from register
        subroutine_addr = reg[pc + 1]
        # jump to it
        pc = subroutine_addr

    elif ir == RET:
        # get return addr from top of stack
        return_addr = pop_val()
        # store it in the pc
        pc = return_addr

    else:
        print(f"Unknown op_code: {ir} at address: {pc}")
        sys.exit()