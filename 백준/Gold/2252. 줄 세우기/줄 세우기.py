import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
node_info = [[] for _ in range(N + 1)]
topology = [0] * (N + 1)
answer = []

for _ in range(M):
    front, back = map(int, input().split())
    node_info[front].append(back)
    topology[back] += 1

Q = deque()
for i in range(1, N + 1):
    if not topology[i]:
        Q.append(i)

while Q:
    cur = Q.popleft()
    answer.append(cur)
    for nd in node_info[cur]:
        topology[nd] -= 1
        if not topology[nd]:
            Q.append(nd)

print(*answer)