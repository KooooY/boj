N = int(input())
time_info = list(map(int, input().split()))
ans = 0

time_info.sort()
sum_list = [time_info[0]]
for i in range(1,N):
    sum_list.append(sum_list[i-1]+time_info[i])

print(sum(sum_list))