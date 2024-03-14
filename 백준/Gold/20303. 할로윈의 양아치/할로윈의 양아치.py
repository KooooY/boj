import sys
input = sys.stdin.readline

def find(leaf):
    if leaf != friends[leaf]:
        friends[leaf] = find(friends[leaf])
    return friends[leaf]

def union(start, end):
    start = find(start)
    end = find(end)
    if start < end:
        friends[end] = start
        candies[0][start] += candies[0][end]
        candies[1][start] += candies[1][end]
        candies[0][end] = 0
        candies[1][end] = 0
    elif start > end:
        friends[start] = end
        candies[0][end] += candies[0][start]
        candies[1][end] += candies[1][start]
        candies[0][start] = 0
        candies[1][start] = 0

N, M, K = map(int, input().split())
candies = [[0] + list(map(int, input().split()))]
candies.append([0] + [1] * N)
friends = [i for i in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

for n in range(1, N + 1):
    find(n)

children = list(set(friends[1:]))
dp = [0] * K
for j in range(len(children)):
    for k in range(K - 1, 0, -1):
        if candies[1][children[j]] <= k:
            dp[k] = max(dp[k], dp[k - candies[1][children[j]]] + candies[0][children[j]])

print(dp[K-1])