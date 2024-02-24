import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C, T = map(int, input().split())
answer = 2

air_purifier = 0
matrix = []
for i in range(R):
    temp = list(map(int, input().split()))
    if temp[0] == -1:
        air_purifier = i
    matrix.append(temp)

for _ in range(T):
    temp_matrix = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if matrix[r][c] > 0:
                temp_matrix[r][c] += matrix[r][c]
                for d in range(4):
                    if 0 <= r + dr[d] < R and 0 <= c + dc[d] < C and matrix[r + dr[d]][c + dc[d]] > -1:
                        temp_matrix[r + dr[d]][c + dc[d]] += matrix[r][c] // 5
                        temp_matrix[r][c] -= matrix[r][c] // 5

    for k in range(air_purifier - 2, 0, -1):
        temp_matrix[k][0] = temp_matrix[k - 1][0]
    temp_matrix[0] = temp_matrix[0][1:] + [temp_matrix[1][C - 1]]
    for l in range(air_purifier - 1):
        temp_matrix[l][C - 1] = temp_matrix[l + 1][C - 1]
    temp_matrix[air_purifier - 1] = [-1] + temp_matrix[air_purifier - 1][:C - 1]
    for m in range(air_purifier + 1, R - 1):
        temp_matrix[m][0] = temp_matrix[m + 1][0]
    temp_matrix[R - 1] = temp_matrix[R - 1][1:] + [temp_matrix[R - 2][C - 1]]
    for n in range(R - 1, air_purifier, -1):
        temp_matrix[n][C - 1] = temp_matrix[n - 1][C - 1]
    temp_matrix[air_purifier] = [-1] + temp_matrix[air_purifier][:C - 1]
    matrix = temp_matrix

for p in range(R):
    answer += sum(matrix[p])

print(answer)