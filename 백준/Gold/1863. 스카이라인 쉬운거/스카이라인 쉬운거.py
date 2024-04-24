import sys
input = sys.stdin.readline

n = int(input())
answer = 0
stack = []
prev_h = 0

for _ in range(n):
    x, y = map(int, input().split())
    if y < prev_h:
        while stack:
            cur = stack.pop()
            if cur > y:
                answer += 1
            else:
                if cur < y:
                    stack.append(cur)
                break
    stack.append(y)
    prev_h = y

while stack:
    cur = stack.pop()
    if cur:
        answer += 1

print(answer)