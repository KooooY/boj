import sys
input = sys.stdin.readline

dr = [1, 0, 1, -1]
dc = [0, 1, 1, 1]

N, M = map(int, input().split())
K = int(input())
hole_info = {tuple(map(int, input().split())) for _ in range(K)}

hive = [[0]*M for _ in range(N)]
hive[0][0] = 1

for c in range(M):
    if c%2:
        for r in range(N):
            if (r+1, c+1) in hole_info:
                continue
            for i in [0,1,2]:
                if 0 <= r+dr[i] < N and 0 <= c+dc[i] < M:
                    hive[r+dr[i]][c+dc[i]] += hive[r][c]
    else:
        for r in range(N):
            if (r+1, c+1) in hole_info:
                continue
            for i in [0,1,3]:
                if 0 <= r+dr[i] < N and 0 <= c+dc[i] < M:
                    hive[r+dr[i]][c+dc[i]] += hive[r][c]

print(hive[N-1][M-1]%(10**9+7))