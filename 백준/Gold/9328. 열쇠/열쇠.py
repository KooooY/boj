from collections import deque
import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for _ in range(T):
    h, w = map(int, input().split())
    matrix = [list(input()) for _ in range(h)]
    keys = set(list(input()))
    keys.discard('0')
    start = set()
    doors = dict()
    answer = set()
    visited = set()

    for i in range(h):
        for j in range(w):
            if (not i or i == h - 1 or not j or j == w - 1) and matrix[i][j] != '*':
                if 65 <= ord(matrix[i][j]) <= 90:
                    if matrix[i][j] in doors:
                        doors[matrix[i][j]].add((i, j))
                    else:
                        doors[matrix[i][j]] = {(i, j)}
                else:
                    if 97 <= ord(matrix[i][j]) <= 122:
                        keys.add(matrix[i][j])
                    if matrix[i][j] == '$':
                        answer.add((i, j))
                    start.add((i, j))

    # for door in doors:
    #     if door.lower() in keys:
    #         start.update(doors[door])

    for k in keys:
        if k.upper() in doors:
            start.update(doors[k.upper()])

    for s in start:
        Q = deque()
        Q.append(s)
        visited.add(s)
        while Q:
            r, c = Q.popleft()
            for k in range(4):
                if 0 <= r + dr[k] < h and 0 <= c + dc[k] < w and matrix[r + dr[k]][c + dc[k]] != '*' and (r + dr[k], c + dc[k]) not in visited:
                    if 65 <= ord(matrix[r + dr[k]][c + dc[k]]) <= 90:
                        if matrix[r + dr[k]][c + dc[k]].lower() in keys:
                            visited.add((r + dr[k], c + dc[k]))
                            Q.append((r + dr[k], c + dc[k]))
                        else:
                            if matrix[r + dr[k]][c + dc[k]] in doors:
                                doors[matrix[r + dr[k]][c + dc[k]]].add((r + dr[k], c + dc[k]))
                            else:
                                doors[matrix[r + dr[k]][c + dc[k]]] = {(r + dr[k], c + dc[k])}
                    else:
                        visited.add((r + dr[k], c + dc[k]))
                        Q.append((r + dr[k], c + dc[k]))
                        if 97 <= ord(matrix[r + dr[k]][c + dc[k]]) <= 122:
                            keys.add(matrix[r + dr[k]][c + dc[k]])
                            if matrix[r + dr[k]][c + dc[k]].upper() in doors:
                                for d in doors[matrix[r + dr[k]][c + dc[k]].upper()]:
                                    if d not in visited:
                                        visited.add(d)
                                        Q.append(d)
                        elif matrix[r + dr[k]][c + dc[k]] == '$':
                            answer.add((r + dr[k], c + dc[k]))

    print(len(answer))
