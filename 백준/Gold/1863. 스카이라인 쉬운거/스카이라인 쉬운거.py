import sys
input = sys.stdin.readline

n = int(input())
skyline = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)] + [(0, 0)]
answer = 0
stack = []

for i in range(1, n + 2):
    if skyline[i][1] < skyline[i - 1][1]:
        while stack:
            cur = stack.pop()
            if cur > skyline[i][1]:
                answer += 1
            else:
                if cur < skyline[i][1]:
                    stack.append(cur)
                break
    stack.append(skyline[i][1])

print(answer)