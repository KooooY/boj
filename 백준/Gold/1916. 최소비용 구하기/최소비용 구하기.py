import sys
input = sys.stdin.readline

def dijk(dep, arr):
    dist = [999999*N]*(N+1)
    dist[dep] = 0
    visited = set()

    for _ in range(N+1):
        min_idx = -1
        min_value = 999999*N

        for i in range(N+1):
            if i not in visited and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited.add(min_idx)
        if min_idx == arr:
            break

        for j in range(N+1):
            if j not in visited and dist[j] > bus_cost[min_idx][j] + dist[min_idx]:
                dist[j] = bus_cost[min_idx][j] + dist[min_idx]

    return dist[arr]


N = int(input())
M = int(input())
bus_cost = [[999999*N]*(N+1) for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    if bus_cost[start][end] > cost:
        bus_cost[start][end] = cost

dep, arr = map(int, input().split())

print(dijk(dep, arr))