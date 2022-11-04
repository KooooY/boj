N, M = map(int, input().split())
friendship = [[0]*(N+1) for _ in range(N+1)]
friendship_sum = [999999999999]

for _ in range(M):
    start, end = map(int, input().split())
    friendship[start][end] = 1
    friendship[end][start] = 1

for i in range(1, N+1):
    Q = [i, 'a']
    visited = [i]
    cnt = 1
    total = 0

    while Q != ['a']:
        item = Q.pop(0)

        if item == 'a':
            Q.append('a')
            cnt += 1
            continue

        for destination in range(1, N+1):
            if destination not in visited and friendship[item][destination]:
                visited.append(destination)
                Q.append(destination)
                total += cnt

    friendship_sum.append(total)

print(friendship_sum.index(min(friendship_sum)))