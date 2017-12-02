ips = []
with open('7.input', 'r') as f:
	for line in f:
		hypernet = False
		abba = False
		for i in range(len(line.strip()) - 3 ):
			if line[i+3] == '[':
				hypernet = True
			if line[i] == ']':
				hypernet = False
			if line[i] == line[i+3] and line[i+1] == line[i+2] and line[i] != line[i+1]:
				if hypernet:
					abba = False
					break
				else:
					abba = True

		if abba:
			ips += [line.strip()]
print(len(ips))


import re
with open('7.input', 'r') as f:
	for line in f:
		line = re.split(r'[\[\]]', line.strip())
		print(line)