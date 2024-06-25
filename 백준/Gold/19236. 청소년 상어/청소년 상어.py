import sys
from copy import deepcopy
input = sys.stdin.readline

def shark_move(shark, shark_dir, cnt, fish, sea, num):
    global answer
    new_shark = (0, 0)
    new_fish = dict()
    new_sea = [[0 for _ in range(4)] for _ in range(4)]

    for f in range(1, 17):
        fish_cur_r = 0
        fish_cur_c = 0
        fish_cur_d = 0
        new = 0
        if f in new_fish:

            fish_cur_r, fish_cur_c, fish_cur_d = new_fish[f][0], new_fish[f][1], new_fish[f][2]
            new = 1
        elif f in fish and fish[f]:
            fish_cur_r, fish_cur_c, fish_cur_d = fish[f][0], fish[f][1], fish[f][2]
        else:
            continue

        if not new:
            new_sea[fish_cur_r][fish_cur_c] = f
            new_fish[f] = fish[f]

        for d in range(8):
            if 0 <= fish_cur_r + dr[(fish_cur_d + d) % 8] < 4 and 0 <= fish_cur_c + dc[(fish_cur_d + d) % 8] < 4:
                if new_sea[fish_cur_r + dr[(fish_cur_d + d) % 8]][fish_cur_c + dc[(fish_cur_d + d) % 8]]:
                    other_dir = new_fish[new_sea[fish_cur_r + dr[(fish_cur_d + d) % 8]][fish_cur_c + dc[(fish_cur_d + d) % 8]]][2]
                    new_fish[new_sea[fish_cur_r + dr[(fish_cur_d + d) % 8]][fish_cur_c + dc[(fish_cur_d + d) % 8]]] = (fish_cur_r, fish_cur_c, other_dir)
                    new_fish[f] = (fish_cur_r + dr[(fish_cur_d + d) % 8], fish_cur_c + dc[(fish_cur_d + d) % 8], (fish_cur_d + d) % 8)
                    new_sea[fish_cur_r][fish_cur_c] = new_sea[fish_cur_r + dr[(fish_cur_d + d) % 8]][fish_cur_c + dc[(fish_cur_d + d) % 8]]
                    new_sea[fish_cur_r + dr[(fish_cur_d + d) % 8]][fish_cur_c + dc[(fish_cur_d + d) % 8]] = f
                    if not new:
                        sea[fish_cur_r][fish_cur_c] = 0
                    break
                elif sea[fish_cur_r + dr[(fish_cur_d + d) % 8]][fish_cur_c + dc[(fish_cur_d + d) % 8]]:
                    other_dir = fish[sea[fish_cur_r + dr[(fish_cur_d + d) % 8]][fish_cur_c + dc[(fish_cur_d + d) % 8]]][2]
                    new_fish[sea[fish_cur_r + dr[(fish_cur_d + d) % 8]][fish_cur_c + dc[(fish_cur_d + d) % 8]]] = (fish_cur_r, fish_cur_c, other_dir)
                    new_fish[f] = (fish_cur_r + dr[(fish_cur_d + d) % 8], fish_cur_c + dc[(fish_cur_d + d) % 8], (fish_cur_d + d) % 8)
                    new_sea[fish_cur_r][fish_cur_c], new_sea[fish_cur_r + dr[(fish_cur_d + d) % 8]][fish_cur_c + dc[(fish_cur_d + d) % 8]] = sea[fish_cur_r + dr[(fish_cur_d + d) % 8]][fish_cur_c + dc[(fish_cur_d + d) % 8]], f
                    sea[fish_cur_r + dr[(fish_cur_d + d) % 8]][fish_cur_c + dc[(fish_cur_d + d) % 8]], sea[fish_cur_r][fish_cur_c] = 0, 0
                    break
                elif (fish_cur_r + dr[(fish_cur_d + d) % 8], fish_cur_c + dc[(fish_cur_d + d) % 8]) != shark:
                    new_fish[f] = (fish_cur_r + dr[(fish_cur_d + d) % 8], fish_cur_c + dc[(fish_cur_d + d) % 8], (fish_cur_d + d) % 8)
                    new_sea[fish_cur_r + dr[(fish_cur_d + d) % 8]][fish_cur_c + dc[(fish_cur_d + d) % 8]] = f
                    new_sea[fish_cur_r][fish_cur_c] = 0
                    sea[fish_cur_r][fish_cur_c] = 0
                    break
    for k in range(1, 5):
        new_r, new_c = shark[0] + k * dr[shark_dir], shark[1] + k * dc[shark_dir]
        if 0 <= new_r < 4 and 0 <= new_c < 4:
            if new_sea[new_r][new_c]:
                new_shark = (new_r, new_c)
                new_shark_dir = new_fish[new_sea[new_r][new_c]][2]
                new_cnt = cnt + new_sea[new_r][new_c]
                next_sea = deepcopy(new_sea)
                next_sea[new_r][new_c] = 0
                info_save = (new_sea[new_r][new_c], new_fish[new_sea[new_r][new_c]])
                del new_fish[new_sea[new_r][new_c]]
                shark_move(new_shark, new_shark_dir, new_cnt, new_fish, next_sea, num + 1)
                new_fish[info_save[0]] = info_save[1]
                new_sea[new_r][new_c] = info_save[0]
        else:
            break

    if new_shark == (0, 0):
        if cnt > answer:
            answer = cnt
        return


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

sea = []
fish = dict()
living_fish = {f for f in range(1, 17)}

for j in range(4):
    temp = list(map(int, input().split()))
    fish_info = []
    for i in range(4):
        a, b = temp[2 * i], temp[2 * i + 1] - 1
        fish_info.append(a)
        fish[a] = (j, i, b)
    sea.append(fish_info)

shark = (0, 0)
shark_dir = fish[sea[0][0]][2]
answer = sea[0][0]
del fish[sea[0][0]]
sea[0][0] = 0

shark_move(shark, shark_dir, answer, fish, sea, 1)

print(answer)