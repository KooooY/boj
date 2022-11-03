def check(length, coordinate):
    global m_cnt
    global z_cnt
    global o_cnt

    r = coordinate[0]
    c = coordinate[1]
    if length > 1:
        new_length = length//3
        piece_1 = check(new_length, (r-new_length*2, c-new_length*2))
        piece_2 = check(new_length, (r-new_length*2, c-new_length))
        piece_3 = check(new_length, (r-new_length*2, c))
        piece_4 = check(new_length, (r-new_length, c-new_length*2))
        piece_5 = check(new_length, (r-new_length, c-new_length))
        piece_6 = check(new_length, (r-new_length, c))
        piece_7 = check(new_length, (r, c-new_length*2))
        piece_8 = check(new_length, (r, c-new_length))
        piece_9 = check(new_length, (r, c))

        if piece_1+piece_2+piece_3+piece_4+piece_5+piece_6+piece_7+piece_8+piece_9 == -9:
            return -1
        elif piece_1+piece_2+piece_3+piece_4+piece_5+piece_6+piece_7+piece_8+piece_9 == 0 and 1 not in [piece_1,piece_2,piece_3,piece_4,piece_5,piece_6,piece_7,piece_8,piece_9]:
            return 0
        elif piece_1+piece_2+piece_3+piece_4+piece_5+piece_6+piece_7+piece_8+piece_9 == 9:
            return 1
        else:
            for i in [piece_1,piece_2,piece_3,piece_4,piece_5,piece_6,piece_7,piece_8,piece_9]:
                if i == -1:
                    m_cnt += 1
                elif i == 0:
                    z_cnt += 1
                elif i == 1:
                    o_cnt += 1
            return 999
    else:
        if paper[r][c] == -1:
            return -1
        elif paper[r][c] == 0:
            return 0
        elif paper[r][c] == 1:
            return 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
m_cnt = 0
z_cnt = 0
o_cnt = 0

check(N, (N-1, N-1))

if not m_cnt and not z_cnt and not o_cnt:
    if paper[0][0] == -1:
        m_cnt += 1
    elif paper[0][0] == 0:
        z_cnt += 1
    elif paper[0][0] == 1:
        o_cnt += 1

print(m_cnt)
print(z_cnt)
print(o_cnt)