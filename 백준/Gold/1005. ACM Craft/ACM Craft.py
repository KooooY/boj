import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    topology = [0] * (N + 1)
    node_info = [[] for _ in range(N + 1)]
    buildings = []

    for i in range(K):
        front, back = map(int, input().split())
        node_info[front].append(back)
        topology[back] += 1

    for j in range(1, N + 1):
        if not topology[j]:
            heapq.heappush(buildings, (times[j], j))

    answer = int(input())

    while buildings:
        time, number = heapq.heappop(buildings)
        if number == answer:
            print(time)
            break
        for b in node_info[number]:
            topology[b] -= 1
            if not topology[b]:
                heapq.heappush(buildings, (time + times[b], b))

