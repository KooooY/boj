import sys
import heapq
input = sys.stdin.readline

n = int(input())
stars = [[] for _ in range(n)]
star_info = [tuple(map(float, input().split())) for _ in range(n)]
mst = set()
answer = 0

for i in range(n):
    for j in range(i + 1, n):
        dist = (((star_info[i][0] - star_info[j][0]) ** 2) + ((star_info[i][1] - star_info[j][1]) ** 2)) ** 0.5
        stars[i].append((dist, j))
        stars[j].append((dist, i))

Q = [(0, 0)]

while Q:
    cur_dist, cur_star = heapq.heappop(Q)
    if cur_star not in mst:
        mst.add(cur_star)
        answer += cur_dist
        for star in stars[cur_star]:
            if star[1] not in mst:
                heapq.heappush(Q, star)

print(answer)