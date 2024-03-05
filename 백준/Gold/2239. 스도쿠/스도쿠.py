import sys
input = sys.stdin.readline

def find_number(idx):
    global sudoku
    global flag

    number_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    r, c = empty[idx]

    if flag:
        return

    for i in range(3):
        for j in range(3):
            number_set -= {sudoku[r][i * 3 + j]}
            number_set -= {sudoku[i * 3 + j][c]}
            number_set -= {sudoku[3 * (r // 3) + i % 3][3 * (c // 3) + j % 3]}

    if number_set:
        numbers = sorted(list(number_set))
        for number in numbers:
            sudoku[r][c] = number
            if idx > len(empty) - 2:
                for l in range(9):
                    print("".join(map(str, sudoku[l])))
                flag = 1
            else:
                find_number(idx + 1)
                sudoku[r][c] = 0

sudoku = []
empty = []
flag = 0

for r in range(9):
    temp = list(map(int, list(input().rstrip())))
    for c in range(9):
        if not temp[c]:
            empty.append((r, c))
    sudoku.append(temp)

find_number(0)
