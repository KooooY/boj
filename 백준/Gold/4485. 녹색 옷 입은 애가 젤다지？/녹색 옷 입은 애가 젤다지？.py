from collections import deque
tc = 1
while True:
    N = int(input())
    if not N:
        break

    cave = [list(map(int, input().split())) for _ in range(N)]

    dist = [[987654321] * N for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))
    dist[0][0] = cave[0][0]

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < N and 0 <= ny < N:
                if dist[y][x] + cave[ny][nx] < dist[ny][nx]:
                    queue.append((ny, nx))
                    dist[ny][nx] = dist[y][x] + cave[ny][nx]

    print(f"Problem {tc}: {dist[N-1][N-1]}")
    tc += 1
