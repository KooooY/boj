T = int(input())

for _ in range(T):
    N = int(input())
    sticker_info = [[0]+list(map(int, input().split())) for _ in range(2)]
    sticker_sack = [[0]*(N+1) for _ in range(2)]

    for i in range(1, N+1):
        sticker_sack[0][i] = max(sticker_sack[0][i-1], sticker_sack[1][i-1]+sticker_info[0][i])
        sticker_sack[1][i] = max(sticker_sack[1][i-1], sticker_sack[0][i-1]+sticker_info[1][i])

    print(max(sticker_sack[0][N], sticker_sack[1][N]))