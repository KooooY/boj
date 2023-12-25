from collections import deque

M, N, H = map(int, input().split())
box = []
riped_tomatoes = deque()
green_tomatoes = 0

for h in range(H):
    temp = []
    for n in range(N):
        tomato_state = list(map(int, input().split()))
        for m in range(M):
            if tomato_state[m] == 1:
                riped_tomatoes.append((h, n, m, 0))
            if not tomato_state[m]:
                green_tomatoes += 1
        temp.append(tomato_state)
    box.append(temp)

if not green_tomatoes:
    print(0)
elif not riped_tomatoes:
    print(-1)
else:
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    answer = 0
    while riped_tomatoes:
        current = riped_tomatoes.popleft()
        for i in range(4):
            h = current[0]
            n_r = current[1] + dr[i]
            n_c = current[2] + dc[i]
            n_d = current[3] + 1
            if 0 <= n_r < N and 0 <= n_c < M and not box[h][n_r][n_c]:
                riped_tomatoes.append((h, n_r, n_c, n_d))
                box[h][n_r][n_c] = 1
                green_tomatoes -= 1
        if 0 <= current[0] - 1 < H and not box[current[0]-1][current[1]][current[2]]:
            riped_tomatoes.append((current[0] - 1, current[1], current[2], current[3] + 1))
            box[current[0] - 1][current[1]][current[2]] = 1
            green_tomatoes -= 1
        if 0 <= current[0] + 1 < H and not box[current[0]+1][current[1]][current[2]]:
            riped_tomatoes.append((current[0] + 1, current[1], current[2], current[3] + 1))
            box[current[0] + 1][current[1]][current[2]] = 1
            green_tomatoes -= 1
        answer = current[3]
    if green_tomatoes:
        print(-1)
    else:
        print(answer)