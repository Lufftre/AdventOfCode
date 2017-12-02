from string import ascii_lowercase
idsum = 0

with open('4.input', 'r') as f:
	for line in f:
		hej, svejs = line.rsplit('-', 1)
		tja = {}
		for c in hej.replace('-',''):
			tja[c] = tja.get(c, 0) - 1

		sector, checksum = svejs.replace(']','[').split('[')[:-1]
		try:
			for i, j in enumerate(sorted(tja.items(), key=lambda x: (x[1],x[0]))):
					if checksum[i] != j[0]:
						break
		except IndexError:
			idsum += int(sector)
			secret = ''.join([ascii_lowercase[(ascii_lowercase.find(c)+int(sector))%26] if c != '-' else ' ' for c in hej])
			if 'north' in secret:
				print(sector)

print(idsum)