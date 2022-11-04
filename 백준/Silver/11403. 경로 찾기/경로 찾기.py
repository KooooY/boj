N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    visited = [0]*N
    Q = [i]

    while Q:
        item = Q.pop(0)
        for j in range(N):
            if not visited[j] and arr[item][j]:
                visited[j] = 1
                Q.append(j)

    print(*visited)