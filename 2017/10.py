from functools import reduce
def run(string, ops, iterations=1):
    current_pos = 0
    skip = 0
    for iteration in range(iterations):
        for op in ops:
            diff = len(string) - (current_pos + op)
            if diff > 0:
                asf = string[current_pos:current_pos+op]
                asf2 = []
                string[current_pos:current_pos+op] = asf[::-1]
            else:
                asf = string[current_pos:]
                asf2 = string[:abs(diff)]
                for i,n in enumerate((asf+asf2)[::-1]):
                    string[(current_pos+i)%len(string)] = n
            
            current_pos = (current_pos + op + skip) % len(string)
            skip += 1
    return string


with open('.10') as f:
    ops = [int(op) for op in f.read().split(',')]
string = run(list(range(256)), ops)
print(string[0]*string[1])
    
with open('.10') as f:
    ops = [ord(c) for c in f.read()] + [17, 31, 73, 47, 23]
string = run(list(range(256)), ops, 64)

dense = ''.join('{:02X}'.format(x) for x in [reduce(lambda a,b: a^b, string[i:i+16]) for i in range(0,256,16)]).lower()
print(dense)
    