import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
answer = 'IMPOSSIBLE'
maze = []
jihoon = (0, 0, 0)
fires = set()

for i in range(R):
    temp = input().rstrip()
    for j in range(C):
        if temp[j] == 'J':
            jihoon = (i, j, 0)
        if temp[j] == 'F':
            fires.add((i, j))
    maze.append(list(temp))

Q = deque()
Q.append(jihoon)
Q.extend(fires)
jihoon_visited = {(jihoon[0], jihoon[1])}

while Q and answer == 'IMPOSSIBLE':
    cur = Q.popleft()
    if len(cur) == 3:
        cur_r, cur_c, dist = cur
        if (cur_r, cur_c) in fires:
            continue
        if not cur_r or cur_r == R - 1 or not cur_c or cur_c == C - 1:
            answer = dist + 1
            break
        for l in range(4):
            if 0 <= cur_r + dr[l] < R and 0 <= cur_c + dc[l] < C and (cur_r + dr[l], cur_c + dc[l]) not in jihoon_visited and (cur[0] + dr[l], cur[1] + dc[l]) not in fires and maze[cur_r + dr[l]][cur_c + dc[l]] == '.':
                jihoon_visited.add((cur_r + dr[l], cur_c + dc[l]))
                Q.append((cur_r + dr[l], cur_c + dc[l], dist + 1))

    else:
        for k in range(4):
            if 0 <= cur[0] + dr[k] < R and 0 <= cur[1] + dc[k] < C and (cur[0] + dr[k], cur[1] + dc[k]) not in fires and (maze[cur[0] + dr[k]][cur[1] + dc[k]] == '.' or maze[cur[0] + dr[k]][cur[1] + dc[k]] == 'J'):
                fires.add((cur[0] + dr[k], cur[1] + dc[k]))
                Q.append((cur[0] + dr[k], cur[1] + dc[k]))

print(answer)