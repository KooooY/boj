N, M = map(int, input().split())
truth_info = list(map(int, input().split()))
total = truth_info[0]
truth_Q = truth_info[1:]
truth_person = set(truth_info[1:])
party_info = [list(map(int, input().split())) for _ in range(M)]
arr = [[0]*(N+1) for _ in range(N+1)]

while truth_Q:
    item = truth_Q.pop(0)
    for i in party_info:
        invite = i[1:]
        if item in invite:
            for j in invite:
                if j not in truth_person:
                    truth_Q.append(j)
                    truth_person.add(j)

cnt = 0
for k in party_info:
    invite = set(k[1:])
    if not invite & truth_person:
        cnt += 1

print(cnt)