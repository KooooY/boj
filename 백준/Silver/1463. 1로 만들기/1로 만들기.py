N = int(input())
cnt_list = [0, 0, 1, 1]

for idx in range(4, N+1):
    if idx % 3 == 0 and idx % 2 == 0:
        cnt_list.append(min(cnt_list[idx//3], cnt_list[idx//2], cnt_list[idx-1])+1)
    elif idx % 3 == 0:
        cnt_list.append(min(cnt_list[idx//3], cnt_list[idx-1])+1)
    elif idx % 2 == 0:
        cnt_list.append(min(cnt_list[idx//2], cnt_list[idx-1])+1)
    else:
        cnt_list.append(cnt_list[idx-1]+1)

print(cnt_list[N])