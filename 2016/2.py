
pos1 = [2,2]
grid1 = [
[0,0,0,0,0],
[0,1,2,3,0],
[0,4,5,6,0],
[0,7,8,9,0],
[0,0,0,0,0],
]

pos2 = [1,3]
grid2 = [
[0,0,0,0,0,0,0],
[0,0,0,1,0,0,0],
[0,0,2,3,4,0,0],
[0,5,6,7,8,9,0],
[0,0,'A','B','C',0,0],
[0,0,0,'D',0,0,0],
[0,0,0,0,0,0,0]
]

grid = grid2
pos = pos2

hej = {'R' : (1,0), 'L':(-1,0), 'U':(0,-1), 'D':(0,1)}


with open('2.input', 'r') as f:
	for line in f.readlines():
		for op in line:
			if op == '\n':
				break
			if grid[pos[0]+hej.get(op)[0]][pos[1]+hej.get(op)[1]] != 0:
				pos[0] += hej.get(op)[0]
				pos[1] += hej.get(op)[1]

		print(grid[pos[1]][pos[0]])