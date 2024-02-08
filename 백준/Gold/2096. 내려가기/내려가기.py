N = int(input())

dp = [[[0, 0]] * 3 for _ in range(2)]

for i in range(N):
    game = list(map(int, input().split()))
    dp[1][0] = [min(dp[0][0][0], dp[0][1][0]) + game[0], max(dp[0][0][1], dp[0][1][1]) + game[0]]
    dp[1][1] = [min(dp[0][0][0], dp[0][1][0], dp[0][2][0]) + game[1], max(dp[0][0][1], dp[0][1][1], dp[0][2][1]) + game[1]]
    dp[1][2] = [min(dp[0][1][0], dp[0][2][0]) + game[2], max(dp[0][1][1], dp[0][2][1]) + game[2]]

    dp[0][0] = dp[1][0]
    dp[0][1] = dp[1][1]
    dp[0][2] = dp[1][2]

answer = []
answer.extend(dp[1][0])
answer.extend(dp[1][1])
answer.extend(dp[1][2])
print(max(answer), min(answer))