import heapq
import sys
input = sys.stdin.readline

def dijk(info):
    min_dist = [100001] * N
    min_dist[X - 1] = 0
    next_cur = []
    heapq.heappush(next_cur, (0, X - 1))

    while next_cur:
        cur_dist, cur = heapq.heappop(next_cur)
        if cur_dist <= min_dist[cur]:
            for distance, destination in info[cur]:
                if min_dist[cur] + distance < min_dist[destination]:
                    min_dist[destination] = min_dist[cur] + distance
                    heapq.heappush(next_cur, (min_dist[destination], destination))

    return min_dist


N, M, X = map(int, input().split())
map_info = [[] for _ in range(N)]
reverse_map_info = [[] for _ in range(N)]
answer = 0

for _ in range(M):
    start, end, dist = map(int, input().split())
    map_info[start - 1].append((dist, end - 1))
    reverse_map_info[end - 1].append((dist, start - 1))

dijk_info = dijk(map_info)
reverse_dijk_info = dijk(reverse_map_info)

for n in range(N):
    time = dijk_info[n] + reverse_dijk_info[n]
    if time > answer:
        answer = time

print(answer)