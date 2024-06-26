import sys
import heapq
input = sys.stdin.readline

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

N, M, k = map(int, input().split())
sea = []
shark_cur = dict()
for r in range(N):
    temp_sea = list(map(int, input().split()))
    for c in range(N):
        if temp_sea[c]:
            shark_cur[temp_sea[c]] = [r, c]
            temp_sea[c] = (temp_sea[c], 0)
    sea.append(temp_sea)

shark_cur_dir = list(map(int, input().split()))
for shark in range(M):
    shark_cur[shark + 1].append(shark_cur_dir[shark])

dir_priority = dict()
for i in range(1, M + 1):
    temp = []
    for _ in range(4):
        temp.append(tuple(map(int, input().split())))
    dir_priority[i] = temp

turn = 1
living_shark = M
while turn < 1001:
    cur_sea = dict()
    for sh in shark_cur:
        cur_r, cur_c, cur_d = shark_cur[sh][0], shark_cur[sh][1], shark_cur[sh][2]
        flag = 1
        for di in dir_priority[sh][cur_d - 1]:
            if 0 <= cur_r + dr[di] < N and 0 <= cur_c + dc[di] < N:
                if sea[cur_r + dr[di]][cur_c + dc[di]] and turn - sea[cur_r + dr[di]][cur_c + dc[di]][1] > k:
                    sea[cur_r + dr[di]][cur_c + dc[di]] = 0
                if not sea[cur_r + dr[di]][cur_c + dc[di]]:
                    if (cur_r + dr[di], cur_c + dc[di]) in cur_sea:
                        heapq.heappush(cur_sea[(cur_r + dr[di], cur_c + dc[di])], (sh, di))
                    else:
                        cur_sea[(cur_r + dr[di], cur_c + dc[di])] = [(sh, di)]
                    flag = 0
                    break
        if flag:
            for di in dir_priority[sh][cur_d - 1]:
                if 0 <= cur_r + dr[di] < N and 0 <= cur_c + dc[di] < N:
                    if sea[cur_r + dr[di]][cur_c + dc[di]][0] == sh:
                        cur_sea[(cur_r + dr[di], cur_c + dc[di])] = [(sh, di)]
                        flag = 0
                        break

    for cur in cur_sea:
        survived = heapq.heappop(cur_sea[cur])
        sea[cur[0]][cur[1]] = (survived[0], turn)
        shark_cur[survived[0]] = [cur[0], cur[1], survived[1]]
        for dead in cur_sea[cur]:
            del shark_cur[dead[0]]
            living_shark -= 1
    if living_shark < 2:
        break
    turn += 1

if turn < 1001:
    print(turn)
else:
    print(-1)