import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
matrix = [[] for _ in range(V)]
mst = set()
heap = []
answer = 0

for _ in range(E):
    A, B, C = map(int, input().split())
    matrix[A - 1].append((C, B - 1))
    matrix[B - 1].append((C, A - 1))

heapq.heappush(heap, (0, 1))

while heap:
    cur = heapq.heappop(heap)
    if cur[1] not in mst:
        mst.add(cur[1])
        answer += cur[0]
        for i in matrix[cur[1]]:
            if i[1] not in mst:
                heapq.heappush(heap, i)

print(answer)