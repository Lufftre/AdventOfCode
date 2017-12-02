import re

data = {}
ops = {
    r'(\w+)$': (lambda a: a),
    r'NOT (\w+)$': (lambda a: 65535 - a),
    r'(\w+) AND (\w+)$': (lambda a,b: a & b),
    r'(\w+) OR (\w+)$': (lambda a,b: a | b),
    r'(\w+) LSHIFT (\w+)$': (lambda a,b: a << b),
    r'(\w+) RSHIFT (\w+)$': (lambda a,b: a >> b),
}


def part1():
    with open('.day7') as f:
        conns = [line.strip().split(' -> ') for line in f]

        #while not data.get('a'):
        while not 'a' in data:
            for op, dest in conns:
                for regex, func in ops.items():
                    m = re.match(regex, op)
                    if m:
                        try:
                            data[dest] = func(*[int(data.get(x,x)) for x in m.groups()])
                        except:
                            pass
                        continue
        return data.get('a')



def part2(a):
    data = {'b': a}
    with open('.day7') as f:
        conns = [line.strip().split(' -> ') for line in f]

        while 'a' in data:
            for op, dest in conns:
                if dest == 'b':
                    continue
                for regex, func in ops.items():
                    m = re.match(regex, op)
                    if m:
                        try:
                            data[dest] = func(*[int(data.get(x,x)) for x in m.groups()])
                        except:
                            pass
                        continue
        return data.get('a')

a = part1()
print( a )
print( part2(a) )
