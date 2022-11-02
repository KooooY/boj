T = int(input())

for _ in range(T):
    N = int(input())
    zero = [1, 0]
    one = [0, 1]

    for i in range(2, N+1):
        zero.append(zero[i-2]+zero[i-1])
        one.append(one[i-2]+one[i-1])

    print(zero[N], one[N])