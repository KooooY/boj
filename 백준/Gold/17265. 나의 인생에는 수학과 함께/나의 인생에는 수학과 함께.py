dr = [1, 0]
dc = [0, 1]

def perm(depth):
    if depth == N*2-2:
        cases.append(selected[:])
        return

    for j in range(2):
        selected[depth] = j
        perm(depth+1)

N = int(input())
arr = [input().split() for _ in range(N)]
sum_list = []

cases = []
selected = [0]*(N*2-2)
perm(0)

for case in cases:
    temp = 0
    sign = '+'
    r = 0
    c = 0
    flag = 1

    for i in range(N*2-1):
        if r < 0 or r >= N or c < 0 or c >= N:
            flag = 0
            break
        if i%2:
           sign = arr[r][c]
        else:
            if sign == '+':
                temp += int(arr[r][c])
            elif sign == '-':
                temp -= int(arr[r][c])
            elif sign == '*':
                temp *= int(arr[r][c])
        if i < N*2-2:
            r += dr[case[i]]
            c += dc[case[i]]

    if flag:
        sum_list.append(temp)

print(max(sum_list), min(sum_list))