import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    phone_list = [input().strip() for _ in range(N)]
    phone_list.sort(reverse=True)

    flag = 0
    for i in range(N-1):
        if phone_list[i].startswith(phone_list[i+1]):
            print('NO')
            flag = 1
            break

    if not flag:
        print('YES')