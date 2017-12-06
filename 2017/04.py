c = 0
with open('.04') as f:
    for line in f:
        words = {}
        for word in line.split():
            try:
                words[''.join(sorted(word))]
                break
            except:
                words[''.join(sorted(word))] = 1
        else:
            c += 1
print(c)
