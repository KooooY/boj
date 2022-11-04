dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]

Q = [(0,0), 'a']
visited = {(0,0)}
cnt = 1
flag = 1

while Q != ['a'] and flag:
    item = Q.pop(0)
    if item == 'a':
        Q.append('a')
        cnt += 1
        continue
    r = item[0]
    c = item[1]
    for i in range(4):
        if (r+dr[i], c+dc[i]) not in visited and 0 <= r+dr[i] < N and 0 <= c+dc[i] < M and maze[r+dr[i]][c+dc[i]]:
            Q.append((r+dr[i], c+dc[i]))
            visited.add((r+dr[i], c+dc[i]))
            if (r+dr[i], c+dc[i]) == (N-1, M-1):
                cnt += 1
                flag = 0
                break

print(cnt)