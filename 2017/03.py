square = 265149

x = 0
y = 0
counter = 0
cur_square = 1
grid = {(0,0) : 1}

def get_close_bois(x,y):
    return sum([grid.get((x+i,y+j), 0) for i in range(-1,2) for j in range(-1,2) if i or j])

while True:
    counter += 1
    
    for i in range(counter):
        if counter % 2:
            x += 1
        else:
            x -= 1
        # cur_square += 1
        cur_square = get_close_bois(x,y)
        grid[(x,y)] = cur_square
        #if cur_square == square:
        if cur_square > square:
            # print(abs(x) + abs(y))
            print(cur_square)
            1/0

    for i in range(counter):
        if counter % 2:
            y += 1
        else:
            y -= 1
        # cur_square += 1
        cur_square = get_close_bois(x,y)
        grid[(x,y)] = cur_square
        #if cur_square == square:
        if cur_square > square:
            # print(abs(x) + abs(y))
            print(cur_square)
            1/0