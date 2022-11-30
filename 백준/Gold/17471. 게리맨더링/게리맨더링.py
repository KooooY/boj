N = int(input())
adj_arr = [[0]*(N) for _ in range(N)]
dist = list(map(int, input().split()))
village = [i for i in range(N)]
total = sum(dist)
ans = total

for idx in range(N):
    adj_info = list(map(int, input().split()))
    for n in adj_info[1:]:
        adj_arr[idx][n-1] = 1
        adj_arr[n-1][idx] = 1

powerset = []
for i in range(1 << N):
    sel = []
    for j in range(N):
        if i & 1 << j:
            sel.append(j)
    powerset.append(sel)

powerset.remove([])
powerset.remove(village)

for k in powerset:
    Q = [k[0]]
    visited = {k[0]}

    while Q:
        item = Q.pop(0)
        for des in k:
            if adj_arr[item][des] and des not in visited:
                Q.append(des)
                visited.add(des)

    if visited == set(k):
        another = list(set(village) - set(k))
        Q_a = [another[0]]
        visited_a = {another[0]}
        while Q_a:
            item_a = Q_a.pop(0)
            for des_a in another:
                if adj_arr[item_a][des_a] and des_a not in visited_a:
                    Q_a.append(des_a)
                    visited_a.add(des_a)
        if visited_a == set(another):
            temp_sum = 0
            for p in k:
                temp_sum += dist[p]
            if abs(total - 2*temp_sum) < ans:
                ans = abs(total - 2*temp_sum)
if ans < total:
    print(ans)

else:
    print(-1)