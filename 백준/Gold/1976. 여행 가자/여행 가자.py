import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
cities = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    temp = list(map(int, input().split()))
    for j in range(N):
         if temp[j]:
             cities[i].append(j + 1)

path = deque(map(int, input().split()))
flag = 1

while len(path) > 1 and flag:
    flag = 0
    start = path.popleft()
    end = path.popleft()
    if start == end:
        path.appendleft(end)
        flag = 1
    else:
        Q = deque([start])
        visited = {start}
        while Q and not flag:
            next_city = Q.popleft()
            for city in cities[next_city]:
                if city == end:
                    path.appendleft(end)
                    flag = 1
                    break
                if city not in visited:
                    Q.append(city)
                    visited.add(city)

if flag:
    print('YES')
else:
    print('NO')