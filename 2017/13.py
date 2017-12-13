layers = {}
with open('.13') as f:
    exec('layers = {{{}}}'.format(f.read().replace('\n', ',')))

severity = sum([layer*height for layer, height in layers.items() if not layer % (2 * height - 2)])  
print(severity)

delay = 0
while True:
    for layer, height in layers.items():
        if not (layer + delay) % (2 * height - 2):
            break
    else:
        break
    delay += 1
print(delay)