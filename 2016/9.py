def p1():
	s = ''
	with open('9.input', 'r') as f:
		for line in f:
			while line:
				l = line.split(')', 1)
				if len(l)==2:
					hm, tail = l
					head, marker = hm.rsplit('(')
					a, b = [int(x) for x in marker.split('x')]
					s += head
					s += tail[:a]*b
					line = tail[a:]
				else:
					s += l[0]
					line = None
	s = s.strip().replace(' ', '')
	print(s)
	print(len(s))


size = 0
with open('9.input', 'r') as f:
	data = f.read()

print(data)
size = 0
while True:
	l = data.split(')', 1)
	if len(l)==2:
		hm, tail = l
		head, marker = hm.rsplit('(')
		a, b = [int(x) for x in marker.split('x')]
		size += len(head)
	else:
		size += len(data)
		break
	data = tail[:a]*b + tail[a:]
	print(size)
print(size)