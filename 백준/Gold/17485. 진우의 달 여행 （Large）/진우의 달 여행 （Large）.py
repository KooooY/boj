import sys
input = sys.stdin.readline

dc = [-1, 0, 1]

N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
dp = []
end = []

for _ in range(N):
    temp = []
    for _ in range(M):
        temp.append([9999999, 9999999, 9999999])
    dp.append(temp)

for s in range(M):
    dp[0][s] = [space[0][s]]*3

for i in range(N-1):
    for j in range(M):
        for idx in range(3):
            for direction in range(3):
                if 0 <= j+dc[direction] < M and idx != direction:
                    if i+1 == N-1:
                        end.append(dp[i][j][idx] + space[i+1][j+dc[direction]])
                    else:
                        if dp[i+1][j+dc[direction]][direction] > dp[i][j][idx] + space[i+1][j+dc[direction]]:
                            dp[i+1][j+dc[direction]][direction] = dp[i][j][idx] + space[i+1][j+dc[direction]]

end.sort()
print(end[0])