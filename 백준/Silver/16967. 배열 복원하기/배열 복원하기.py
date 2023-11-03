H, W, X, Y = map(int, input().split())

arr_B = []
for _ in range(H+X):
    temp_b = list(map(int, input().split()))
    arr_B.append(temp_b)

arr_A = []
for i in range(H):
    if i < X :
        arr_A.append(arr_B[i][:W])
        print(*arr_B[i][:W])
    else:
        temp = []
        for j in range(W):
            if j < Y:
                temp.append(arr_B[i][j])
            else:
                temp.append(arr_B[i][j] - arr_A[i-X][j-Y])
        arr_A.append(temp)
        print(*temp)