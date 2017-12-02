msg = []
with open('6.input', 'r') as f:
	for line in f:
		if not msg:
			msg = [c for c in line.strip()]
		else:
			for i,c in enumerate(line.strip()):
				msg[i] += c

decrypt = ''
decrypt2 = ''
for letters in msg:
	tja = {}
	for c in letters:
		tja[c] = tja.get(c, 0) - 1
	decrypt += sorted(tja.items(), key=lambda x: x[1])[0][0]
	decrypt2 += sorted(tja.items(), key=lambda x: x[1], reverse=True)[0][0]

print(decrypt)
print(decrypt2)