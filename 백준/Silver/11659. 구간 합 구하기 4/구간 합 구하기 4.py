import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
acc_num = [num_list[0]]

for i in range(1, N):
    acc_num.append(acc_num[i-1]+num_list[i])

for _ in range(M):
    start, end = map(int, input().split())
    if start == 1:
        print(acc_num[end-1])
    else:
        print(acc_num[end-1]-acc_num[start-2])