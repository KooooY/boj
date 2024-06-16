from collections import deque
import sys
input = sys.stdin.readline

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, input().split())
nutrient_info = [list(map(int, input().split())) for _ in range(N)]
field = [[[5, deque(), deque()] for _ in range(N)] for _ in range(N)]
answer = 0

for _ in range(M):
    x, y, z = map(int, input().split())
    field[x - 1][y - 1][2].append(z)

for _ in range(K):
    answer = 0
    breeding_tree = []
    for i in range(N):
        for j in range(N):
            field[i][j][1] = field[i][j][2]
            field[i][j][2] = deque()
            nutrient = 0
            while field[i][j][1]:
                age = field[i][j][1].popleft()
                if field[i][j][0] >= age:
                    field[i][j][0] -= age
                    field[i][j][2].append(age + 1)
                    answer += 1
                    if not (age + 1) % 5:
                        breeding_tree.append((i, j))
                else:
                    nutrient += age // 2
            field[i][j][0] += nutrient + nutrient_info[i][j]

    for tree in breeding_tree:
        for k in range(8):
            if 0 <= tree[0] + dr[k] < N and 0 <= tree[1] + dc[k] < N:
                field[tree[0] + dr[k]][tree[1] + dc[k]][2].appendleft(1)
                answer += 1

print(answer)