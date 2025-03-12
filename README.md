# SIMPLE RISC-V SIMULATOR IN PYTHON
This project is a minimalist RISC-V instruction set simulator written in python. As of now it supports the following instructions:
- add
- lw
- beq
> Note: Instruction Encoding is not the same as RISC-V ISA. This is just a simple implementation for learning purpose.

## Instruction encoding format:
This instruction encoding format is a simple one and is not used in any real-world RISC-V processor and I made it up just for the sake of simplicity.

```
example instruction: 11233
opcode: 1
rd: 1
rs1: 2
rs2: 3
offset: 3
```

## Test Instructions:
```python
# add
memory[2] = 11230 # add x1, x2, x3
reg["x2"] = 5
reg["x3"] = 10

# lw
memory[50] = 123 # stores 123 at memory location 50
reg["x5"] = 50
memory[1] = 24500 # lw x4, (x5)


# beq
# reg["x1"] = 10
# reg["x2"] = 10
# memory[0] = 30122 # beq x1, x2, 2 (if x1==x2, branch to pc+2)

fetch_decode_execute()
print("Registers after execution:", reg)
print("memory after execution:", memory)
```