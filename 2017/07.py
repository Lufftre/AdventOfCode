from collections import Counter
tree = {}
with open('.07') as f:
    for line in f:
        line = line.replace('\n', ' ').split('->')
        key, val = line[0].split()
        children = eval(line[1].replace(' ', '"').replace(',', '",')) if len(line) > 1 else ()
        tree[key] = (eval(val), children)

current = list(tree.keys())[0]
while True:
    for parent, (weight, children) in tree.items():
        if current in children:
            current = parent
            break
    else:
        root = current
        break

def check_node(key):
    weight, children = tree[key]
    weights = [mass_below(child) for child in children]
    uw = list(set(weights))
    if not len(uw) <= 1:
        return abs(uw[0] - uw[1])
    return 0

def mass_below(key):
    weight, children = tree[key]
    tot_weight = weight
    for child in children:
        tot_weight += mass_below(child)
    return tot_weight

print(root)
current = root
while True:
    weight, children = tree[current]
    for i, child in enumerate(children):
        if check_node(child):
            current = children[i]
            break
    else:
        for i, child in enumerate(children):
            print(child, tree[child][0], mass_below(child))
        break

