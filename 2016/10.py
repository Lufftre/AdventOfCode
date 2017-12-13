import re

re0 = r'value (\d+) goes to bot (\d+)'
re1 = r'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)'

data = {}
actions = []
with open('10.input', 'r') as f:
	for line in f:
		m = re.match(re0, line)
		if m:
			data[m.group(2)] = sorted(data.get(m.group(2), []) + [int(m.group(1))])
			continue
		m = re.match(re1, line)
		if m:
			actions += [m.groups()]

#print(data)
#print(actions)
def do_stuff(data, actions, x, y):
	for key, value in data.items():
		if len(value) == 2:
			for a in actions:
				if a[0] == key:
					if(value[0] == x and value[1] == y):
						print(key, 'is bot')
						#del actions[:]
						#return
					print('bot', key,'compare', value[0], value[1])
					if a[1] == 'output':
						k = 'output' + a[2]
					else:
						k = a[2]
					data[k] = sorted(data.get(k, []) + [value[0]])
					if a[3] == 'output':
						k = 'output' + a[4]
					else:
						k = a[4]
						data[k] = sorted(data.get(k, []) + [value[1]])
					data[key] = []
					actions.remove(a)
					#print(data)
					#print(actions)
					return
while actions:
	do_stuff(data, actions, 17, 61)
print(data)
print(data.get('output0'))
print(data.get('output1'))
print(data.get('output2'))
print(data['output0'])