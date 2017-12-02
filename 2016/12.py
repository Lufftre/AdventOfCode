import sys

with open('12.input', 'r') as f:
	pm = [line.strip() for line in f]

i = 0
reg = {
	'a' : 0,
	'b' : 0,
	'c' : 1,
	'd' : 0,
}

#print(reg)
def cpy(x, y):
	global i
	reg[y] = reg.get(x) if x in reg else int(x)
	i += 1

def inc(x):
	global i
	reg[x] += 1
	i += 1

def dec(x):
	global i
	reg[x] -= 1
	i += 1

def jnz(x, y):
	global i
	if reg.get(x) if x in reg else int(x):
		i += int(y)
	else:
		i += 1
c = 0
while i < len(pm):
	op, args = pm[i].split(' ', 1)
	getattr(sys.modules[__name__], op)(*args.split())
	if c % 100 == 0:
		print(reg)
	c += 1
print(reg)
