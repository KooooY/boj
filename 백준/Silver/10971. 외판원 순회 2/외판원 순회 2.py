def find_path(idx, total_cost, visited):
    global min_cost

    if len(visited) == N:
        if cost[idx][visited[0]] != 0:
            total_cost += cost[idx][visited[0]]
            if total_cost < min_cost:
                min_cost = total_cost
        return
    for i in range(N):
        if cost[idx][i] != 0 and i not in visited:
            total_cost += cost[idx][i]
            if total_cost >= min_cost:
                return
            else:
                visited.append(i)
                find_path(i, total_cost, visited)
                total_cost -= cost[idx][i]
                visited.remove(i)

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

min_cost = 10000000

for j in range(N):
    visited = [j]
    find_path(j, 0, visited)

print(min_cost)