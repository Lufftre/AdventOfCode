ops = {
    '^': (lambda x: (x[0],x[1]+1)),
    'v': (lambda x: (x[0],x[1]-1)),
    '>': (lambda x: (x[0]+1,x[1])),
    '<': (lambda x: (x[0]-1,x[1])),
}

def part1():
    with open('.day3') as f:
        pos = (0,0)
        visited = {pos: 1}
        for c in next(f):
            pos = ops[c](pos)
            visited[pos] = visited.get(pos, 0) + 1
        return len(visited)


def part2():
    with open('.day3') as f:
        pos = [0,0,0,0]
        visited = {tuple(pos[:2]): 1}
        while True:
            op = f.read(1)
            if not op:
                return len(visited)
            offset = 2*(f.tell()%2)
            pos[offset:offset+2] = ops[op](pos[offset:offset+2])
            visited[tuple(pos[offset:offset+2])] = visited.get(tuple(pos[offset:offset+2]), 0) + 1


print( part1() )
print( part2() )
