N = int(input())
answer = 0
position = [99] * N

def N_search(r):
    global answer
    global position
    if r == N:
        answer += 1
    for c in range(N):
        flag = 1
        for j in range(r):
            if c == position[j] or abs(position[j] - c) == r - j:
                flag = 0
                break
        if flag:
            position[r] = c
            N_search(r + 1)
    return

for l in range(N):
    position[0] = l
    N_search(1)

print(answer)