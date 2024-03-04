import sys
input = sys.stdin.readline

N = int(input())

dp = [[[9999999] * 3 for _ in range(N)] for _ in range(3)]
r1, g1, b1 = map(int, input().split())
dp[0][0][0], dp[1][0][1], dp[2][0][2] = r1, g1, b1

for i in range(1, N):
    r, g, b = map(int, input().split())
    for j in range(3):
        dp[j][i][0] = min(dp[j][i-1][1] + r, dp[j][i-1][2] + r)
        dp[j][i][1] = min(dp[j][i-1][0] + g, dp[j][i-1][2] + g)
        dp[j][i][2] = min(dp[j][i-1][0] + b, dp[j][i-1][1] + b)

print(min(dp[0][N-1][1], dp[0][N-1][2], dp[1][N-1][0], dp[1][N-1][2], dp[2][N-1][0], dp[2][N-1][1]))