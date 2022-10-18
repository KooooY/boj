import sys
input = sys.stdin.readline

N = int(input())

price_info = [list(map(int, input().split())) for _ in range(N)]
price_list = [1001]*N

for r in range(1, N-1):
    for c in range(N):
        if c == 0 or c == N-1:
            temp = 1001
        else:
            temp = price_info[r][c] + price_info[r-1][c] + price_info[r+1][c] + price_info[r][c-1] + price_info[r][c+1]
        price_list.append(temp)
price_list.extend([1001]*N)

ans = 99999999
for i in range(N+1, N**2-N-2):
    visited_i = {i+N, i+N-1, i+N, i+N+1, i+2*N}
    if price_list[i] == 1001:
        continue
    for j in range(i+3, N**2-N-1):
        if j in visited_i or price_list[j] == 1001:
            continue
        visited_j = {j+N, j+N-1, j+N, j+N+1, j+2*N}
        for k in range(j+3, N**2-N):
            if k in (visited_i|visited_j) or price_list[k] == 1001:
                continue
            if ans > price_list[i]+price_list[j]+price_list[k]:
                ans = price_list[i]+price_list[j]+price_list[k]

print(ans)