# 가로와 세로를 입력을 받고
# 치즈의 4면 중 하나라도 0이면 cnt++
# 전체 개수가 0 인 경우 마지막 cnt 와 time 을 출력
from collections import deque

r, c = map(int, input().split())
ch = [list(map(int, input().split())) for i in range(r)]

total = 0
for i in range(r):
    total += sum(ch[i])

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

ans, t = 0, 0
while total > 0:
    cnt = 0
    visited = []
    visit = set()
    dq = deque()
    dq.append([0, 0])
    while dq:
        [y, x] = dq.pop()
        visit.add((y, x))
        for direc in range(4):
            ny = y + dy[direc]
            nx = x + dx[direc]
            if 0 <= nx < c and 0 <= ny < r:
                if ch[ny][nx]:
                    if [ny, nx] not in visited:
                        visited.append([ny, nx])
                else:
                    if (ny, nx) not in visit:
                        visit.add((ny, nx))
                        dq.append([ny, nx])
    total -= len(visited)
    ans = len(visited)
    while visited:
        [yy, xx] = visited.pop()
        ch[yy][xx] = 0

    t += 1

print(t)
print(ans)
