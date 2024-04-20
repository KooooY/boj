import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    answer = n // 2 + 1

    for i in range(n // 3):
        answer += (n - 3 * (i + 1)) // 2 + 1

    print(answer)