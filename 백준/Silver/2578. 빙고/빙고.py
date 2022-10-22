bingo = []
call_num = []
for _ in range(5):
    bingo += list(map(int, input().split()))
for _ in range(5):
    call_num += list(map(int, input().split()))

for i in range(10):
    bingo[bingo.index(call_num[i])] = 0

idx = 9
cnt = 0
while cnt < 3:
    idx += 1
    bingo[bingo.index(call_num[idx])] = 0
    cnt = 0
    for i in range(0, 25, 5):
        if bingo[i:i+5] == [0, 0, 0, 0, 0]:
            cnt += 1
    for i in range(5):
        if not bingo[i] and not bingo[i+5] and not bingo[i+2*5] and not bingo[i+3*5] and not bingo[i+4*5]:
            cnt += 1
    if not bingo[0] and not bingo[6] and not bingo[12] and not bingo[18] and not bingo[24]:
        cnt += 1
    if not bingo[4] and not bingo[8] and not bingo[12] and not bingo[16] and not bingo[20]:
        cnt += 1

print(idx+1)
