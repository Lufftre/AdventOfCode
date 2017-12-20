from w8m8 import w8m8
import string
line = [c for c in string.ascii_lowercase[:16]]
moves = [(move[0], move[1:].split('/')) for move in open('.16').read().split(',')]

def spin(line, x):
    return line[-x:] + line[:-x]

def exchange(line, a, b):
    tmp = line[b]
    line[b] = line[a]
    line[a] = tmp
    return line

def partner(line, a, b):
    idx_a = line.index(a)
    idx_b = line.index(b)
    line[idx_a] = b
    line[idx_b] = a
    return line


for move in moves:
    if move[0] == 's':
        line = spin(line, int(move[1][0]))
    elif move[0] == 'x':
        line = exchange(line, *map(int, move[1]))
    elif move[0] == 'p':
        line = partner(line, *move[1])
print(''.join(line))

line = [c for c in string.ascii_lowercase[:16]]
seen_lines = []
for i in range(1000000000):

    str_line = ''.join(line)
    if str_line in seen_lines:
        print(seen_lines[1000000000 % i])
        1/0
    seen_lines.append(str_line)

    for move in moves:
        if move[0] == 's':
            line = spin(line, int(move[1][0]))
        elif move[0] == 'x':
            line = exchange(line, *map(int, move[1]))
        elif move[0] == 'p':
            line = partner(line, *move[1])
print(''.join(line))
