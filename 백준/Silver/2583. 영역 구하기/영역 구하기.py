def bfs(y, x):
    Q = [(i, j)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    field = 1
    while Q:
        y, x = Q.pop()
        for n in range(4):
            ny, nx = y + dy[n], x + dx[n]
            if 0 <= ny < M and 0 <= nx < N and (ny, nx) not in visited:
                visited.add((ny, nx))
                Q.append((ny, nx))
                field += 1
    return field

M, N, K = map(int, input().split())

field_count = 0
field_size = []
visited = set()

for _ in range(K):
    p1, p2, p3, p4 = map(int, input().split())
    for r in range(p2, p4):
        for c in range(p1, p3):
            visited.add((r, c))

for i in range(M):
    for j in range(N):
        if (i, j) not in visited:
            visited.add((i,j))
            field_count += 1
            field_size.append(bfs(i, j))

print(field_count)
print(*sorted(field_size))
