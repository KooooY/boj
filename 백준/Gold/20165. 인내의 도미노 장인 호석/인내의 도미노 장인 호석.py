dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
new_board = [['S']*M for _ in range(N)]
point = 0

for i in range(R):
    attacker = list(map(str, input().split()))
    defender = list(map(int, input().split()))
    r = int(attacker[0])-1
    c = int(attacker[1])-1
    goal = board[r][c]
    cnt = 0
    d = 0
    if attacker[2] == 'W':
        d = 1
    elif attacker[2] == 'S':
        d = 2
    elif attacker[2] == 'N':
        d = 3

    while cnt < goal and 0 <= r < N and 0 <= c < M:
        if new_board[r][c] == 'F' and goal-cnt < 2:
            break
        if new_board[r][c] == 'S' and goal-cnt < board[r][c]:
            goal = board[r][c]
            cnt = 0
        if new_board[r][c] == 'S':
            point += 1
        new_board[r][c] = 'F'
        cnt += 1
        r += dr[d]
        c += dc[d]

    if new_board[defender[0]-1][defender[1]-1] == 'F':
        new_board[defender[0]-1][defender[1]-1] = 'S'

print(point)
for i in range(N):
    print(*new_board[i])