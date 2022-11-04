N, K = map(int, input().split())

if N == K:
    print(0)
else:
    Q = [N, 'a']
    visited = {N}
    cnt = 1
    flag = 1

    while Q and flag:
        item = Q.pop(0)
        if item == 'a':
            Q.append('a')
            cnt += 1
            continue
        for i in [item-1, item+1, item*2]:
            if i == K:
                flag = 0
                break
            if i not in visited and 0 <= i <= 100000:
                Q.append(i)
                visited.add(i)

    print(cnt)