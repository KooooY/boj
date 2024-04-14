import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())
sea = []
shark = (-1, 0, 0)
shark_size = 2
eating_count = 0
answer = 0

for i in range(N):
    temp = list(map(int, input().split()))
    if shark == (-1, 0, 0) and 9 in temp:
        shark = (i, temp.index(9), 0)
        temp[shark[1]] = 0
    sea.append(temp)

while True:
    Q = deque()
    Q.append(shark)
    eatable_dist = N * N
    eatable_fish = set()
    visited = {shark}
    while Q:
        cur_r, cur_c, dist = Q.popleft()
        if dist > eatable_dist:
            break
        for j in range(4):
            if 0 <= cur_r + dr[j] < N and 0 <= cur_c + dc[j] < N and (cur_r + dr[j], cur_c + dc[j]) not in visited:
                if 0 <= sea[cur_r + dr[j]][cur_c + dc[j]] <= shark_size:
                    visited.add((cur_r + dr[j], cur_c + dc[j]))
                    if 0 < sea[cur_r + dr[j]][cur_c + dc[j]] < shark_size and dist + 1 <= eatable_dist:
                        eatable_dist = dist + 1
                        eatable_fish.add((cur_r + dr[j], cur_c + dc[j], 0))
                    else:
                        Q.append((cur_r + dr[j], cur_c + dc[j], dist + 1))
    if eatable_fish:
        target = (N, N, 0)
        for fish in eatable_fish:
            if (fish[0] < target[0]) or (fish[0] == target[0] and fish[1] < target[1]):
                target = fish
        sea[target[0]][target[1]] = 0
        shark = target
        answer += eatable_dist
        eating_count += 1
        if eating_count == shark_size:
            shark_size += 1
            eating_count = 0
    else:
        break

print(answer)