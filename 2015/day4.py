import hashlib
with open('.day4') as f:
    puzzle_input = f.read()

def part1():
    c = 1
    while int(hashlib.md5(('%s%d'%(puzzle_input,c)).encode()).hexdigest()[:5], 16):
        c+=1
    return c


def part2():
    c = 1
    while int(hashlib.md5(('%s%d'%(puzzle_input,c)).encode()).hexdigest()[:6], 16):
        c+=1
    return c


print( part1() )
print( part2() )
