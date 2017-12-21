import sys
import time
from queue import Queue
import threading

class Computer(object):
    def __init__(self):
        self.pc = 0
        self.registers = {}

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


    def jgz(self, reg, x):
        if int(self.registers.get(reg, reg)) > 0:
            self.pc += int(self.registers.get(x, x))
        else:
            self.pc += 1
    
    def snd(self, reg):
        self.registers['sound'] = self.registers[reg]
        self.pc += 1

    def rcv(self, reg):
        if self.registers.get(reg):
            print('RECIEVE:', self.registers['sound'])
            raise StopIteration
        self.pc += 1

class Computer2(Computer):
    queues = [Queue(), Queue()]

    def __init__(self, id):
        super().__init__()
        self.id = id
        self.registers['p'] = id
        self.snd_counter = 0

    def snd(self, x):
        self.snd_counter += 1
        self.queues[(self.id + 1) % 2].put(int(self.registers.get(x, x)))
        # 

        print('\033[{}BSent: {}'.format(self.id, self.snd_counter), end='\r\033[{}A'.format(self.id), flush=True)
        self.pc += 1
    
    def rcv(self, reg):
        self.registers[reg] = self.queues[self.id].get()
        self.pc += 1

def run(computer):
    instructions = [line.strip().split(maxsplit=1) for line in open('.18')]
    while computer.pc < len(instructions):
        op, params = instructions[computer.pc]
        getattr(computer, op)(*params.split())

def part1():
    run(Computer())

def part2():
    t = threading.Thread(target=run, args=(Computer2(id=1),))
    t.start()
    run(Computer2(id=0))


if __name__ == '__main__':
    try:
        part1()
    except StopIteration:
        part2()
