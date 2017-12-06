with open('.06') as f:
    memory = [int(cell) for cell in f.read().split()]

history = []
c = 0
while True:
    if tuple(memory) in history:
        break

    history.append(tuple(memory))
    i_max = memory.index(max(memory))
    val_max = max(memory) 
    memory[i_max] = 0
    for i in range(i_max + 1, i_max + val_max + 1):
        memory[i%len(memory)] += 1
    c += 1
print(c, len(history) - history.index(tuple(memory)))