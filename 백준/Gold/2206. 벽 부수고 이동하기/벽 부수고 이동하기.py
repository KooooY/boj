import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
m = [list(input().rstrip()) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]
q = deque()
 
def bfs():
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    while q:
        b, x, y = q.popleft()
        if (x, y) == (N-1, M-1):
            return visited[b][x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[b][nx][ny]:
                if m[nx][ny] == '0':
                    visited[b][nx][ny] = visited[b][x][y] + 1
                    q.append((b, nx,ny))
                if m[nx][ny] == '1' and b == 0:
                    visited[1][nx][ny] = visited[b][x][y] + 1
                    q.append((b+1, nx, ny))
    return -1
 
print(bfs())