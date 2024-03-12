N, T = map(int, input().split())
parent = [i for i in range(N)]


def find(x):
    if x != parent[x]:
        x = find(parent[x])
    return parent[x]


def union_parent(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
        return False
    elif x > y:
        parent[x] = y
        return False
    else:
        return True


for i in range(1, T+1):
    x, y = map(int, input().split())
    if union_parent(find(x), find(y)):
        print(i)
        break
    elif i == T:
        print(0)