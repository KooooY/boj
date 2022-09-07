C, R = map(int, input().split())
K = int(input())
seat_matrix = [[0]*(R+2)]
seat_matrix += [[0]+[-1]*R+[0] for _ in range(C)]
seat_matrix += [[0]*(R+2)]

r, c = (1, 0)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

turn = 0
num = 1

if C*R < K:
    print(0)
else:
    while num < K+1:
        r += dr[turn % 4]
        c += dc[turn % 4]
        if seat_matrix[r][c] == -1:
            seat_matrix[r][c] = num
            num += 1
            continue
        r -= dr[turn % 4]
        c -= dc[turn % 4]
        turn += 1

    print(f'{r} {c}')