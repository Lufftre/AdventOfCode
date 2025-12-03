IN = """987654321111111
811111111111119
234234234234278
818181911112111"""


def solve(line, n):
    res = ""
    for j in range(n, 0, -1):
        for i in range(9, 0, -1):
            idx = line[: len(line) - j + 1].find(str(i))
            if idx != -1:
                res += str(i)
                line = line[idx + 1 :]
                break

    print(res)
    return int(res)


IN = open("03.input").read()
s = sum([solve(line, 12) for line in IN.splitlines()])
print(s)
