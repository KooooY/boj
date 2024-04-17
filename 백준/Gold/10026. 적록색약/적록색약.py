import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, color):
    global arr
    vistited = ''
    if color == 'R' or color == 'G':
        vistited = 'RG'
    else:
        vistited = 'X'
    arr[r][c] = vistited
    Q = [(r, c)]
    while Q:
        cur = Q.pop()
        for d in range(4):
            if 0 <= cur[0] + dr[d] < N and 0 <= cur[1] + dc[d] < N and arr[cur[0] + dr[d]][cur[1] + dc[d]] == color:
                arr[cur[0] + dr[d]][cur[1] + dc[d]] = vistited
                Q.append((cur[0] + dr[d], cur[1] + dc[d]))
    return

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
R = 0
G = 0
B = 0
RG = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] != 'X' and arr[i][j] != 'RG':
            if arr[i][j] == 'R':
                R += 1
            elif arr[i][j] == 'G':
                G += 1
            elif arr[i][j] == 'B':
                B += 1
            dfs(i, j, arr[i][j])

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'RG':
            dfs(i, j, arr[i][j])
            RG += 1

print(R+G+B, RG+B)