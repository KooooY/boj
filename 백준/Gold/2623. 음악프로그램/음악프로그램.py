N, M = map(int, input().split())
adj_dict = {i:set() for i in range(1, N+1)}
singer = [s for s in range(1, N+1)]
ans = []

for _ in range(M):
    temp = list(map(int, input().split()))
    for i in range(1, temp[0]):
        adj_dict[temp[i+1]].update(temp[1:i+1])

Q = []

for j in adj_dict:
    if not adj_dict[j]:
        Q.append(j)

while Q:
    item = Q.pop(0)
    ans.append(item)
    singer.remove(item)

    for k in singer:
        if item in adj_dict[k]:
            adj_dict[k].remove(item)
            if not adj_dict[k]:
                Q.append(k)

if singer:
    print(0)
else:
    for s in ans:
        print(s)