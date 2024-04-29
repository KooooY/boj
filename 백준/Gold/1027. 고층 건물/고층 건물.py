def watch(index):
    answer = 0
    height = build[index]
    for i in range(n):
        dx = i - index
        dy = height - build[i]
        if dx != 0:
            d = dy/abs(dx)
            k = 1
            if dx > 0:
                k = -1
            b = 1
            for j in range(i+k, index, k):
                if build[j] >= build[i] + d*abs(j-i):
                    b = 0
                    break
            if b:
                answer += 1
    return answer

n = int(input())
build = list(map(int,input().split()))
answer = 0

for i in range(n):
    answer = max(answer, watch(i))
    
print(answer)