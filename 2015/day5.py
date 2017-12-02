def is_nice(line):
    vowels = 0
    doubels = False
    baddies = False

    for i in range(len(line) - 1):
        if line[i] in 'aeiou':
            vowels += 1
        if line[i] == line[i + 1]:
            doubels = True
        if line[i] + line[i + 1] in ('ab', 'cd', 'pq', 'xy'):
            baddies = True

    return vowels >= 3 and doubels and not baddies

def is_nice2(line):
    pair = False
    repeat = False

    for i in range(len(line) - 2):
        if line[i:i+2] in line[i+2:]:
            pair = True
        if line[i] == line[i + 2]:
            repeat = True

    return pair and repeat

def part1():
    with open('.day5') as f:
        return sum([is_nice(line) for line in f])

def part2():
    with open('.day5') as f:
        return sum([is_nice2(line) for line in f])

print( part1() )
print( part2() )
