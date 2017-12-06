with open('.01') as f:
    data = [int(d) for d in f.read()]

distance = 1
print(sum([d for i, d in enumerate(data) if d == data[(i+distance)%len(data)]]))
    
distance = len(data)//2
print(sum([d for i, d in enumerate(data) if d == data[(i+distance)%len(data)]]))
    