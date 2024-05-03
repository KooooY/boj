from sys import stdin

n, l = map(int, stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))
cnt = 0


def check(li):
    sw = [False for _ in range(n)]
    for i in range(n - 1):
        if li[i] == li[i + 1]:
            continue

        if abs(li[i] - li[i + 1]) > 1:
            return False

        if li[i] > li[i + 1]:
            temp = li[i + 1]
            for j in range(i + 1, i + 1 + l):
                if 0 <= j < n:
                    if li[j] != temp:
                        return False

                    if sw[j]:
                        return False

                    sw[j] = True

                else:
                    return False

        else:
            temp = li[i]
            for j in range(i, i - l, -1):
                if 0 <= j < n:
                    if li[j] != temp:
                        return False

                    if sw[j]:
                        return False

                    sw[j] = True

                else:
                    return False
    return True


for i in arr:
    if check(i):
        cnt += 1

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(arr[j][i])
    if check(temp):
        cnt += 1

print(cnt)