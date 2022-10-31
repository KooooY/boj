N, M = map(int, input().split())
info = {}
for _ in range(N):
    k, v = map(str, input().split())
    info[k] = v

for _ in range(M):
    print(info[input()])