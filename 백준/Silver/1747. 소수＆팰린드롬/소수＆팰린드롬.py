N = int(input())

arr = [i for i in range(10000001)]
answer = 0
arr[1] = 0

for j in range(2, int(10000000**(1/2))+1):
    if not arr[j]:
        continue
    for k in range(j*j, 10000001, j):
        arr[k] = 0

for l in range(N, 10000001):
    if arr[l] and str(arr[l]) == str(arr[l])[::-1]:
        answer = arr[l]
        break

print(answer)