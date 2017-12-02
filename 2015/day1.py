def part1():
    with open('.day1') as f:
        return 2*f.read().count('(') - f.tell()

def part2():
    counter = []
    with open('.day1') as f:
        while True:
            try:
                if f.read(1) == '(':
                    counter += [0,0]
                counter.pop()
            except:
                return f.tell()

print( part1() )
print( part2() )
