import heapq
import sys
input = sys.stdin.readline

def Prim():
    visited = set()
    answer = []
    heap = []
    heapq.heappush(heap, (0, 1))

    while heap:
        cur = heapq.heappop(heap)
        if cur[1] not in visited:
            visited.add(cur[1])
            answer.append(cur[0])
            for i in arr[cur[1]]:
                if i[1] not in visited:
                    heapq.heappush(heap, i)
    return answer

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, w = map(int, input().split())
    arr[start].append((w, end))
    arr[end].append((w, start))

node = Prim()
print(sum(node) - max(node))