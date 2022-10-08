T = int(input())

for _ in range(T):
    N = int(input())
    clothes = {}
    category = []
    ans = 1

    for _ in range(N):
        clothes_info = list(map(str, input().split()))
        if clothes_info[1] not in clothes:
            clothes[clothes_info[1]] = [clothes_info[0]]
        else:
            clothes[clothes_info[1]] += [clothes_info[0]]

    for i in list(clothes.keys()):
        ans *= (len(clothes[i])+1)

    print(ans-1)