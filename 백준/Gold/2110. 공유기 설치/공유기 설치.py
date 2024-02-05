import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]

house.sort()
dist = []
answer = 0

for i in range(1, N):
    dist.append(house[i] - house[i-1])

start = 0
end = house[N-1] - house[0]

while start <= end:
    mid = (start + end) // 2
    count = N
    prefix = 0

    for d in dist:
        if prefix + d < mid:
            count -= 1
            prefix += d
        else:
            prefix = 0

    if count < C:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid

print(answer)