def bfs(wall_1, wall_2, wall_3):
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    virus = {wall_1, wall_2, wall_3}
    for i in range(N):
        for j in range(M):
            if map_info[i][j]:
                virus.add((i, j))
                if map_info[i][j] == 2:
                    stack = [(i, j)]
                    while stack:
                        cur = stack.pop(0)
                        for k in range(4):
                            if 0 <= cur[0]+dr[k] < N and 0 <= cur[1]+dc[k] < M and not map_info[cur[0]+dr[k]][cur[1]+dc[k]] and (cur[0]+dr[k], cur[1]+dc[k]) not in virus:
                                stack.append((cur[0]+dr[k], cur[1]+dc[k]))
                                virus.add((cur[0]+dr[k], cur[1]+dc[k]))

    return N * M - len(virus)


N, M = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(N)]

answer = 0

for r_1 in range(N):
    for c_1 in range(M):
        walls = set()
        if not map_info[r_1][c_1]:
            walls.add((r_1, c_1))
            for r_2 in range(r_1, N):
                for c_2 in range(M):
                    if not map_info[r_2][c_2] and (r_2, c_2) not in walls:
                        walls.add((r_2, c_2))
                        for r_3 in range(r_2, N):
                            for c_3 in range(M):
                                if not map_info[r_3][c_3] and (r_3, c_3) not in walls:
                                    walls.add((r_3, c_3))
                                    temp = bfs((r_1, c_1), (r_2, c_2), (r_3, c_3))
                                    if temp > answer:
                                        answer = temp
                                    walls.remove((r_3, c_3))
                        walls.remove((r_2, c_2))

print(answer)