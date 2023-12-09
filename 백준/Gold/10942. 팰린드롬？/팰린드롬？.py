import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]
M = int(input())

for i in range(N):
    dp[i][i] = 1

for j in range(N-1):
    if num_list[j] == num_list[j+1]:
        dp[j][j+1] = 1

for length in range(2, N):
    for k in range(N-length):
        if num_list[k] == num_list[k+length] and dp[k+1][k+length-1]:
            dp[k][k+length] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])