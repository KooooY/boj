N = int(input())
numbers = list(map(int, input().split()))
numdict = dict()
answer = 0

for num in numbers:
    if num in numdict:
        numdict[num] += 1
    else:
        numdict[num] = 1

for i in numbers:
    for j in numdict:
        if i - j in numdict:
            if i == j:
                if i and numdict[i] > 1 or numdict[i] > 2:
                    answer += 1
                    break
            elif i and j:
                if j == i - j and numdict[j] < 2:
                    continue
                answer += 1
                break
            else:
                if not j and numdict[i] < 2:
                    continue
                answer += 1
                break

print(answer)