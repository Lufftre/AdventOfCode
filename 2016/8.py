import re
import time
def print_screen(screen):
	print('{0}{1}{0}'.format('+', '-'*len(screen[0])))
	for row in screen:
		print('|', end='')
		for pixel in row:
			if pixel:
				print('#', end='')
			else:
				print(' ', end='')
		print('|')
	print('{0}{1}{0}'.format('+', '-'*len(screen[0])))

def rect(screen, a, b):
	for r in range(b):
		for c in range(a):
			screen[r][c] = True
	return screen

def rotate_col(screen, x, n):
	screen_t = list(zip(*screen))
	screen_t = rotate_row(screen_t, x, n)
	return [list(x) for x in zip(*screen_t)]

def rotate_row(screen, y, n):
	v = list(screen[y])
	for i in range(len(v)):
		v[i] =  screen[y][(i-n)%len(v)]
	screen[y] = v
	return screen

regexs = {
r'rect (\d+)x(\d+)'					: rect,
r'rotate row y=(\d+) by (\d+)'		: rotate_row,
r'rotate column x=(\d+) by (\d+)'	: rotate_col,
}


screen = [[False for c in range(50)] for r in range(6)]
print_screen(screen)

with open('8.input', 'r') as f:
	for line in f:
		for regex, func in regexs.items():
			match = re.match(regex, line)
			if match:
				screen = func(screen, *[int(x) for x in match.groups()])
				print_screen(screen)
				#time.sleep(0.05)
				break
print(sum(sum(screen, [])))

