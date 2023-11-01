non_self_number_set = set()

for i in range(1, 10000):
    self_sum = i + i // 10000 + (i % 10000) // 1000 + (i % 1000) // 100 + (i % 100) // 10 + (i % 10)
    non_self_number_set.add(self_sum)

for j in range(1, 10000):
    if j not in non_self_number_set:
        print(j)