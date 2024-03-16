import sys
input = sys.stdin.readline
from collections import deque
import heapq

N, K = map(int, input().split())
gems = [tuple(map(int, input().split())) for _ in range(N)]
bags = sorted([int(input()) for _ in range(K)])
answer = 0

gems.sort()
gems = deque(gems)

values = []

for bag in bags:
    while gems and gems[0][0] <= bag:
        gem = gems.popleft()
        heapq.heappush(values, -gem[1])
    if values:
        answer -= heapq.heappop(values)

print(answer)