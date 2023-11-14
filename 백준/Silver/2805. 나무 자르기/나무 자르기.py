N, M = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort(reverse=True)
high = trees[0]
low = 0
answer = 0

while high >= low:
    mid = (high + low) // 2
    temp = 0
    for i in trees:
        if i <= mid:
            break
        temp += i - mid
    if temp < M:
        high = mid - 1
    else:
        answer = mid
        if temp > M:
            low = mid + 1
        else:
            break

print(answer)