import hashlib
import re

keys = []
salt = 'zpqevtbw'
i = 0
while True:
	s = hashlib.md5(("%s%d"%(salt,i)).encode('utf-8')).hexdigest()
	i+=1
	for ii in range(32 - 2):
		if s[ii] == s[ii+1] and s[ii] == s[ii+2]:
			triplet = s[ii]
			break
	else:
		continue
	for j in range(1000):
		s = hashlib.md5(("%s%d"%(salt,i+j)).encode('utf-8')).hexdigest()
		m = re.search(triplet*5, s)
		if m:
			break
	else:
		continue
	print(triplet)
	keys.append(triplet)
	if len(keys) == 64:
		print(i-1)
		break

