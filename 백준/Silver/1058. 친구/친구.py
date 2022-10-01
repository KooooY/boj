N = int(input())

friend_info = [input() for _ in range(N)]
matrix = [[0]*N for _ in range(N)]
friend_count = []

for i in range(N):
    for j in range(N):
        if friend_info[i][j] == 'Y':
            matrix[i][j] = 1

for k in range(N):
    visited = []
    Q = [k, 100]

    while visited.count(100) < 3:
        current = Q.pop(0)
        if current == 100:
            Q.append(100)
            visited.append(100)
            continue
        if current not in visited:
            visited.append(current)

        for destination in range(N):
            if matrix[current][destination] and destination not in visited:
                Q.append(destination)

    visited.remove(100)
    visited.remove(100)
    visited.remove(100)
    visited.remove(k)
    visited = set(visited)
    friend_count.append(len(visited))

print(max(friend_count))