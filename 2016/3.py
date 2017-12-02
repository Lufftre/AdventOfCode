possible = 0
with open('3.input', 'r') as f:
  for line in f:
      hej = sorted([int(x) for x in line.split()])
      if hej[0] + hej[1] > hej[2]:
          possible += 1
print(possible)



possible = 0
with open('3.input', 'r') as f:
    hej = [[],[],[]]
    for line in f:
        fin_line = [int(x) for x in line.split()]
        hej[0].append(fin_line[0])
        hej[1].append(fin_line[1])
        hej[2].append(fin_line[2])
        if len(hej[0]) == 3:
            for trig in hej:
                trig.sort()
                if trig[0] + trig[1] > trig[2]:
                    possible += 1

            hej = [[],[],[]]
print(possible)