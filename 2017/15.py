a = 277
b = 349

factor_a = 16807
factor_b = 48271

divider = 2147483647
low_16 = 2**16

score = 0
for i in range(40000000):
    a = (a * factor_a) % divider
    b = (b * factor_b) % divider
    if a % low_16 == b % low_16:
        print(i, a, b)
        score += 1
print(score)

# score = 0
# for i in range(5000000):
#     a = (a * factor_a) % divider
#     while a % 4:
#         a = (a * factor_a) % divider

#     b = (b * factor_b) % divider
#     while b % 8:
#         b = (b * factor_b) % divider

#     if a % low_16 == b % low_16:
#         score += 1
# print(score)