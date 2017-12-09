with open('.06') as f:
    memory = [int(cell) for cell in f.read().split()]

history = []
c = 0
while tuple(memory) not in history:
    history.append(tuple(memory))
    i_max, val_max = max(enumerate(memory), key=lambda k: k[1])
    memory[i_max] = 0
    for i in range(i_max + 1, i_max + val_max + 1):
        memory[i%len(memory)] += 1
    c += 1
print(c, c - history.index(tuple(memory)))