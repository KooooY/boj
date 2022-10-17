import sys
input = sys.stdin.readline

N = int(input())

coordinate = [tuple(map(int, input().split())) for _ in range(N)]
sel = [0]*3

ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sel = [coordinate[i], coordinate[j], coordinate[k]]
            tri_1 = (sel[0][0]-sel[1][0])**2+(sel[0][1]-sel[1][1])**2
            tri_2 = (sel[1][0]-sel[2][0])**2+(sel[1][1]-sel[2][1])**2
            tri_3 = (sel[2][0]-sel[0][0])**2+(sel[2][1]-sel[0][1])**2
            if tri_1 + tri_2 + tri_3 == 2*max(tri_1, tri_2, tri_3):
                ans += 1

print(ans)