with open('.11') as f:
    moves = [move for move in f.read().split(',')]

pos = (0,0)
steps = {
    'n': (-1, 1),
    'ne': (0, 1),
    'se': (1, 0),
    's': (1, -1),
    'sw': (0, -1),
    'nw': (-1, 0),
}
far_away = 0
for move in moves:
    pos = [sum(x) for x in zip(pos, steps.get(move))]
    far_away = max(map(abs, pos)) if max(map(abs, pos)) > far_away else far_away

print(max(map(abs, pos)))
print(far_away)