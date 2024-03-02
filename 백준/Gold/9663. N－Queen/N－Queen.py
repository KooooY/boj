N = int(input())
answer = 0
position = [99] * N

def N_search(r):
    global answer
    global position

    for c in range(N):
        flag = 1
        for j in range(r):
            if c == position[j] or abs(position[j] - c) == r - j:
                flag = 0
                break
        if flag:
            if r == N - 1:
                answer += 1
            else:
                position[r] = c
                N_search(r + 1)
    return

if N == 1:
    print(1)
else:
    for l in range(N):
        position[0] = l
        N_search(1)

    print(answer)