regs = {}
highscore = 0
with open('.08') as f:
    for line in f:
        exec('regs["{0}"] = regs.get("{0}", 0) {1} ({2} {3} regs.get("{4}", 0) {5} {6} else 0)'.format(*line.replace('inc', '+').replace('dec', '-').split()))
        highscore = max(regs.values()) if max(regs.values()) > highscore else highscore
print(max(regs.values()))
print(highscore)
