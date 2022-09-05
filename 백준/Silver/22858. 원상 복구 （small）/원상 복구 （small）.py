N, K = map(int, input().split())
S = list(map(int, input().split()))
D = list(map(int, input().split()))

for j in range(K):
    ex_P = [0] * N
    for i in range(N):
        ex_P[D[i]-1] = S[i]
    S = ex_P

print(*S)