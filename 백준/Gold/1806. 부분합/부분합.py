import sys
input = sys.stdin.readline

def solve():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    ans, st, en, t = [], 0, 0, 0
    for en in range(N):
        t += A[en]

        while t >= S:
            if st == en:    return 1
            ans.append(en-st+1)
            t -= A[st]
            st += 1
    return 0 if len(ans) == 0 else min(ans)

print(solve())