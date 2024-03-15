import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
info = [[0] * M for _ in range(N)]
walls = set()
lands = dict()
visited = set()

for i in range(N):
    for j in range(M):
        if matrix[i][j] == '1':
            walls.add((i, j))
        else:
            if not info[i][j]:
                land = 0
                start = (i, j)
                Q = [start]
                visited.add(start)
                while Q:
                    cur = Q.pop()
                    land += 1
                    info[cur[0]][cur[1]] = start
                    for k in range(4):
                        if 0 <= cur[0] + dr[k] < N and 0 <= cur[1] + dc[k] < M and matrix[cur[0] + dr[k]][cur[1] + dc[k]] == '0' and (cur[0] + dr[k], cur[1] + dc[k]) not in visited:
                            visited.add((cur[0] + dr[k], cur[1] + dc[k]))
                            Q.append((cur[0] + dr[k], cur[1] + dc[k]))
                lands[(i, j)] = land

for wall in walls:
    temp = set()
    ans = 1
    for d in range(4):
        if 0 <= wall[0] + dr[d] < N and 0 <= wall[1] + dc[d] < M and info[wall[0] + dr[d]][wall[1] + dc[d]]:
            temp.add(info[wall[0] + dr[d]][wall[1] + dc[d]])
    for lan in temp:
        ans += lands[lan]
    matrix[wall[0]][wall[1]] = str(ans%10)

for mat in matrix:
    print(''.join((mat)))