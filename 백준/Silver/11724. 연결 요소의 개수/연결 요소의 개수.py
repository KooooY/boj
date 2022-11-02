import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0]*N for _ in range(N)]
visited = set()
cnt = 0

for _ in range(M):
    start, end = map(int, input().split())
    graph[start-1][end-1] = 1
    graph[end-1][start-1] = 1

for i in range(N):
    if i not in visited:
        cnt += 1
        stack = [i]
        visited.add(i)
        while stack:
            current = stack.pop()
            for j in range(N):
                if graph[current][j] and j not in visited:
                    stack.append(j)
                    visited.add(j)

print(cnt)