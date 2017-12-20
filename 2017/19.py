import string
grid = []
with open('.19') as f:
    for y, line in enumerate(f):
        d = {}
        for x, c in enumerate(line.rstrip()):    
            if c != ' ':
                d[x] = c
        grid.append(d)


x_, y_ = list(grid[0].keys())[0], -1
x, y = list(grid[0].keys())[0], 0
c = 0
while True:
    if x == 0:
        print()
        break
    if grid[y].get(x) in string.ascii_uppercase:
        print(grid[y].get(x), end='')
    xx = 2*x - x_
    yy = 2*y - y_

    if not grid[yy].get(xx):
        xx = x + (y - y_)
        yy = y + (x - x_)
        if not grid[yy].get(xx):
            xx = x - (y - y_)
            yy = y - (x - x_)
    x_, y_ = x, y
    x, y = xx, yy
    c += 1
print(c)