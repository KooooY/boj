N = input()
M = int(input())
if N == '100':
    print(0)

elif M:
    answer = abs(int(N) - 100)
    broken_buttons = list(map(int, input().split()))
    for i in range(answer):
        temp = set()
        if 0 <= int(N) - i:
            temp.add(str(int(N) - i))
        if 0 <= int(N) + i:
            temp.add(str(int(N) + i))
        remove_number = set()
        for j in temp:
            for k in j:
                if int(k) in broken_buttons:
                    remove_number.add(j)
        temp -= remove_number
        for l in temp:
            if i + len(l) < answer:
                answer = i + len(l)
        if temp:
            break
    print(answer)

else:
    print(min(len(N), abs(100 - int(N))))