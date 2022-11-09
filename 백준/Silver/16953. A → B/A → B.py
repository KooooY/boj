A, B = map(int, input().split())

Q = [A, 'a']
visited = {A}

cnt = 1
while Q != ['a']:
    item = Q.pop(0)
    if item == 'a':
        Q.append('a')
        cnt += 1
        continue
    for i in [item*2, int(str(item)+'1')]:
        if i <= B and i not in visited:
            Q.append(i)
            visited.add(i)
    if B in visited:
        cnt += 1
        break


if B in visited:
    print(cnt)
else:
    print(-1)