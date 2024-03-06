N, M = map(int, input().split())
memory_bite = list(map(int, input().split()))
disabled = list(map(int, input().split()))

dp = [[0] * (sum(disabled) + 1) for _ in range(2)]
answer = sum(disabled)

for i in range(N):
    for j in range(sum(disabled) + 1):
        if j >= disabled[i]:
            dp[1][j] = max(dp[0][j], dp[1][j], dp[0][j - disabled[i]] + memory_bite[i])
            if dp[1][j] >= M and j < answer:
                answer = j
    dp[0] = dp[1][:]

print(answer)