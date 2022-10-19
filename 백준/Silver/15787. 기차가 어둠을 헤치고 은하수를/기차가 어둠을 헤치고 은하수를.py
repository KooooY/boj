N, M = map(int, input().split())
request = [list(map(int, input().split())) for _ in range(M)]
train = [[0]*20 for _ in range(N)]

for i in range(M):
    if len(request[i]) == 3:
        number = request[i][1]-1
        seat = request[i][2]-1
        if request[i][0] == 1:
            train[number][seat] = 1
        else:
            train[number][seat] = 0
    else:
        number = request[i][1]-1
        if request[i][0] == 3:
            train[number] = [0] + train[number][:19]
        else:
            train[number] = train[number][1:] + [0]

for j in range(N):
    train[j] = tuple(train[j])

train = set(train)
print(len(train))