N = int(input())
orchard = [list(map(int, input().split())) for _ in range(N)]
prefix_sum = [[0]*(N+1) for _ in range(N+1)]
ans = -1001

for i in range(N):
    for j in range(N):
        prefix_sum[i+1][j+1] = orchard[i][j]+prefix_sum[i][j+1]+prefix_sum[i+1][j]-prefix_sum[i][j]

for k in range(N, 0, -1):
    for r in range(N, k-1, -1):
        for c in range(N, k-1, -1):
            if prefix_sum[r][c]+prefix_sum[r-k][c-k]-prefix_sum[r][c-k]-prefix_sum[r-k][c] > ans:
                ans = prefix_sum[r][c]+prefix_sum[r-k][c-k]-prefix_sum[r][c-k]-prefix_sum[r-k][c]

print(ans)