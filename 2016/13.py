def cost(pos, goal):
	return pos[2] + abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

locations = []
def is_wall(x, y):
	val = x*x + 3*x + 2*x*y + y + y*y + 1364
	wall = False
	for bit in bin(val)[2:]:
		if bit == '1':
			wall = not wall
	if not wall:
		locations.append((x,y))
	return wall

def main():
	start = (1, 1)
	goal = (31, 39)


	front = [(*start, 0)]
	visited = []
	while front:
		cur = front.pop(0)
		#print(cur[:2])
		if cur[:2] == goal:
			return cur
		for x in range(-1,2):
			for y in range(-1, 2):
				if cur[0]+ x < 0 or cur[1] + y < 0:
					continue
				#if cur[2] >= 50:
				#	continue
				if abs(x) == abs(y):
					continue
				if is_wall(cur[0]+x, cur[1]+y):
					continue
				new = (cur[0]+x, cur[1]+y, cur[2]+1)
				if new[:2] not in visited:
					front.append((*new, *cur))
		front.sort(key=lambda node: cost(node, goal))
		visited.append(cur[:2])

path = main()
s = set(locations)
print(s)
print(len(s))


path = [path[i-2:i] for i in range(len(path)-1, 2, -3)]
path.sort(key=lambda node: (node[1],node[0]))


cursor = [0,0]
for x,y in path:
	y_diff = y - cursor[1]
	cursor[1] += y_diff
	print('\n'*y_diff, end='')
	if y_diff: cursor[0] = 0
	x_diff = x - cursor[0]
	print(' '*(x_diff-1), end='')
	cursor[0] += x_diff
	print('#', end='')
print()
print(len(path))



