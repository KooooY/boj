import sys
input = sys.stdin.readline

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

M, N = map(int, input().split())
tomato_state = []
ripe_tomato = deque()
tomato_count = 0
date_count = 0

for n in range(N):
    temp = list(map(int, input().split()))
    for m in range(M):
        if not temp[m]:
            tomato_count += 1
        if temp[m] == 1:
            ripe_tomato.append((n, m, 0))
    tomato_state.append(temp)

if not ripe_tomato:
    print(-1)
elif not tomato_count:
    print(0)
else:
    while ripe_tomato:
        current = ripe_tomato.popleft()
        for i in range(4):
            n_r = current[0] + dr[i]
            n_c = current[1] + dc[i]
            n_d = current[2] + 1
            if 0 <= n_r < N and 0 <= n_c < M and not tomato_state[n_r][n_c]:
                tomato_state[n_r][n_c] = 1
                ripe_tomato.append((n_r, n_c, n_d))
                tomato_count -= 1
        date_count = current[2]
    if tomato_count:
        print(-1)
    else:
        print(date_count)