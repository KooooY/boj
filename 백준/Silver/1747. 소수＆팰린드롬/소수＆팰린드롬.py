N = int(input())

arr = [i for i in range(2000001)]
arr[1] = 0

for j in range(2, int(2000000**(1/2))+1):
    if not arr[j]:
        continue
    for k in range(j*j, 2000001, j):
        arr[k] = 0

for l in range(N, 2000001):
    if arr[l] and str(arr[l]) == str(arr[l])[::-1]:
        print(arr[l])
        break