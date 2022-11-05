import sys
input = sys.stdin.readline

N, T = map(int, input().split())
carrot = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
time = min(N, T)

carrot.sort(key=lambda x:(x[1], x[0]))

for i in range(time):
    rabbit = carrot.pop()
    cnt += rabbit[0] + rabbit[1]*(T-i-1)

print(cnt)