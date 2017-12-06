with open('.05') as f:
    jumps = [int(line) for line in f]

i = 0
c = 0
try:
    while True:
        if jumps[i] >= 3:
            bla = -1
        else:
            bla = 1
        jumps[i] += bla
        i = i + jumps[i] - bla
        c += 1
    
except:
    print(c)