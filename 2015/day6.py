import re
regex = re.compile(r'([a-z]+ ?[a-z]*) (\d+),(\d+) through (\d+),(\d+)')

def control1(op, grid, x, y):
    if op == 'turn on':
        val = True
    if op == 'turn off':
        val = False
    if op == 'toggle':
        val = not grid.get((x,y), False)
    return val

def control2(op, grid, x, y):
    if op == 'turn on':
        val = grid.get((x,y), 0) + 1
    if op == 'turn off':
        cur = grid.get((x,y), 0)
        val = cur - 1 if cur > 0 else 0
    if op == 'toggle':
        val = grid.get((x,y), 0) + 2
    return val

def control_lights(controller):
    grid = {}
    with open('.day6') as f:
        for line in f:
            data = regex.match(line).groups()
            op = data[0]
            x1, y1, x2, y2 = [int(x) for x in data[1:]]
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    grid[(x,y)] = controller(op, grid, x, y)
    return sum([value for key, value in grid.items()])

def part1():
    return control_lights(control1)

def part2():
    return control_lights(control2)

print( part1() )
print( part2() )
