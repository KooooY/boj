import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())
    answer = 0
    Q = deque()
    Q.append(graph[v])
    visited = {v}

    while Q:
        current = Q.popleft()
        for i in current:
            if i[1] >= k and i[0] not in visited:
                Q.append(graph[i[0]])
                visited.add(i[0])
                answer += 1

    print(answer)