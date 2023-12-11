import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
answer = 0

visited_alphabet = {board[0][0]}

def dfs(r, c, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(4):
        new_r, new_c = r + dr[i], c + dc[i]
        if 0 <= new_r < R and 0 <= new_c < C and board[new_r][new_c] not in visited_alphabet:
            visited_alphabet.add(board[new_r][new_c])
            dfs(new_r, new_c, cnt + 1)
            visited_alphabet.remove(board[new_r][new_c])

dfs(0, 0, 1)
print(answer)