from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find(leaf):
    if leaf != parents[leaf]:
        parents[leaf] = find(parents[leaf])
    return parents[leaf]

def union(start, end):
    start = find(start)
    end = find(end)
    if start == end:
        return True
    else:
        parents[start] = end
        return False

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
parents = [i for i in range(N * M)]
visited = set()
answer = set()

for j in range(N):
    for k in range(M):
        if (j, k) not in visited:
            r, c = j, k
            visited.add((r, c))
            while True:
                direction = 0
                if matrix[r][c] == 'U':
                    direction = 0
                elif matrix[r][c] == 'D':
                    direction = 1
                elif matrix[r][c] == 'L':
                    direction = 2
                elif matrix[r][c] == 'R':
                    direction = 3
                if 0 <= r + dr[direction] < N and 0 <= c + dc[direction] < M:
                    visited.add((r + dr[direction], c + dc[direction]))
                    if union(r * M + c, (r + dr[direction]) * M + c + dc[direction]):
                        answer.add(find(r * M + c))
                        break
                    else:
                        r, c = r + dr[direction], c + dc[direction]
                else:
                    answer.add(find(r * M + c))
                    break

print(len(answer))
