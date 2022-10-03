dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra():
    dist = [[99999]*(N+2) for _ in range(N+2)]
    dist[1][1] = matrix[1][1]
    visited = [[0]*(N+2) for _ in range(N+2)]
    min_idx = (-1, -1)
    path_set = {(1, 1)}

    for _ in range(N*N):
        min_value = 99999
        for i in path_set:
            if not visited[i[0]][i[1]] and dist[i[0]][i[1]] < min_value:
                min_idx = (i[0], i[1])
                min_value = dist[i[0]][i[1]]

        visited[min_idx[0]][min_idx[1]] = 1
        path_set.remove((min_idx[0], min_idx[1]))

        for k in range(4):
            if not visited[min_idx[0]+dr[k]][min_idx[1]+dc[k]] and dist[min_idx[0]+dr[k]][min_idx[1]+dc[k]] > matrix[min_idx[0]+dr[k]][min_idx[1]+dc[k]]+dist[min_idx[0]][min_idx[1]]:
                dist[min_idx[0]+dr[k]][min_idx[1]+dc[k]] = matrix[min_idx[0]+dr[k]][min_idx[1]+dc[k]]+dist[min_idx[0]][min_idx[1]]
                path_set.add((min_idx[0]+dr[k], min_idx[1]+dc[k]))

        if dist[N][N] != 99999:
            break

    return dist[N][N]

t = 1
while True:
    N = int(input())
    if not N:
        break
    matrix = [[99999]*(N+2)]
    matrix += [[99999] + list(map(int, input().split())) + [99999] for _ in range(N)]
    matrix += [[99999]*(N+2)]
    ans = 10*(N**2)

    print(f'Problem {t}:', dijkstra())
    t += 1