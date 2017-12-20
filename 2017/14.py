
knot = __import__('10').knot
puzzle = 'hxtvlmkl'


grid = []
for i in range(128): 
    row = knot('{}-{}'.format(puzzle, i))
    grid.append([c for c in bin(int(row, 16))[2:].zfill(128).replace('0','.').replace('1','#')])

squares = sum([row.count('#') for row in grid])
print(squares)

def get_bois(x, y):
    # for i in range(128):
    #     for j in range(128):
    #         print(grid[i][j], end='')
    #     print()
    grid[y][x] = groups
    if x > 0 and grid[y][x-1] == '#':
        get_bois(x-1, y)
    if x < 127 and grid[y][x+1] == '#':
        get_bois(x+1, y)
    if y > 0 and grid[y-1][x] == '#':
        get_bois(x, y-1)
    if y < 127 and grid[y+1][x] == '#':
        get_bois(x, y+1)
    
    
    
groups = 0
for y in range(128):
    for x in range(128):
        if grid[y][x] == '#':
            get_bois(x,y)
            groups += 1
print(groups)