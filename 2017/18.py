import sys
import time
from queue import Queue
import threading
# name = sys.argv[1]
# conn = sys.argv[2]

queues = [Queue(), Queue()]
class Computer(object):
    def __init__(self, queues, id):
        self.queues = queues
        self.pc = 0
        self.id = id
        self.registers = {'p': id}
        self.snd_counter = 0
    def set(self, reg, x):
        self.registers[reg] = int(self.registers.get(x, x))
        self.pc += 1

    def add(self, reg, x):
        self.registers[reg] = self.registers.get(reg, 0) + int(self.registers.get(x, x))
        self.pc += 1

    def mul(self, reg, x):
        self.registers[reg] = self.registers.get(reg, 0) * int(self.registers.get(x, x))
        self.pc += 1

    def mod(self, reg, x):
        self.registers[reg] = self.registers.get(reg, 0) % int(self.registers.get(x, x))
        self.pc += 1

    # def snd(self, reg):
    #     self.registers['sound'] = self.registers[reg]
    #     self.pc += 1

    # def rcv(self, reg):
    #     if self.registers.get(reg):
    #         print(__name__, 'RECIEVE:', self.registers['sound'])
    #         1/0
    #     self.pc += 1

    def jgz(self, reg, x):
        if int(self.registers.get(reg, reg)) > 0:
            self.pc += int(self.registers.get(x, x))
        else:
            self.pc += 1
    
    def snd(self, x):
        self.snd_counter += 1
        self.queues[(self.id + 1) % 2].put(int(self.registers.get(x, x)))
        print(self.id, self.snd_counter)
        self.pc += 1
    
    def rcv(self, reg):
        #print(self.registers)
        self.registers[reg] = self.queues[self.id].get()
        self.pc += 1

def run(queues, id):
    instructions = [line.strip().split(maxsplit=1) for line in open('.18')]
    computer = Computer(queues, id)
    while computer.pc < len(instructions):
        op, params = instructions[computer.pc]
        getattr(computer, op)(*params.split())

if __name__ == '__main__':
    t = threading.Thread(target=run, args=(queues,1))
    t.start()
    run(queues, 0)