import sys
input = sys.stdin.readline

L = int(input())
M_l, M_k = map(int, input().split())
C = int(input())
flag = 0
C_log = [0]*(L+1)
zombie = 0

for i in range(1, L+1):
    Z_i = int(input())
    zombie += C_log[i]
    num = min(i, M_l)
    if (num-zombie)*M_k < Z_i:
        if C:
            C -= 1
            zombie += 1
            if i+M_l <= L:
                C_log[i+M_l] = -1
        else:
            flag = 1
            break

if flag:
    print('NO')
else:
    print('YES')