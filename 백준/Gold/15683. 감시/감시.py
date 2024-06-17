import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def dfs(cctv_info, visited):
    global answer
    if cctv_info == len(cctv):
        if N * M - len(visited) < answer:
            answer = N * M - len(visited)
        return

    number, cur_r, cur_c = cctv[cctv_info]
    if number == 5:
        new_visited = set()
        for di in range(4):
            c_r, c_c = cur_r + dr[di], cur_c + dc[di]
            while 0 <= c_r < N and 0 <= c_c < M:
                if matrix[c_r][c_c] == 6:
                    break
                else:
                    new_visited.add((c_r, c_c))
                    c_r, c_c = c_r + dr[di], c_c + dc[di]
        new_visited |= visited
        dfs(cctv_info + 1, new_visited)

    if number == 4:
        for d in range(4):
            new_visited = set()
            for di in range(4):
                if di != d:
                    c_r, c_c = cur_r + dr[di], cur_c + dc[di]
                    while 0 <= c_r < N and 0 <= c_c < M:
                        if matrix[c_r][c_c] == 6:
                            break
                        else:
                            new_visited.add((c_r, c_c))
                            c_r, c_c = c_r + dr[di], c_c + dc[di]
            new_visited |= visited
            dfs(cctv_info + 1, new_visited)

    if number == 3:
        three_case = [(0, 1), (1, 2), (2, 3), (0, 3)]
        for three in three_case:
            new_visited = set()
            for di in three:
                c_r, c_c = cur_r + dr[di], cur_c + dc[di]
                while 0 <= c_r < N and 0 <= c_c < M:
                    if matrix[c_r][c_c] == 6:
                        break
                    else:
                        new_visited.add((c_r, c_c))
                        c_r, c_c = c_r + dr[di], c_c + dc[di]
            new_visited |= visited
            dfs(cctv_info + 1, new_visited)

    if number == 2:
        for d in range(2):
            new_visited = set()
            for di in range(4):
                if di % 2 != d:
                    c_r, c_c = cur_r + dr[di], cur_c + dc[di]
                    while 0 <= c_r < N and 0 <= c_c < M:
                        if matrix[c_r][c_c] == 6:
                            break
                        else:
                            new_visited.add((c_r, c_c))
                            c_r, c_c = c_r + dr[di], c_c + dc[di]
            new_visited |= visited
            dfs(cctv_info + 1, new_visited)

    if number == 1:
        for di in range(4):
            new_visited = set()
            c_r, c_c = cur_r + dr[di], cur_c + dc[di]
            while 0 <= c_r < N and 0 <= c_c < M:
                if matrix[c_r][c_c] == 6:
                    break
                else:
                    new_visited.add((c_r, c_c))
                    c_r, c_c = c_r + dr[di], c_c + dc[di]
            new_visited |= visited
            dfs(cctv_info + 1, new_visited)


N, M = map(int, input().split())
cctv = []
matrix = []
visited = set()
answer = N * M

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j]:
            if temp[j] < 6:
                cctv.append((temp[j], i, j))
            visited.add((i, j))
    matrix.append(temp)

dfs(0, visited)
print(answer)