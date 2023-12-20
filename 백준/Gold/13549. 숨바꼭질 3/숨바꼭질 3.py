N, K = map(int, input().split())
time = [100001 for _ in range(200000)]
time[N] = 0

deque = [N]
visited = {N}

while deque:
    current = deque.pop(0)
    visited.add(current)
    if current - 1 not in visited and 0 <= current - 1 < 200000:
        deque.append(current - 1)
        time[current-1] = min(time[current]+1, time[current-1])
    if current + 1 not in visited and 0 <= current + 1 < 200000:
        deque.append(current + 1)
        time[current + 1] = min(time[current]+1, time[current + 1])
    if current * 2 not in visited and 0 <= current * 2 < 200000:
        deque.insert(0, current * 2)
        time[current * 2] = min(time[current], time[current*2])

    if K in [current-1, current+1, current*2]:
        break

print(time[K])