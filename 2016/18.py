import time
with open('18.input', 'r') as f:
	row = [c=='.' for c in '.'+f.read()+'.']

t0 = time.time()
l = range(1, len(row)-1)
c = sum(row) - 2
for i in range(400000-1):
	row = [True] + [not(row[j-1]!=row[j+1]) for j in l] + [True]
	c += sum(row)
print(c - 2*(400000-1))
t = time.time() - t0
print(t)



