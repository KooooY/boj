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

for j in range(P):
    plane = int(input())
    parking = find(plane)
    if parking > 0:
        gate[parking] -= 1
    else:
        print(j)
        break
    if j == P - 1:
        print(P)