T = int(input())
for _ in range(T):
    N = int(input())
    P_list = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if N > 10:
        for i in range(11, N+1):
            P_list.append(P_list[i-3]+P_list[i-2])
    print(P_list[N])