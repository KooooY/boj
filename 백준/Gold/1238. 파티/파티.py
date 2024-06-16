import heapq

def dijk(s, e):
    min_dist = [100001] * N
    min_dist[s] = 0
    next_cur = []
    heapq.heappush(next_cur, (0, s))

    while next_cur:
        cur_dist, cur = heapq.heappop(next_cur)
        if cur_dist <= min_dist[cur]:
            for distance, destination in map_info[cur]:
                if min_dist[cur] + distance < min_dist[destination]:
                    min_dist[destination] = min_dist[cur] + distance
                    heapq.heappush(next_cur, (min_dist[destination], destination))

    return min_dist[e]


N, M, X = map(int, input().split())
map_info = [[] for _ in range(N)]
answer = 0

for _ in range(M):
    start, end, dist = map(int, input().split())
    map_info[start - 1].append((dist, end - 1))

for n in range(N):
    time = dijk(n, X - 1) + dijk(X - 1, n)
    if time > answer:
        answer = time

print(answer)