def floor_num(pre_num, pre_binary, turn):
    global answer
    if pre_binary == 1023:
        answer += 1
    if turn == N:
        return

    cur_min = pre_num % 10 - 1
    cur_max = pre_num % 10 + 1
    if pre_num % 10 > 0:
        new_binary = pre_binary | (1 << cur_min)
        floor_num(pre_num * 10 + cur_min, new_binary, turn + 1)
    if pre_num % 10 < 9:
        new_binary = pre_binary | (1 << cur_max)
        floor_num(pre_num * 10 + cur_max, new_binary, turn + 1)
    return


N = int(input())
dp = [[[0] * (2 ** 10) for _ in range(10)] for _ in range(N + 1)]
answer = 0

if N > 9:
    for num in range(1, 10):
        dp[1][num][1 << num] = 1

    for i in range(1, N):
        for j in range(10):
            for k in range(1024):
                if j > 0:
                    dp[i + 1][j - 1][k | 1 << (j - 1)] += dp[i][j][k]
                if j < 9:
                    dp[i + 1][j + 1][k | 1 << (j + 1)] += dp[i][j][k]

    for l in range(10):
        answer += dp[N][l][1023]

print(answer % 1000000000)