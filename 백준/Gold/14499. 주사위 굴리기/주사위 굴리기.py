import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
moving = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]

for m in moving:
    new_x, new_y = x + dx[m - 1], y + dy[m - 1]
    if 0 <= new_x < N and 0 <= new_y < M:
        x, y = new_x, new_y
        if m == 1:
            dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
        elif m == 2:
            dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
        elif m == 3:
            dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
        else:
            dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
        print(dice[0])
        if arr[x][y]:
            dice[5] = arr[x][y]
            arr[x][y] = 0
        else:
            arr[x][y] = dice[5]