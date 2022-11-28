r_1, c_1, r_2, c_2 = map(int, input().split())
ans = []
max_len = 1
for r in range(r_1, r_2+1):
    temp = []
    for c in range(c_1, c_2+1):
        if r == 0 and c == 0:
            a = '1'
        elif r == c and r < 0:
            a = str((abs(r)*2-1)**2 + abs(r)*4)
        elif r == -c and r < 0:
            a = str((abs(r)*2-1)**2 + abs(r)*2)
        elif r == c and r > 0:
            a = str((abs(r)*2+1)**2)
        elif r == -c and r > 0:
            a = str((abs(r)*2-1)**2 + abs(r)*6)
        elif r < c and abs(r) > abs(c):
            a = str((abs(r)*2-1)**2 + abs(r)*4 - (c-r))
        elif r < c and abs(r) < abs(c):
            a = str((abs(c)*2-1)**2 + (c-r))
        elif r > c and abs(r) > abs(c):
            a = str((abs(r)*2-1)**2 + abs(r)*6 + (r+c))
        elif r > c and abs(r) < abs(c):
            a = str((abs(c)*2-1)**2 + abs(c)*6 + (r+c))
        if len(a) > max_len:
            max_len = len(a)
        temp.append(a)
    ans.append(temp)

for r in range(r_2 - r_1 +1):
    for c in range(c_2 - c_1 + 1):
        if len(ans[r][c]) < max_len:
            ans[r][c] = ' '*(max_len-len(ans[r][c])) + ans[r][c]
    print(*ans[r])