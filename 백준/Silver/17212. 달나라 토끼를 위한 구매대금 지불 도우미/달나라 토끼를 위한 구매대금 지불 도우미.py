N = int(input())
coin_count = {1:0, 2:0, 5:0, 7:0}
ans = 0

while N:
    if N == 10:
        N -= 10
        coin_count[5] += 2
    elif N >= 7:
        N -= 7
        coin_count[7] += 1
    elif N >= 5:
        N -= 5
        coin_count[5] += 1
    elif N >= 2:
        N -= 2
        coin_count[2] += 1
    elif N >= 1:
        N -= 1
        coin_count[1] += 1

for k in coin_count:
    ans += coin_count[k]

print(ans)