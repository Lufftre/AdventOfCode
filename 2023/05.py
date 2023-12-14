import json
import multiprocessing
import math

maps = json.load(open("05_maps.json"))
seeds = (
    364807853,
    408612163,
    302918330,
    20208251,
    1499552892,
    200291842,
    3284226943,
    16030044,
    2593569946,
    345762334,
    3692780593,
    17215731,
    1207118682,
    189983080,
    2231594291,
    72205975,
    3817565407,
    443061598,
    2313976854,
    203929368,
)
# seeds = (79, 14, 55, 13)


def seedToLocation(seed):
    current = seed
    for map in maps:
        for dest, src, length in map:
            if current >= src and current < (src + length):
                current = dest + (current - src)
                break
    return current


def seedRange(seedRange):
    start, length = seedRange
    shortest = math.inf

    for seed in range(start, start + length):
        location = seedToLocation(seed)
        shortest = min(shortest, location)
    return shortest


part2 = None
results = []
if __name__ == "__main__":
    ranges = []
    for i in range(0, len(seeds), 2):
        seedStart = seeds[i]
        length = seeds[i + 1]
        ranges.append([seedStart, length])

    with multiprocessing.Pool() as pool:
        shortest = min(pool.imap_unordered(seedRange, ranges))
        results.append(shortest)
    print(min(results))
