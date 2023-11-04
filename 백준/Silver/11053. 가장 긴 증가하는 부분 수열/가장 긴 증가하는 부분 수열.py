N = int(input())
num_list = list(map(int, input().split()))
count_list = [1] * N

for i in range(N):
    for j in range(i):
        if num_list[j] < num_list[i]:
            count_list[i] = max([count_list[j]+1, count_list[i]])

print(max(count_list))