n = int(input())
num_list = list(map(int,input().split()))

dp_f = [0] * (n+1)
dp_b = [0] * (n+1)
dp_f[0] = 1
dp_b[n] = 1

for i in range(1,n):
    for j in range(i):
        if num_list[i] > num_list[j] and dp_f[i] < dp_f[j]:
            dp_f[i] = dp_f[j]
    dp_f[i] += 1

for i in range(n-1,-1,-1):
    for j in range(n-1, i,-1):
        if num_list[i] > num_list[j] and dp_b[i] < dp_b[j]:
            dp_b[i] = dp_b[j]
    dp_b[i] += 1

dp = list(map(lambda x,y: x + y - 1, dp_b, dp_f))
print(max(dp))