import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    money_dict = dict()
    total = 0
    for _ in range(N):
        money, cnt = map(int, input().split())
        money_dict[money] = cnt
        total += money * cnt

    if total % 2:
        print(0)
    else:
        dp = [0] * (total // 2 + 1)
        dp[0] = 1
        for m in money_dict:
            for i in range(total // 2, m - 1, -1):
                if dp[i - m]:
                    for j in range(money_dict[m] + 1):
                        if i + m * j <= total // 2:
                            dp[i + m * j] = 1
                        else:
                            break
        if dp[total // 2]:
            print(1)
        else:
            print(0)