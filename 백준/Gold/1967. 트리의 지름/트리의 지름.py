from collections import deque
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(next_info, dis):
    global answer
    global furthest_node
    global visited

    dis += next_info[1]

    for info in tree_info[next_info[0]]:
        if info[0] not in visited:
            visited.add(info[0])
            dfs(info, dis)

    if dis > answer:
        answer = dis
        furthest_node = next_info[0]

    return

n = int(input())
if n == 1:
    print(0)
else:
    tree_info = dict()
    furthest_node = 99999
    answer = 0

    for i in range(1, n+1):
        tree_info[i] = set()

    for _ in range(n-1):
        a, b, c = map(int, input().split())
        tree_info[a].add((b, c))
        tree_info[b].add((a, c))

    visited = {1}
    dfs((1, 0), 0)

    visited = {furthest_node}
    answer = 0

    dfs((furthest_node, 0), 0)

    print(answer)