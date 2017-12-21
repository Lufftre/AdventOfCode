import numpy as np
image = np.mat('0 1 0;0 0 1;1 1 1')
patterns = {}
for line in open('.21'):
    key, val = map(str.strip, line.split('=>'))
    patterns[key] = np.matrix(val.replace('/',';').replace('#','1 ').replace('.','0 '))

def mat2key(mat):
    s = ''
    for y in range(len(mat)):
        for x in range(len(mat)):
            s += str(mat[y,x]).replace('1','#').replace('0','.')
        s += '/'
    return s[:-1]
    
def split(image, step):
    big = None
    for y in range(0, len(image), step):
        row = None
        for x in range(0, len(image), step):
            sub = image[y:y+step, x:x+step]
            new = flipboi(sub)
            row = np.concatenate((row, new), axis=1) if row is not None else new 
        big = np.concatenate((big, row), axis=0) if big is not None else row
    return big


def flipboi(boi):
    for i in range(4):
        mat = np.rot90(boi, i)
        key = mat2key(mat)
        if key in patterns:
            break
        mat = mat.transpose()
        key = mat2key(mat)
        if key in patterns:
            break
    else:
        raise Exception('Fail')
    return patterns.get(key)

for i in range(18):
    image = split(image, 2 if len(image) % 2 == 0 else 3)
    print(i+1, np.sum(image))
