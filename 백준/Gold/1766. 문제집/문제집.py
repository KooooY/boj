import sys
from collections import deque
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
topology = [[] for _ in range(N + 1)]
count = [0] * (N + 1)
answer = []

for _ in range(M):
    A, B = map(int, input().split())
    topology[A].append(B)
    count[B] += 1

Q = []

for i in range(1, N + 1):
    if not count[i]:
        heapq.heappush(Q, i)

while Q:
    cur = heapq.heappop(Q)
    answer.append(cur)
    for t in topology[cur]:
        count[t] -= 1
        if not count[t]:
            heapq.heappush(Q, t)

print(*answer)