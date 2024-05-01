import sys
input = sys.stdin.readline

N, M = map(int, input().split())

MAP = []
for i in range(N):
    row = list(map(int, input().split()))
    MAP.append(row)

check = [[True for i in range(M)] for _ in range(N)] 
moves =[[0,1],[0,-1],[1,0],[-1,0]]
max_result = -1

def dfs(row, col, now, cnt):
    global max_result 

    if cnt == 4:
        max_result = max(max_result, now)
        return
	
    for drow, dcol in moves:
        nrow = row + drow
        ncol = col + dcol
        if 0 <= nrow < N and 0 <= ncol < M:
            if check[nrow][ncol]:
                check[nrow][ncol] = False
                dfs(nrow, ncol, now+MAP[nrow][ncol], cnt+1)
                check[nrow][ncol] = True

def except_dfs(row, col):
    center = MAP[row][col]
    wings = 4
    min_result = 100000
    
    for drow, dcol in moves:
        nrow = row + drow
        ncol = col + dcol
        if wings ==2:
            return 0

        if not(0 <= nrow < N and 0 <= ncol < M):
            wings -=1
            continue
        
        center += MAP[nrow][ncol]
        if MAP[nrow][ncol] < min_result:
            min_result = MAP[nrow][ncol]
    
    if wings == 4:
        center -= min_result
    
    return center

for i in range(N):
    for j in range(M):
        check[i][j] = False
        dfs(i, j, MAP[i][j], 1)
        check[i][j] = True
        temp = except_dfs(i,j)
        max_result = max(temp, max_result)

print(max_result)