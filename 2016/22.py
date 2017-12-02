import re

def count_pairs():
	with open('22.input') as fp:
		data = [line.split() for line in fp]

	pairs = []
	for i,(name1, size1, used1, avail1, use1) in enumerate(data):
		for j,(name2, size2, used2, avail2, use2) in enumerate(data):
			if i == j:
				continue
			if int(use1[:-1]) == 0:
				continue
			if int(used1[:-1]) <= int(avail2[:-1]):
				pairs.append((i,j))

	print(len(pairs))


regex = re.compile(r'/dev/grid/node-x(\d+)-y(\d+)')

grid = []
with open('22.input') as fp:
	for line in fp:
		node, size, used, avail, use = line.split()
		x, y = [int(n) for n in regex.match(node).groups()]
		if y == 0:
			grid.append([])
		grid[x].append( ((x,y), int(size[:-1]), int(used[:-1]), int(avail[:-1])) )


cur = (35,0)
for y in range(len(grid[0])):
	for x in range(len(grid)):
		pos, size, used, avail = grid[x][y]
		if pos == cur:
			s = '💾'
		elif used > 100:
			s = '🚧'
		elif used == 0:
			s = '🚣'
		else:
			s = '🌊'
		print(s, end=' ')
	print()