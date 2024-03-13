import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(leaf):
    if gate[leaf] != leaf:
        gate[leaf] = find(gate[leaf])
    return gate[leaf]

G = int(input())
P = int(input())

gate = [i for i in range(G + 1)]
ans = 0

for j in range(P):
    plane = int(input())
    if find(plane) > 0:
        gate[find(plane)] -= 1
        ans += 1
    else:
        break

print(ans)