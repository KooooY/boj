T = int(input())

for _ in range(T):
    n = int(input())
    sum_list = [0, 1, 2, 4]

    for i in range(4, n+1):
        sum_list.append(sum_list[i-3]+sum_list[i-2]+sum_list[i-1])
        
    print(sum_list[n])