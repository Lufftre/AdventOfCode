IN = """987654321111111
811111111111119
234234234234278
818181911112111"""


def solve(line, n):
    res = ""
    line = list(map(int, list(line)))
    for j in range(n, 0, -1):
        idx = line.index(max(line[: len(line) - (j - 1)]))
        res += str(line[idx])
        line = line[idx + 1 :]

    print(res)
    return int(res)


IN = open("03.input").read()
s = sum([solve(line, 12) for line in IN.splitlines()])
print(s)
