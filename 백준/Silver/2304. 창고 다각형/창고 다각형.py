N = int(input())

column_list = [list(map(int, input().split())) for _ in range(N)]
column_list.sort()

column = [0]*(column_list[N-1][0]+1)

for i in range(N):
    column[column_list[i][0]] = column_list[i][1]

height = 0
area = 0
point = column.index(max(column))
other_p = 0
l_height = 0
r_height = 0

for i in range(0, point):
    if column[i] == max(column):
        break
    if column[i] > height:
        area += (column[i]-height)*(point-i)
        height = column[i]
        l_height = column[i]

height = 0
for j in range(len(column)-1, 0, -1):
    if column[j] == max(column):
        other_p = j
        break
    if column[j] > height:
        area += (column[j]-height)*(j-point+1)
        height = column[j]
        r_height = column[j]

if point != other_p:
    if r_height >= l_height:
        area += (other_p - point + 1) * (max(column) - r_height)
    else:
        area += (other_p - point + 1) * (max(column) - l_height) + other_p - r_height
else:
    area += (max(column)-r_height)

print(area)