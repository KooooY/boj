import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]
answer = K * K

white_prefix = [[0]*(M+1) for _ in range(N+1)]
black_prefix = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if (i%2 and j%2) or (not i%2 and not j%2):
            if board[i-1][j-1] == 'B':
                white_prefix[i][j] = white_prefix[i-1][j] + white_prefix[i][j-1] - white_prefix[i-1][j-1] + 1
                black_prefix[i][j] = black_prefix[i-1][j] + black_prefix[i][j-1] - black_prefix[i-1][j-1]
            else:
                white_prefix[i][j] = white_prefix[i - 1][j] + white_prefix[i][j - 1] - white_prefix[i - 1][j - 1]
                black_prefix[i][j] = black_prefix[i - 1][j] + black_prefix[i][j - 1] - black_prefix[i - 1][j - 1] + 1
        else:
            if board[i-1][j-1] == 'B':
                white_prefix[i][j] = white_prefix[i-1][j] + white_prefix[i][j-1] - white_prefix[i-1][j-1]
                black_prefix[i][j] = black_prefix[i-1][j] + black_prefix[i][j-1] - black_prefix[i-1][j-1] + 1
            else:
                white_prefix[i][j] = white_prefix[i - 1][j] + white_prefix[i][j - 1] - white_prefix[i - 1][j - 1] + 1
                black_prefix[i][j] = black_prefix[i - 1][j] + black_prefix[i][j - 1] - black_prefix[i - 1][j - 1]

for k in range(K, N+1):
    for l in range(K, M+1):
        white = white_prefix[k][l] + white_prefix[k-K][l-K] - white_prefix[k-K][l] - white_prefix[k][l-K]
        black = black_prefix[k][l] + black_prefix[k-K][l-K] - black_prefix[k-K][l] - black_prefix[k][l-K]
        answer = min(answer, white, black)


print(answer)