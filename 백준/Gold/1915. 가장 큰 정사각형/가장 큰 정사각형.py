n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
arr_sum = [[0]*(m+1) for _ in range(n+1)]
max_sum = arr[0][0]
start = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        arr_sum[i][j] = arr[i-1][j-1] + arr_sum[i-1][j] + arr_sum[i][j-1] - arr_sum[i-1][j-1]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            temp_max = arr[i][j]
            end = min(n-i+1, m-j+1)
            for r in range(start, end):
                temp = arr_sum[i+r][j+r] - arr_sum[i][j+r] - arr_sum[i+r][j] + arr_sum[i][j]
                if temp == r**2 and temp > temp_max:
                    temp_max = temp
                    start = r+1
            if temp_max > max_sum:
                max_sum = temp_max

print(max_sum)