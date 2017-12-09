skip = False
garbage = False
i = 0
tot = 0
garbage_count = 0
with open('.09') as f:
    for c in f.read():
        if skip:
            skip = False
        elif c == '!':
            skip = True
        elif garbage:
            if c == '>':
                garbage = False
            else:
                garbage_count += 1
        elif c == '<':
            garbage = True
        elif c == '{':
            i += 1
            tot += i
        elif c == '}':
            i -= 1
print(tot, garbage_count)