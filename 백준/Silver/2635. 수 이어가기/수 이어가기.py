N = int(input())
second = [int(N * 0.618)-2, int(N * 0.618)-1, int(N * 0.618), int(N * 0.618)+1, int(N * 0.618)+2]
max_num_len = 0

for i in second:
    num_list = [N, i]
    new = 0
    start = 0
    while new >= 0:
        new = num_list[start] - num_list[start+1]
        num_list.append(new)
        start += 1

    if num_list[-1] < 0:
        del num_list[-1]
    if len(num_list) > max_num_len:
        max_num_len = len(num_list)
        max_num_list = num_list

print(max_num_len)
print(*max_num_list)