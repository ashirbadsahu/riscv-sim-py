memory = [0] * 256# memory from locations 0 to 255
# print(memory)

reg = {
    "x0": 0, # x0 is hardwired to 0
    "x1": 0,
    "x2": 0,
    "x3": 0,
    "x4": 0,
    "x5": 0,
    "x6": 0,
    "x7": 0,
}
pc = 0

def execute_add(rd, rs1, rs2):
    """
    adds the values in rs1 and rs2 and stores the result in rd
    """
    if rd == "x0":
        return

    val_rs1 = reg[rs1]
    val_rs2 = reg[rs2]
    result = val_rs1 + val_rs2
    reg[rd] = result
    print(f"adding {val_rs1}, {val_rs2} and storing the result {result} in {rd}")

def execute_lw(rd, rs1):
    """
    loads a value from memory address rs1 to register rd
    """
    if rd == "x0":
        return
    address = reg[rs1]
    if 0 <= address < len(memory):
        loaded_value = memory[address]
        print(f"Loading value {loaded_value} from memory address {address} to register {rd}")
        reg[rd] = loaded_value
    else:
        print(f"memory access error: address {address} out of bounds!")

def execute_beq(rs1, rs2, offset):
    """
    if the values in rs1 and rs2 are equal, then branch to pc + offset
    """
    val_rs1 = reg[rs1]
    val_rs2 = reg[rs2]

    if val_rs1 == val_rs2:
        global pc
        pc = pc + offset
        print(f"BEQ {rs1}, {rs2}, {offset} - branch taken to PC: {pc}")
    else:
        print(f"BEQ {rs1}, {rs2}, {offset} - branch not taken")
        pass

"""
instruction encoding format:
this instruction encoding format is a simple one and is not used in any real-world processor and i made it up just for the sake of simplicity.

example instruction: 11233
opcode: 1
rd: 1
rs1: 2
rs2: 3
offset: 3
"""
def decode_instruction(instruction):
    """
    decodes the instruction into opcode, rd, rs1, rs2, and offset
    """
    opcode = instruction // 10000
    rd = (instruction // 1000) % 10
    rs1 = (instruction // 100) % 10
    rs2 = (instruction // 10) % 10
    offset = instruction % 10
    return opcode, rd, rs1, rs2, offset

def fetch_decode_execute():
    """
    fetches the instruction from memory, decodes it, and executes it
    """
    global pc
    instruction_count = 0
    instruction_limit = 3

    while pc < len(memory) and instruction_count < instruction_limit:
        instruction = memory[pc]
        print(f"accessing memory[{pc}]")
        opcode, rd, rs1, rs2, offset = decode_instruction(instruction)

        if opcode == 1:
            execute_add(f"x{rd}", f"x{rs1}", f"x{rs2}")
        elif opcode == 2:
            execute_lw(f"x{rd}", f"x{rs1}")
        elif opcode == 3:
            execute_beq(f"x{rs1}", f"x{rs2}", offset)
        pc += 1
        instruction_count += 1