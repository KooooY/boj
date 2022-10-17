import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
node_info = [tuple(map(int, input().split())) for _ in range(M)]

Q = [X, 'a']
visited = {X}
cnt = 0
ans = []

while cnt < K and Q != ['a']:
    item = Q.pop(0)
    if item == 'a':
        if cnt == K-1:
            Q.sort()
            for i in Q:
                print(i)
            break
        else:
            Q.append('a')
            cnt += 1
    else:
        for i in node_info:
            if i[0] == item and i[1] not in visited:
                Q.append(i[1])
                visited.add(i[1])

if Q == ['a']:
    print(-1)