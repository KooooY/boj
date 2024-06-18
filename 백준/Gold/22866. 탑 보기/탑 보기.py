N = int(input())
buildings = list(map(int, input().split()))

maximum = 0
answer = [[0, 0, -1] for _ in range(N)]

for i in range(1, N):
    if buildings[i - 1] > buildings[i]:
        answer[i][0] = answer[i - 1][0] + 1
        answer[i][2] = i - 1
        if buildings[i - 1] > buildings[maximum]:
            maximum = i - 1
    elif buildings[i - 1] <= buildings[i] < buildings[maximum]:
        cur = i - 2
        while cur >= maximum:
            if buildings[cur] > buildings[i]:
                answer[i][0] = answer[cur][0] + 1
                answer[i][2] = cur
                break
            elif buildings[cur] == buildings[i]:
                answer[i][0] = answer[cur][0]
                answer[i][2] = answer[cur][2]
                break
            else:
                cur -= 1
    else:
        maximum = i
        if answer[i - 1][2] != i - 2 and buildings[i - 1] < buildings[i] and answer[i - 1][2] < 0:
            answer[i - 1][2] = i

maximum = N - 1
for j in range(N - 2, -1, -1):
    if buildings[j + 1] > buildings[j]:
        answer[j][1] = answer[j + 1][1] + 1
        if j - answer[j][2] > 1 or answer[j][2] < 0:
            answer[j][2] = j + 1
        if buildings[j + 1] > buildings[maximum]:
            maximum = j + 1
    elif buildings[j + 1] <= buildings[j] < buildings[maximum]:
        cur = j + 2
        while cur <= maximum:
            if buildings[cur] > buildings[j]:
                answer[j][1] = answer[cur][1] + 1
                if j - answer[j][2] > cur - j or answer[j][2] < 0:
                    answer[j][2] = cur
                break
            elif buildings[cur] == buildings[j]:
                answer[j][1] = answer[cur][1]
                if j - answer[j][2] > answer[cur][2] - j or answer[j][2] < 0:
                    answer[j][2] = answer[cur][2]
                break
            else:
                cur += 1
    else:
        maximum = j
        if answer[j + 1][2] != j + 1 and buildings[j] < buildings[j + 1] and answer[j + 1][2] < 0:
            answer[j + 1][2] = j

for k in range(N):
    if answer[k][0] + answer[k][1]:
        print(answer[k][0] + answer[k][1], answer[k][2] + 1)
    else:
        print(0)