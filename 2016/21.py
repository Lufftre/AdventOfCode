import itertools
import re

r0 = r'swap position (\d+) with position (\d+)'
r1 = r'swap letter (\w+) with letter (\w+)'
r2 = r'reverse positions (\d+) through (\d+)'
r3 = r'rotate (\w+) (\d+) steps?'
r4 = r'move position (\d+) to position (\d+)'
r5 = r'rotate based on position of letter (\w+)'


def swap_pos(pw, p1, p2):
	p1, p2 = sorted([int(p1), int(p2)])
	pw = pw[:p1] + pw[p2] + pw[p1+1:p2] + pw[p1] + pw[p2+1:]
	return pw

def swap_letter(pw, c1, c2):
	p1 = pw.find(c1)
	p2 = pw.find(c2)
	return swap_pos(pw, p1, p2)

def reverse_pos(pw, p1, p2):
	p1, p2 = sorted([int(p1), int(p2)])
	pw = pw[:p1] + pw[p2:p1:-1] + pw[p1] + pw[p2+1:]
	return pw

def rotate_step(pw, direction, steps):
	steps = int(steps) % len(pw)
	if direction == 'right':
		steps *= -1
	pw = pw[steps:] + pw[:steps]
	return pw 

def move(pw, p1, p2):
	p1, p2 = [int(p1), int(p2)]
	l = [c for c in pw]
	l.insert(p2, l.pop(p1))
	pw = ''.join(l)
	return pw

def rotate_letter(pw, c):
	steps =  pw.find(c) + 1
	if steps > 4:
		steps += 1
	pw = rotate_step(pw, 'right', steps)
	return pw

regexs = {
r0 : swap_pos,
r1 : swap_letter,
r2 : reverse_pos,
r3 : rotate_step,
r4 : move,
r5 : rotate_letter
}


def solve1(pw="abcdefgh"):
	with open('21.input', 'r') as f:

		for line in f:
			for regex, func in regexs.items():
				match = re.match(regex, line)
				if match:
					pw = func(pw, *match.groups())
					break
			else:
				1/0
	return pw

def solve2():
	goal = "fbgdceah"
	for pw in itertools.permutations([c for c in goal]):
		pw = ''.join(pw)
		if solve1(pw) == goal:
			return pw


print(solve1())
print(solve2())
	


