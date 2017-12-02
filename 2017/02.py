with open('.02.input') as f:
    print(sum([b-a for a,b in [sorted([int(cell) for cell in row.split()])[::15] for row in f]]))

def kvot(cells):
    for i in range(len(cells)):
        for j in range(i + 1, len(cells)):
            if not cells[i] % cells[j]:
                return cells[i] // cells[j]
with open('.02.input') as f:
    print(sum([kvot(sorted([int(cell) for cell in row.split()], reverse=True)) for row in f]))


        
