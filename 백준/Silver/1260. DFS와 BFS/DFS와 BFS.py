N, M, V = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    arr[start][end] = 1
    arr[end][start] = 1

stack = [V]
visited_s = []

while stack:
    current = stack.pop()
    if current not in visited_s:
        visited_s.append(current)
        temp = []
        for i in range(1, N+1):
            if i not in visited_s and arr[current][i]:
                temp.append(i)
        temp.sort(reverse=True)
        stack.extend(temp)

print(*visited_s)

Q = [V]
visited_q = []

while Q:
    item = Q.pop(0)
    if item not in visited_q:
        visited_q.append(item)
        temp = []
        for i in range(1, N+1):
            if i not in visited_q and arr[item][i]:
                temp.append(i)
        temp.sort()
        Q.extend(temp)

print(*visited_q)