from math import inf
lines = open("16.test").read().splitlines()
grid = []
for y,r in enumerate(lines):
    row = []
    for x, c in enumerate(r):
        if c == "S":
            start = (x,y)
        elif c == "E":
            end = (x,y)
        row.append(c)
    grid.append(row)


def draw(grid):
    for r in grid:
        for c in r:
            print(c, end=" ")
        print()
draw(grid)


def get_neighbours(grid, pos, current_dir):
    ns = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if (current_dir[0]*-1, current_dir[1]*-1) == (dx, dy):
            continue
        xx = pos[0] + dx
        yy = pos[1] + dy
        if current_dir == (dx, dy):
            s = 1
        else:
            s = 1001

        if grid[yy][xx] != "#":
            ns.append(((xx, yy), s, (dx, dy)))
    return ns

def search(grid, start):
    scores = {}
    frontier = [(start, 0, (1,0))]
    while len(frontier):
        pos, score, cur_dir = frontier.pop()
        scores[(pos, cur_dir)] = min(scores.get((pos, cur_dir), inf))
        ns = get_neighbours(grid, pos, cur_dir)
        for n in ns:
            frontier.append(n)
