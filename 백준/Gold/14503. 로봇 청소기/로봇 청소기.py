di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def rotate(direction):
    rd = direction - 1
    if rd < 0:
        rd = 3
    return rd


def back(direction):
    bd = direction - 2
    if bd < 0:
        bd += 4
    return bd


def clean(y, x, direction):
    matrix[y][x] = 2
    # pprint.pprint(matrix)
    rotated = 0
    find = False

    for _ in range(4):
        direction = rotate(direction)
        rotated += 1
        if 0 <= y + di[direction] < N and 0 <= x + dj[direction] < M:
            if matrix[y + di[direction]][x + dj[direction]] == 0:
                find = True
                break
    if rotated <= 4 and find:
        clean(y + di[direction], x + dj[direction], direction)

    if rotated == 4 and not find:
        if matrix[y + di[back(direction)]][x + dj[back(direction)]] == 1:
            pass
        else:
            clean(y + di[back(direction)], x + dj[back(direction)], direction)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

clean(r, c, d)

ans = 0

for row in matrix:
    ans += row.count(2)

print(ans)