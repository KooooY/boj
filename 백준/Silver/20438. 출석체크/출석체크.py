N, K, Q, M = map(int, input().split())
sleep_list = list(map(int, input().split()))
code_list = list(map(int, input().split()))
count_range = [list(map(int, input().split())) for _ in range(M)]
attendance = [1]*(N+3)

for i in code_list:
    if i not in sleep_list:
        for j in range(i, N+3, i):
            if j not in sleep_list:
                attendance[j] = 0

for k in count_range:
    print(sum(attendance[k[0]:k[1]+1]))