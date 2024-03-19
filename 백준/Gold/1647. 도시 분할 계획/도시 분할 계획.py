import heapq
import sys
input = sys.stdin.readline

def Prim():
    dist = [0] * (N+1)
    heap = [(1, 1)]

    while heap:
        cur = heapq.heappop(heap)
        if not dist[cur[1]]:
            dist[cur[1]] = cur[0]
            for i in arr[cur[1]]:
                if not dist[i[1]]:
                    heapq.heappush(heap, i)
    return dist

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, w = map(int, input().split())
    arr[start].append((w, end))
    arr[end].append((w, start))

node = Prim()
print(sum(node[2:]) - max(node))