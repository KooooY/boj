def bingo(check, board):
    vertical = 0
    horizontal = 0
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == check:
            vertical = 1
            break
    for j in range(3):
        if board[j*3] == board[j*3+1] == board[j*3+2] == check:
            horizontal = 1
            break
    if vertical + horizontal < 1:
        if board[0] == board[4] == board[8] == check or board[2] == board[4] == board[6] == check:
            return 1
        else:
            return 0
    else:
        return 1

while True:
    cur = input()
    if cur == 'end':
        break
    else:
        x_count = cur.count('X')
        o_count = cur.count('O')
        if x_count == o_count or x_count == o_count + 1:
            if x_count + o_count == 9:
                if bingo('O', cur):
                    print('invalid')
                else:
                    print('valid')
            else:
                x_bingo = bingo('X', cur)
                o_bingo = bingo('O', cur)
                if (x_count > o_count and o_bingo) or (x_count == o_count and x_bingo) or (x_bingo and o_bingo) or (not x_bingo and not o_bingo):
                    print('invalid')
                else:
                    print('valid')
        else:
            print('invalid')
