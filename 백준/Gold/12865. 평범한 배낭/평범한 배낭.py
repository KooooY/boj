import sys
input = sys.stdin.readline

N, K = map(int, input().split())
value_info = [tuple(map(int, input().split())) for _ in range(N)]
sack = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        W = value_info[i-1][0]
        V = value_info[i-1][1]
        if W > j:
            sack[i][j] = sack[i-1][j]
        else:
            sack[i][j] = max(sack[i-1][j-W]+V, sack[i-1][j])

print(sack[N][K])