N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

dp = [[(0, 0, 0)]*N for _ in range(N)]
dp[0][1] = (1, 0, 0)

for i in range(N):
    for j in range(2, N):
        if not house[i][j]:
            if not i:
                dp[i][j] = (dp[i][j-1][0], 0, 0)
            else:
                horizontal = dp[i][j-1][0] + dp[i][j-1][2]
                vertical = dp[i-1][j][1] + dp[i-1][j][2]
                diagonal = 0
                if not house[i-1][j] and not house[i][j-1]:
                    diagonal = sum(dp[i-1][j-1])
                dp[i][j] = (horizontal, vertical, diagonal)

print(sum(dp[N-1][N-1]))
