from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

turn = {}

N = int(input())
m = [[0] * N for _ in range(N)]
for _ in range(int(input())):
	r, c = map(int,input().split())
	m[r-1][c-1] = -1
for _ in range(int(input())):
	x, c = input().split()
	turn[int(x)] = c
dir, time = 0, 0
body = deque([(0,0)])

while True:
	time += 1
	headx, heady = body[0][0], body[0][1]
	tailx, taily = body[-1][0], body[-1][1]
	headx, heady = headx + dx[dir], heady + dy[dir]
	if headx < 0 or headx >= N or heady < 0 or heady >= N or (headx, heady) in body:
		print(time)
		break
	if m[headx][heady] == -1:
		m[headx][heady] = 0
		body.appendleft((headx, heady))
	else:
		body.pop()
		body.appendleft((headx, heady))
	if time in turn:
		if dir == 0:
			dir = 3 if turn[time] == 'D' else 2
		elif dir == 1:
			dir = 2 if turn[time] == 'D' else 3
		elif dir == 2:
			dir = 0 if turn[time] == 'D' else 1
		elif dir == 3:
			dir = 1 if turn[time] == 'D' else 0