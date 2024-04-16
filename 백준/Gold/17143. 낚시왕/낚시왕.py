import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

R, C, M = map(int, input().split())
sharks = {i: dict() for i in range(C)}

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    if r - 1 in sharks[c - 1]:
        if sharks[c - 1][r - 1][2] > z:
            continue
    sharks[c - 1][r - 1] = (s, d - 1, z)

fisherman = -1
answer = 0

while fisherman < C - 1:
    fisherman += 1
    if sharks[fisherman]:
        answer += sharks[fisherman][min(sharks[fisherman])][2]
        del sharks[fisherman][min(sharks[fisherman])]
    if fisherman == C - 1:
        break

    new_sharks = {k: dict() for k in range(C)}
    for col in sharks:
        for row in sharks[col]:
            new_r = row + dr[sharks[col][row][1]] * sharks[col][row][0]
            new_c = col + dc[sharks[col][row][1]] * sharks[col][row][0]
            new_s = sharks[col][row][0]
            new_d = sharks[col][row][1]
            new_z = sharks[col][row][2]
            if new_r < 0:
                if not ((-new_r - 1) // (R - 1)) % 2:
                    new_d = 1
                    new_r = ((-new_r - 1) % (R - 1)) + 1
                else:
                    new_r = (R - 1) - ((-new_r - 1) % (R - 1) + 1)
            elif new_r >= R:
                if ((new_r - 1) // (R - 1)) % 2:
                    new_d = 0
                    new_r = (R - 1) - ((new_r - 1) % (R - 1) + 1)
                else:
                    new_r = (new_r - 1) % (R - 1) + 1
            elif new_c < 0:
                if not ((-new_c - 1) // (C - 1)) % 2:
                    new_d = 2
                    new_c = ((-new_c - 1) % (C - 1)) + 1
                else:
                    new_c = (C - 1) - ((-new_c - 1) % (C - 1) + 1)
            elif new_c >= C:

                if ((new_c - 1) // (C - 1)) % 2:
                    new_d = 3
                    new_c = (C - 1) - ((new_c - 1) % (C - 1) + 1)
                else:
                    new_c = (new_c - 1) % (C - 1) + 1
            if new_r in new_sharks[new_c]:
                if new_sharks[new_c][new_r][2] > new_z:
                    continue
            new_sharks[new_c][new_r] = (new_s, new_d, new_z)

    sharks = new_sharks

print(answer)
