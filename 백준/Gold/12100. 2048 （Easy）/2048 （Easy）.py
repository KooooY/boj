def push(direction):
    x, y = direction

    a = int((N - 1) / 2 + (x + y) * (1 - N) / 2)
    b = int((N - 1) / 2 + (x + y) * (N + 1) / 2)
    s = x + y

    for rc in range(a, b, s):
        temp = []
        for cr in range(a, b, s):
            rorc = rc * abs(y) + cr * abs(x)
            corr = cr * abs(y) + rc * abs(x)
            if board_copy[rorc][corr]:
                temp.append(board_copy[rorc][corr])
                board_copy[rorc][corr] = 0

        c_i = int((N - 1) / 2 + (x + y) * (N - 1) / 2)

        while temp:
            num = temp.pop()
            if len(temp) > 0 and num == temp[-1]:
                num += temp.pop()
            board_copy[rc * abs(y) + c_i * abs(x)][c_i * abs(y) + rc * abs(x)] = num
            c_i -= x + y


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_num = 0
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(1 << 10):
    cmd_list = []
    for j in range(0, 10, 2):
        if i & (1 << j) and i & (1 << (j + 1)):
            cmd_list.append(directions[0])
        elif i & (1 << j):
            cmd_list.append(directions[1])
        elif i & (1 << (j + 1)):
            cmd_list.append(directions[2])
        else:
            cmd_list.append(directions[3])

    board_copy = [board[i][:] for i in range(N)]
    for cmd in cmd_list:
        push(cmd)
    now_max_num = max(map(max, board_copy))
    if max_num < now_max_num:
        max_num = now_max_num

print(max_num)