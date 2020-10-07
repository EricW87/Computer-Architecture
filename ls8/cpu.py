"""CPU functionality."""

import sys
HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0B10100010
class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8
        self.reg[7] = 0xF4
        self.ram = [0] * 256
        self.pc = 0
        self.halted = False

    def ram_read(self, address):
        return self.ram[address]

    def ram_write():
        self.ram[address] = val
    
    def load(self):
        """Load a program into memory."""
        if len(sys.argv) != 2:
            print("Not enough arguments")
            sys.exit(1)
            

        fname = sys.argv[1]      
        address = 0
        # For now, we've just hardcoded a program:
        try:
            with open(fname) as f:
                for l in f: #for every line in file f
                    instruction = ""
                    for c in l: #for every character in the line
                        if c == '0' or c == '1':
                            instruction += c
                        else:
                            break

                    if len(instruction) > 0:
                        #print(instruction, int(instruction, 2))
                        self.ram[address] = int(instruction, 2)
                        address += 1
        except:
            print("File not found")
            sys.exit(1)

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()



    def run(self):
        """Run the CPU."""
        while not self.halted:
            instruction_to_execute = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            self.execute_instruction(instruction_to_execute, operand_a, operand_b)

    def execute_instruction(self, instruction, operand_a, operand_b):
        if instruction == HLT:
            self.halted = True
            #self.pc += 1
        elif instruction == LDI:
            self.reg[operand_a] = operand_b
            #self.pc += 3
        elif instruction == PRN:
            print(self.reg[operand_a])
            #self.pc += 2
        elif instruction == MUL:
            self.alu("MUL", operand_a, operand_b)
            #self.pc += 3

        instruction = instruction >> 6
        #print(bin(instruction), instruction)
        self.pc += 1 + instruction
