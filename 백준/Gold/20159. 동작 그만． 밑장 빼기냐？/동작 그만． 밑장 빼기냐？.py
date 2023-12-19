N = int(input())
cards = list(map(int, input().split()))

prefix = [0 for _ in range(N+4)]

for i in range(N//2):
    prefix[i*2+2] = prefix[i*2] + cards[i*2]
    prefix[N-(i*2)+1] = prefix[N-(i*2)+3] + cards[N-(i*2)-1]

answer = prefix[3]

for i in range(N-1):
    if i%2:
        temp = prefix[i+1] + prefix[i+4]
    else:
        temp = prefix[i + 2] + prefix[i + 3] - cards[N - 1]
    if temp > answer:
        answer = temp

print(answer)