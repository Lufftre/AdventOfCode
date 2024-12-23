from collections import Dict
from time import perf_counter
@value
struct Pos():
    var x: Int
    var y: Int

@value
struct Grid():
    var rows: Int
    var cols: Int
    var start: Pos
    var end: Pos
    var data: List[List[String]]

def init() -> Grid:
    map_str = open("input.txt", "r").read().splitlines()
    w, h = len(map_str[0]), len(map_str)
    grid = List[List[String]]()
    start = Pos(0,0)
    end = Pos(0,0)
    for y in range(h):
        r = List[String]()
        for x in range(w):
            c = map_str[y][x]
            if c == "S":
                start = Pos(x,y)
            if c == "E":
                end = Pos(x,y)
            r.append(c)
        grid.append(r)

    return Grid(h, w, start, end, grid)

fn get_neighbours(pos: Pos, grid: Grid) -> List[Pos]:
    ns = List[Pos]()
    xs = List(1, -1, 0, 0)
    ys = List(0, 0, 1, -1)
    for i in range(4):
        ns.append(Pos(pos.x + xs[i], pos.y + ys[i]))
    return ns

fn manhattan(pos: Pos, pos2: Pos) -> UInt:
    dx = pos.x - pos2.x
    dy = pos.y - pos2.y
    return abs(dx) + abs(dy)

fn search(grid: Grid) -> Dict[UInt, UInt]:
    pos = grid.start
    frontier = List((pos, 0))
    seen = Dict[UInt, UInt]()
    while len(frontier):
        pos, score = frontier.pop()
        i = pos.y * grid.cols + pos.x
        seen[i] = score
        ns = get_neighbours(pos, grid)
        for n in ns:
            xx = n[].x
            yy = n[].y
            ii = yy*grid.cols + xx
            c = grid.data[yy][xx]
            if c != "#" and ii not in seen:
                frontier.append((n[], score + 1))

    return seen

fn cheat(seen: Dict[UInt, UInt], grid: Grid) -> UInt:
    deltas = List[Int]()
    for key1 in seen:
        for key2 in seen:
            if key1 == key2:
                continue
            i1 = key1[]
            i2 = key2[]
            pos1 = Pos(i1 % grid.cols, i1 // grid.cols)
            pos2 = Pos(i2 % grid.cols, i2 // grid.cols)
            m = manhattan(pos1, pos2)
            if  m > 1 and m <= 20:
                try:
                    s = seen[i1]
                    s2 = seen[i2]
                except:
                    continue
                deltas.append(s2 - s - m)

    s = 0
    for d in deltas:
        if d[] >= 100:
            s += 1

    return s

fn cheat2(seen: Dict[UInt, UInt], grid: Grid) -> UInt:
    deltas = List[Int]()
    for key1 in seen:
        for x in range(-20, 21):
            for y in range(-20, 21):
                i1 = key1[]
                i2 = i1 + y*grid.cols + x
                if i2 not in seen:
                    continue
                pos1 = Pos(i1 % grid.cols, i1 // grid.cols)
                pos2 = Pos(i2 % grid.cols, i2 // grid.cols)
                m = manhattan(pos1, pos2)
                if  m > 1 and m <= 20:
                    try:
                        s = seen[i1]
                        s2 = seen[i2]
                    except:
                        continue
                    deltas.append(s2 - s - m)

    s = 0
    for d in deltas:
        if d[] >= 100:
            s += 1

    return s

def main():
    s0 = perf_counter()
    grid = init()
    seen = search(grid)
    s = cheat2(seen, grid)
    print(s)
    print((perf_counter() - s0) * 1000)
