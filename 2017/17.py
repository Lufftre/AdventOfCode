step_size = 356

lock = [0]
current_pos = 0
for i in range(1, 2018):
    current_pos = (current_pos + step_size) % i
    current_pos += 1
    lock.insert(current_pos, i)
print(lock[current_pos], lock[current_pos+1])

# lock = [0]
# current_pos = 0
# for i in range(1, 50000001):
#     current_pos = (current_pos + step_size) % i
#     current_pos += 1
#     lock.insert(current_pos, i)
# idx = lock.index(0)
# print(idx, lock[idx+1])
cur_idx = 0
best = -1
# Zero is always at the beginning
# Save just the value if it is after 0
for i in range(1, 50000000+1):
    cur_idx = (cur_idx + step_size) % i
    if cur_idx == 0:
        best = i
    cur_idx += 1
print('Answer #2: {}'.format(best))