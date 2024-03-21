def sol(rsi, rsj, bsi, bsj, cnt):
    global result

    if result <= cnt:
        return

    if cnt > 10:
        return

    for d in range(4):
        flag = 0
        rni = rsi + di[d]
        rnj = rsj + dj[d]
        bni = bsi + di[d]
        bnj = bsj + dj[d]
        if arr[rni][rnj] != '#' or arr[bni][bnj] != '#':
            dist1 = 0
            for c in range(1, N+M):
                rni = rsi + c*di[d]
                rnj = rsj + c*dj[d]
                if arr[rni][rnj] == '#':
                    break
                elif arr[rni][rnj] == 'O':
                    flag = 1
                    break
                elif rni == bsi and rnj == bsj:
                    continue
                else:
                    dist1 += 1
            rni = rsi + dist1*di[d]
            rnj = rsj + dist1*dj[d]
            dist2 = 0
            for c in range(1, N+M):
                bni = bsi + c*di[d]
                bnj = bsj + c*dj[d]
                if arr[bni][bnj] == '#':
                    break
                elif arr[bni][bnj] == 'O':
                    flag = 2
                    break
                elif flag==0 and bni == rsi and bnj == rsj:
                    continue
                else:
                    dist2 += 1
            if flag == 2:
                continue
            if flag == 1:
                result = cnt
                return
            bni = bsi + dist2*di[d]
            bnj = bsj + dist2*dj[d]
            sol(rni, rnj, bni, bnj, cnt+1)


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            rsi = i
            rsj = j
        elif arr[i][j] == 'B':
            bsi = i
            bsj = j

result = 11
sol(rsi, rsj, bsi, bsj, 1)

if result == 11:
    result = -1

print(result)