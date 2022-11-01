N = int(input())
time_info = list(map(int, input().split()))
ans = 0

time_info.sort()
for i in range(N):
    ans += sum(time_info[:i+1])

print(ans)