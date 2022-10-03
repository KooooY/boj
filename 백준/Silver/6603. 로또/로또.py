def combination(idx, sidx):
    if sidx == 6:
        print(*sel)
        return

    if idx == k:
        return

    sel[sidx] = arr[idx]
    combination(idx+1, sidx+1)
    combination(idx+1, sidx)


while True:
    num_list = list(map(int, input().split()))
    if num_list == [0]:
        break
    k = num_list[0]
    arr = num_list[1:]
    sel = [0]*6
    arr_list = []

    combination(0,0)
    print()