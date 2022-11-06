dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def combi(idx, sidx):
    if sidx == M:
        combi_list.append(sel[:])
        return
    if idx == chicken_cnt:
        return
    sel[sidx] = arr[idx]
    combi(idx+1, sidx+1)
    combi(idx+1, sidx)


N, M = map(int, input().split())
city_arr = [list(map(int, input().split())) for _ in range(N)]
chicken_cnt = 0
home_cnt = 0
chicken_road = {}

for i in range(N):
    for j in range(N):
        if city_arr[i][j] == 1:
            home_cnt += 1
            Q = [(i, j)]
            visited = {(i, j)}
            while Q:
                item = Q.pop(0)
                for k in range(4):
                    r = item[0]+dr[k]
                    c = item[1]+dc[k]
                    if (r, c) not in visited and 0 <= r < N and 0 <= c < N:
                        Q.append((r, c))
                        visited.add((r, c))
                        if city_arr[r][c] == 2:
                            dist = abs(i-r) + abs(j-c)
                            if (r, c) in chicken_road:
                                chicken_road[(r, c)] += [dist]
                            else:
                                chicken_cnt += 1
                                chicken_road[(r, c)] = [dist]

sel = [0]*M
arr = [l for l in chicken_road]
combi_list = []

combi(0, 0)

min_path = 9999999999999999999999999
for chick in combi_list:
    road_cnt = 0
    total = [chicken_road[key] for key in chick]
    total_zip = list(zip(*total[::-1]))
    for h in range(home_cnt):
        road_cnt += min(total_zip[h])
    if road_cnt < min_path:
        min_path = road_cnt

print(min_path)