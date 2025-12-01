def next_secret(secret: Int) -> Int:
    temp = secret << 6
    secret = temp ^ secret
    secret = secret % 16777216

    temp = secret >> 5
    secret = temp ^ secret
    secret = secret % 16777216

    temp = secret << 11
    secret = temp ^ secret
    secret = secret % 16777216

    return secret

@value
struct Seq():
    var a: Int
    var b: Int
    var c: Int
    var d: Int

def main():
    n_secrets = 2000
    all_prices = List[List[Int]]()
    lines = open("input.22", "r").read().splitlines()
    buyers = List[Int]()
    for line in lines:
        buyers.append(atol(line[], 10))

    for b in buyers:
        prices = List[Int]()
        secret = b[]
        prices.append(secret % 10)
        for _ in range(n_secrets):
            secret = next_secret(secret)
            prices.append(secret % 10)
        all_prices.append(prices)


    all_deltas = List[List[Int]]()
    for prices in all_prices:
        deltas = List[Int]()
        for i in range(len(prices[]) - 1):
            delta = prices[][i+1] - prices[][i]
            deltas.append(delta)
        all_deltas.append(deltas)

    seen = Dict[Seq]()
    for deltas in all_deltas:
        for i in range(len(deltas) - 4):
            seq = tuple(deltas[i:i+4])
            seen.add(seq)


    # max_banana = 0
    # for x, given_seq in enumerate(seen):
    #     print(x, len(seen))
    #     bananas = 0
    #     for monkey, deltas in enumerate(all_deltas):
    #         for i in range(len(deltas) - 4):
    #             seq = tuple(deltas[i:i+4])
    #             if seq == given_seq:
    #                 bananas += all_prices[monkey][i+4]
    #                 break
    #         if sum([price for price in max_prices[monkey:]]) + bananas < max_banana:
    #             continue
    #     max_banana = max(max_banana, bananas)
    # print(max_banana)