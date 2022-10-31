N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr_sum = [[0]*(M+1) for _ in range(N+1)]
max_sum = arr[0][0]

for i in range(1, N+1):
    for j in range(1, M+1):
        arr_sum[i][j] = arr[i-1][j-1] + arr_sum[i-1][j] + arr_sum[i][j-1] - arr_sum[i-1][j-1]

for i in range(N):
    for j in range(M):
        temp_max = arr[i][j]
        for r in range(i+1, N+1):
            for c in range(j+1, M+1):
                temp = arr_sum[r][c] - arr_sum[i][c] - arr_sum[r][j] + arr_sum[i][j]
                if temp > temp_max:
                    temp_max = temp
        if temp_max > max_sum:
            max_sum = temp_max

print(max_sum)