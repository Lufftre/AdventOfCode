import re

regex = r'a ([A-z -]+)'

def get_house():
	with open('11.input', 'r') as f:
		house = [[(x.split()[0][0]+x.split()[1][0]).upper() for x in re.findall(regex, line)] for line in f]
	return house

def show_house(house, elev):
	elems = sorted(sum(house, []))
	for i, floor in enumerate(house[::-1]):
		print('F%d'%(len(house)-i), end=" ")
		if 3-i == elev:
			s = 'E '
		else:
			s = '  '
		print(s, end="")
		for elem in elems:
			if elem in floor:
				s = elem
			else:
				s = '..'
			print(s, end=" ")
		print()


house = get_house()
elev = 0
paths = 

show_house(house, elev)