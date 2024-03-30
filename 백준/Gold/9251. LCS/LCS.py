string_1 = input()
string_2 = input()

dp = [[0] * (len(string_2) + 1) for _ in range(len(string_1) + 1)]

for i in range(1, len(string_1) + 1):
    for j in range(1, len(string_2) + 1):
        if string_1[i - 1] == string_2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

print(dp[len(string_1)][len(string_2)])