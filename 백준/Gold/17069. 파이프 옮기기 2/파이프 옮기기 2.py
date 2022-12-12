N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
check = []

for _ in range(N):
    temp = []
    for _ in range(N):
        temp.append([0, 0, 0])      #가로 세로 대각선
    check.append(temp)

check[0][1] = [1, 0, 0]
for i in range(N):
    for j in range(1, N):
        if check[i][j][0]:
            if j+1 < N and not arr[i][j+1]:
                check[i][j+1][0] += check[i][j][0]
            if j+1 < N and i+1 < N and not arr[i][j+1] and not arr[i+1][j] and not arr[i+1][j+1]:
                check[i+1][j+1][2] += check[i][j][0]
        if check[i][j][1]:
            if i+1 < N and not arr[i+1][j]:
                check[i+1][j][1] += check[i][j][1]
            if j+1 < N and i+1 < N and not arr[i][j+1] and not arr[i+1][j] and not arr[i+1][j+1]:
                check[i+1][j+1][2] += check[i][j][1]
        if check[i][j][2]:
            if j+1 < N and not arr[i][j+1]:
                check[i][j+1][0] += check[i][j][2]
            if i + 1 < N and not arr[i+1][j]:
                check[i+1][j][1] += check[i][j][2]
            if j+1 < N and i+1 < N and not arr[i][j+1] and not arr[i+1][j] and not arr[i+1][j+1]:
                check[i+1][j+1][2] += check[i][j][2]

print(sum(check[N-1][N-1]))