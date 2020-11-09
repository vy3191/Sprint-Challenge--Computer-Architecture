"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""
    
    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.register = [0] * 8
        self.pc = 0
        self.sp = 7

    def load(self, file_name):
        """Load a program into memory."""
        # address value for tracking the index of the ram memory
        address = 0
        with open(file_name) as f:
            for each_line in f:
                split_line = each_line.split('#')
                # grab the first element at the index 0 and trim the  space if any
                get_item_at_zero = split_line[0].strip()
              
                if get_item_at_zero == '':
                    continue
                # print(f'before integers>>>bin{get_item_at_zero}')
                self.ram[address] = int(get_item_at_zero, 2)               
                address += 1   
        # print(self.ram)  
        # For now, we've just hardcoded a program:
        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]
        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.register[reg_a] += self.register[reg_b]
        #elif op == "SUB": etc
        elif op == "MUL":
            return self.register[reg_a] * self.register[reg_b] # a = a * b  8 = 8 * 9

        else:
            raise Exception("Unsupported ALU operation")

    def multiply(self):
        mul_val = self.alu('MUL', self.ram_read(self.pc+1), self.ram_read(self.pc+2))   
        print(f'Multiplication value>>>>>>{mul_val}')  
        self.pc += 3

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

    def ram_read(self, index):
        return self.ram[index]   

    def ram_write(self, address, value):
        # return self.ram[address] = value
        pass
     

    def run(self):
        """Run the CPU."""
        running = True
        
        while running:
            # ir = self.ram[self.pc]   # ir=  _Instruction Register_.
            ir = self.ram_read(self.pc)
            # print(f'Printing all ir values{ir}')
            if ir ==  0b10000010: #LDI    index =0
                operand_a = self.ram_read(self.pc+1)  # index at 1
                operand_b = self.ram_read(self.pc+2)  # index at 2 this is the value gives (8)
                self.register[operand_a] = operand_b   # register[0] = 8
                self.pc += 3

            elif ir ==  0b00000001: #HLT  
                print('working for printing') 
                self.pc += 1  
                running = False
                       
            elif ir == 0b01000111:  # PRN    this is the index at 3 --->this should print
                operand_a = self.ram_read(self.pc+1)  # grab the next pc value in decimal
                print(f'Print 8 here>>>>>>>{self.register[operand_a]}')   # this should print 8
                self.pc += 2
            elif ir == 0b10000010: #LDI R1,9  
                operand_a1 = self.ram_read(self.pc+1)  # this is the index
                operand_b1 = self.ram_read(self.pc+2)  # this is the value 9 storing 
                self.register[operand_a1] = operand_b1
                self.pc += 3
                         
            elif ir == 0b10100010: # MUL R0,R1
                self.multiply()
                # # grab the indices
                # index_1 = self.ram_read(self.pc+1)
                # index_2 = self.ram_read(self.pc+2)
                # # get the value using indices
                # value_at_index_1 = self.register[index_1]
                # value_at_index_2 = self.register[index_2]
                # # multiply the value
                # mul_value = value_at_index_1 * value_at_index_2
                # # print the value now
                # print(f'The is multiplied value>>>>>{mul_value}')
                # self.pc += 3
            print(f'Register>>>>{self.register}')    






        
