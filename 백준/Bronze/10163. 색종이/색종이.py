N = int(input())
matrix = [[0]*1001 for _ in range(1001)]

for i in range(1,N+1):
    info = list(map(int, input().split()))
    for j in range(info[0], info[0]+info[2]):
        change = [i] * info[3]
        matrix[j] = matrix[j][:info[1]] + change + matrix[j][info[1]+info[3]:]
        
for p in range(1, N + 1):
    count = 0
    for l in matrix:
        count += l.count(p)
    print(count)