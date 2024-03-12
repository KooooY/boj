from collections import deque
import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = int(input())
K = int(input())
apple = {tuple(map(int, input().split())) for _ in range(K)}
L = int(input())
dd = [tuple(map(str, input().split())) for _ in range(L)]

snake = 1
sec = 0
direction = 1
dir_change = 0
head = (0, 0)
flag = 1

path = deque()
path.append((0, 0))

while flag:
    sec += 1
    next_path = (head[0] + dr[direction], head[1] + dc[direction])
    if 0 <= next_path[0] < N and 0 <= next_path[1] < N and next_path not in path:
        path.appendleft(next_path)
        head = next_path
        if (next_path[0] + 1, next_path[1] + 1) in apple:
            apple.remove((next_path[0] + 1, next_path[1] + 1))
            snake += 1
        else:
            path.pop()
    else:
        flag = 0
        break

    if dir_change < L and sec == int(dd[dir_change][0]):
        if dd[dir_change][1] == 'L':
            direction -= 1
        else:
            direction += 1
        direction = direction % 4
        dir_change += 1

print(sec)