import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    grade_info = [list(map(int, input().split())) for _ in range(N)]

    grade_info.sort()
    standard = grade_info[0][1]
    ans = 1

    for i in grade_info:
        if i[1] < standard:
            ans += 1
            standard = i[1]

    print(ans)