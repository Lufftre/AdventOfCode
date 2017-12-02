def part1():
    with open('.day2') as f:
        tot = 0
        for line in f:
            dims = [int(x) for x in line.split('x')]
            sides = [dims[i]*dims[i-1] for i in range(3)]
            tot += sum(sides)*2 + min(sides)
        return tot
        #return sum([min(x) + sum(x*2) for x in [[int(line.split('x')[i])*int(line.split('x')[i-1]) for i in range(3)] for line in f]])

def part2():
    with open('.day2') as f:
        tot = 0
        for line in f:
            a,b,c = sorted([int(x) for x in line.split('x')])
            tot += 2*a + 2*b + a*b*c
        return tot

print( part1() )
print( part2() )
