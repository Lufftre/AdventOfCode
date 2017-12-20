import re
class Particle(object):
    def __init__(self, id, pos, vel, acc):
        self.id = id
        self.pos = pos
        self.vel = vel
        self.acc= acc
        self.dead = False

    def update(self):
        self.vel = [v+a for v,a in zip(self.vel, self.acc)]
        self.pos = [v+p for v,p in zip(self.vel, self.pos)]
        return sum(map(abs, self.pos))

regex = re.compile(r'p=<([0-9,-]+)>, v=<([0-9,-]+)>, a=<([0-9,-]+)>')
particles = [Particle(i,*map(eval, regex.match(line).groups())) for i,line in enumerate(open('.20'))]

while True:
    best = None, None
    for p in particles:
        distance = p.update()
        best = (p.id, distance) if best[1] is None or distance < best[1] else best
    for i,p in enumerate(particles):
        if p.dead: continue
        for pp in particles[i+1:]:
            if pp.dead: continue
            if p.pos == pp.pos:
                p.dead = True
                pp.dead = True
    print('close:', best[0], end='\033[K\n')
    print('alive:', sum([not p.dead for p in particles]), end='\033[K\033[1A\r')