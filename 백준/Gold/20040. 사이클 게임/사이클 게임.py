import sys
input = sys.stdin.readline

def find(leaf):
    if parents[leaf] != leaf:
        leaf = find(parents[leaf])
    return parents[leaf]

def union(start, end):
    start = find(start)
    end = find(end)
    if start > end:
        parents[start] = end
        return False
    elif start < end:
        parents[end] = start
        return False
    else:
        return True

n, m = map(int, input().split())
answer = 0
parents = [i for i in range(n)]
rank = [1 for _ in range(n)]

for j in range(m):
    start, end = map(int, input().split())
    if union(start, end):
        answer = j + 1
        break

print(answer)