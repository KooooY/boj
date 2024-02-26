from collections import deque

N, K = map(int, input().split())

if N == K:
    print(0)
    print(1)
else:
    time = 100000
    way = 0
    
    dx = [1, -1, 0]
    dy = [1, 1, 2]
    
    Q = deque()
    Q.append((N, 0))
    visited = set()
    
    while Q:
        cur, cur_time = Q.popleft()
        if cur_time >= time:
            break
        visited.add(cur)
        for i in range(3):
            next_time = cur * dy[i] + dx[i]
            if next_time not in visited and 0 <= next_time <= 200000:
                if next_time == K:
                    way += 1
                    time = cur_time + 1
                else:
                    Q.append((next_time, cur_time + 1))
    
    print(time)
    print(way)