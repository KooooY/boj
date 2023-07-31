N, C, W = map(int, input().split())
trees = []
answer = 0

for i in range(N):
    trees.append(int(input()))

for length in range(1, max(trees)+1):
    cost = 0
    for tree in trees:
        if tree % length:
            if (tree // length) * length * W > (tree // length) * C:
                cost += (tree // length) * length * W - (tree // length) * C
        else:
            if (tree // length) * length * W > ((tree // length) - 1) * C:
                cost += (tree // length) * length * W - ((tree // length) - 1) * C
    if cost > answer:
        answer = cost

print(answer)