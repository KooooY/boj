N = int(input())
node = int(input())
graph = [[0]*N for _ in range(N)]

for _ in range(node):
    start, end = map(int, input().split())
    graph[start-1][end-1] = 1
    graph[end-1][start-1] = 1

Q = [0]
visited = {0}
while Q:
    item = Q.pop(0)
    for i in range(N):
        if graph[item][i] and i not in visited:
            Q.append(i)
            visited.add(i)

print(len(visited)-1)