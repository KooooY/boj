from collections import deque
import sys
input = sys.stdin.readline

def moveup(cur, count):
    global answer
    temp = [[0] * N for _ in range(N)]
    flag = [0] * N
    for i in range(N):
        new = deque()
        for j in range(N):
            if cur[j][i]:
                if cur[j][i] > answer:
                    answer = cur[j][i]
                if new:
                    if new[-1] == cur[j][i]:
                        new[-1] = str(cur[j][i] * 2)
                        if cur[j][i] * 2 > answer:
                            answer = cur[j][i] * 2
                        continue
                new.append(cur[j][i])
        idx = 0

        for k in new:
            if type(k) == int:
                if idx:
                    if temp[idx - 1][i] == k and not flag[idx - 1]:
                        temp[idx - 1][i] *= 2
                        flag[idx - 1] = 1
                        continue
            else:
                flag[idx] = 1
            temp[idx][i] = int(k)
            idx += 1
    if count == 5:
        return
    else:
        count += 1
        moveleft(temp, count)
        moveright(temp, count)
        movedown(temp, count)
        moveup(temp, count)

def movedown(cur, count):
    global answer
    temp = [[0] * N for _ in range(N)]
    flag = [0] * N
    for i in range(N):
        new = deque()
        for j in range(N - 1, -1, -1):
            if cur[j][i]:
                if new:
                    if new[-1] == cur[j][i]:
                        new[-1] = str(cur[j][i] * 2)
                        if cur[j][i] * 2 > answer:
                            answer = cur[j][i] * 2
                        continue
                new.append(cur[j][i])
        idx = N - 1
        for k in new:
            if type(k) == int:
                if idx < N - 1:
                    if temp[idx + 1][i] == k and not flag[idx + 1]:
                        temp[idx + 1][i] *= 2
                        flag[idx + 1] = 1
                        continue
            else:
                flag[idx] = 1

            temp[idx][i] = int(k)
            idx -= 1
    if count == 5:
        return
    else:
        count += 1
        moveleft(temp, count)
        moveright(temp, count)
        moveup(temp, count)
        movedown(temp, count)

def moveleft(cur, count):
    global answer
    temp = [[0] * N for _ in range(N)]
    flag = [0] * N
    for i in range(N):
        new = deque()
        for j in range(N):
            if cur[i][j]:
                if new:
                    if new[-1] == cur[i][j]:
                        new[-1] = str(cur[i][j] * 2)
                        if cur[i][j] * 2 > answer:
                            answer = cur[i][j] * 2
                        continue
                new.append(cur[i][j])
        idx = 0
        for k in new:
            if type(k) == int:
                if idx:
                    if temp[i][idx - 1] == k and not flag[idx - 1]:
                        temp[i][idx - 1] *= 2
                        flag[idx - 1] = 1
                        continue
            else:
                flag[idx] = 1
            temp[i][idx] = int(k)
            idx += 1
    if count == 5:
        return
    else:
        count += 1
        moveup(temp, count)
        movedown(temp, count)
        moveright(temp, count)
        moveleft(temp, count)

def moveright(cur, count):
    global answer
    temp = [[0] * N for _ in range(N)]
    flag = [0] * N
    for i in range(N):
        new = deque()
        for j in range(N - 1, -1, -1):
            if cur[i][j]:
                if new:
                    if new[-1] == cur[i][j]:
                        new[-1] = str(cur[i][j] * 2)
                        if cur[i][j] * 2 > answer:
                            answer = cur[i][j] * 2
                        continue
                new.append(cur[i][j])
        idx = N - 1
        for k in new:
            if type(k) == int:
                if idx < N - 1:
                    if temp[i][idx + 1] == k and not flag[idx + 1]:
                        temp[i][idx + 1] *= 2
                        flag[idx + 1] = 1
                        continue
            else:
                flag[idx] = 1
            temp[i][idx] = int(k)
            idx -= 1
    if count == 5:
        return
    else:
        count += 1
        moveup(temp, count)
        movedown(temp, count)
        moveleft(temp, count)
        moveright(temp, count)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

moveup(board, 1)
movedown(board, 1)
moveleft(board, 1)
moveright(board, 1)

print(answer)