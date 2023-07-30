cannonball = int(input())
answer = cannonball

total_info = []

ball = 0
for i in range(1, 300001):
    ball += (i * (i+1)) // 2
    total_info.append(ball)

    if total_info[-1] >= cannonball:
        break

count_arr = [300000]*(cannonball+1)

for j in range(1, cannonball+1):
    for k in total_info:
        if j == k:
            count_arr[j] = 1
        if j < k:
            break
        count_arr[j] = min(count_arr[j], count_arr[j-k]+1)

print(count_arr[cannonball])