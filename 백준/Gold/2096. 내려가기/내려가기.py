N = int(input())

dp = [[[0, 0, 0], [0, 0, 0]]] * 2

for i in range(N):
    game = list(map(int, input().split()))
    dp[1][0] = [min(dp[0][0][0], dp[0][0][1]) + game[0], min(dp[0][0]) + game[1], min(dp[0][0][1], dp[0][0][2]) + game[2]]
    dp[1][1] = [max(dp[0][1][0], dp[0][1][1]) + game[0], max(dp[0][1]) + game[1], max(dp[0][1][1], dp[0][1][2]) + game[2]]

    dp[0] = dp[1]

print(max(dp[1][1]), min(dp[1][0]))