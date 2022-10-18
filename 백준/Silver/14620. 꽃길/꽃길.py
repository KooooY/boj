import sys
input = sys.stdin.readline

N = int(input())

price_info = [list(map(int, input().split())) for _ in range(N)]
price_list = []

for r in range(N):
    for c in range(N):
        if r == 0 or r == N - 1 or c == 0 or c == N - 1:
            temp = 1001
        else:
            temp = price_info[r][c] + price_info[r - 1][c] + price_info[r + 1][c] + price_info[r][c - 1] + price_info[r][c + 1]
        price_list.append(temp)

ans = 99999999
for i in range(N+1, N**2-N):
    visited_i = {i+N, i+N-1, i+N, i+N+1, i+2*N}
    if price_list[i] == 1001:
        continue
    for j in range(i+3, N**2-N):
        if j in visited_i or price_list[j] == 1001:
            continue
        visited_j = {j+N, j+N-1, j+N, j+N+1, j+2*N}
        for k in range(j+3, N**2-N):
            if k in visited_i or k in visited_j or price_list[k] == 1001:
                continue
            if ans > price_list[i]+price_list[j]+price_list[k]:
                ans = price_list[i]+price_list[j]+price_list[k]

print(ans)