import sys
input = sys.stdin.readline

N = int(input())

if N < 3:
    print(0)
else:
    matrix_info = list(map(int, input().split()))
    dp = [[999999999] * N for _ in range(N)]

    for _ in range(N - 1):
        a, b = map(int, input().split())
        matrix_info.append(b)

    for i in range(N):
        dp[i][i] = 0
        for j in range(i - 1, -1, -1):
            for k in range(j, i):
                dp[j][i] = min(dp[j][i], dp[j][k] + dp[k + 1][i] + matrix_info[j] * matrix_info[i + 1] * matrix_info[k + 1])

    print(dp[0][N - 1])