import sys
input = sys.stdin.readline

N = int(input())
coordinate = [list(map(int, input().split())) for _ in range(N)]
coordinate.sort(key=lambda x:(x[0], x[1]))

for c in coordinate:
    print(*c)