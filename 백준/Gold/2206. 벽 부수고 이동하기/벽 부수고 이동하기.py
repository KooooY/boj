import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
map_arr = [list(input().rstrip()) for _ in range(N)]
answer = 0
flag = 1

Q = deque([(0, 0, 0)])
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

while Q and flag:
    r, c, w = Q.popleft()
    for k in range(4):
        if (r + dr[k], c + dc[k]) == (N - 1, M - 1):
            answer = visited[r][c][w] + 1
            flag = 0
            break
        if 0 <= r + dr[k] < N and 0 <= c + dc[k] < M:
            if map_arr[r + dr[k]][c + dc[k]] == '1' and w == 0:
                Q.append((r + dr[k], c + dc[k], 1))
                visited[r + dr[k]][c + dc[k]][1] = visited[r][c][w] + 1

            if map_arr[r + dr[k]][c + dc[k]] == '0' and not visited[r + dr[k]][c + dc[k]][w]:
                Q.append((r + dr[k], c + dc[k], w))
                visited[r + dr[k]][c + dc[k]][w] = visited[r][c][w] + 1

if N == 1 and M == 1:
    print(1)
elif answer:
    print(answer)
else:
    print(-1)