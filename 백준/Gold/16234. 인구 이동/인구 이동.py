from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]
answer = 0
flag = 1
visited = set()

while flag:
    for r in range(N):
        for c in range(r%2, N, 2):
            if (r, c) not in visited:
                Q = deque()
                Q.append((r, c))
                visited.add((r, c))
                group_visited = {(r, c)}
                total_population = population[r][c]

                while Q:
                    cur_r, cur_c = Q.popleft()
                    for i in range(4):
                        if 0 <= cur_r + dr[i] < N and 0 <= cur_c + dc[i] < N and (cur_r + dr[i], cur_c + dc[i]) not in visited and L <= abs(population[cur_r + dr[i]][cur_c + dc[i]] - population[cur_r][cur_c]) <= R:
                            flag = 0
                            visited.add((cur_r + dr[i], cur_c + dc[i]))
                            group_visited.add((cur_r + dr[i], cur_c + dc[i]))
                            Q.append((cur_r + dr[i], cur_c + dc[i]))
                            total_population += population[cur_r + dr[i]][cur_c + dc[i]]

                if total_population != population[r][c]:
                    cur_pop = total_population//len(group_visited)
                    for land in group_visited:
                        population[land[0]][land[1]] = cur_pop

    if flag:
        flag = 0
    else:
        flag = 1
        answer += 1
        visited.clear()

print(answer)