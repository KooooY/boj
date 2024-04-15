import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

while True:
    Q = deque()
    Q.append((0, 0))
    visited = {(0, 0)}
    cheeses = set()
    melting_cheese = set()
    while Q:
        cur_r, cur_c = Q.popleft()
        for i in range(4):
            if 0 <= cur_r + dr[i] < N and 0 <= cur_c + dc[i] < M and (cur_r + dr[i], cur_c + dc[i]) not in visited:
                if not arr[cur_r + dr[i]][cur_c + dc[i]]:
                    visited.add((cur_r + dr[i], cur_c + dc[i]))
                    Q.append((cur_r + dr[i], cur_c + dc[i]))
                else:
                    if (cur_r + dr[i], cur_c + dc[i]) in cheeses:
                        melting_cheese.add((cur_r + dr[i], cur_c + dc[i]))
                    else:
                        cheeses.add((cur_r + dr[i], cur_c + dc[i]))
    if melting_cheese:
        answer += 1
        for cheese in melting_cheese:
            arr[cheese[0]][cheese[1]] = 0
    else:
        break

print(answer)