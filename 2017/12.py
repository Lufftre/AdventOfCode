village = {}
with open('.12') as f:
    for line in f:
        program, neighbours = [x.strip() for x in line.split('<->')]
        village[program] = [x.strip() for x in neighbours.split(',')]

visited = ['0']
def walk(node):
    for boi in village.get(node, []):
        if boi not in visited:
            visited.append(boi)
            walk(boi)

walk('0')
print(visited, len(visited))
groups = 1
for boi in village.keys():
    if boi not in visited:
        walk(boi)
        groups += 1
print(groups)