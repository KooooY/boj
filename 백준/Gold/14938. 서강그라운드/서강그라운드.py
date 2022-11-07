def dijkstra(start):
    dist = [99] * (n+1)
    dist[start] = 0
    visited = set()
    item_sum = 0

    for _ in range(n+1):
        min_idx = -1
        min_value = 99

        for i in range(n+1):
            if i not in visited and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]

        visited.add(min_idx)
        for j in range(n+1):
            if j not in visited and dist[j] > matrix[min_idx][j] + dist[min_idx] and matrix[min_idx][j] + dist[min_idx] <= m:
                dist[j] = matrix[min_idx][j] + dist[min_idx]

    visited.remove(-1)
    for k in visited:
        item_sum += item_info[k-1]

    return item_sum


n, m, r = map(int, input().split())
item_info = list(map(int, input().split()))
matrix = [[99]*(n+1) for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    matrix[a][b] = l
    matrix[b][a] = l

max_sum = 0
for start in range(1, n+1):
    sum_item = dijkstra(start)
    if sum_item > max_sum:
        max_sum = sum_item

print(max_sum)