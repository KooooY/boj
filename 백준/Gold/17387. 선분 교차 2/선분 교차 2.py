import sys
input = sys.stdin.readline

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
p1, p2, p3, p4 = [x1, y1], [x2, y2], [x3, y3], [x4, y4]
cross1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
cross2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)
ans = 0
if cross1 == cross2 == 0:
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2): #두 직선이 겹치면 (점끼리 만나는 것도 포함)
        ans = 1
elif cross1 <= 0 and cross2 <= 0:
    ans = 1
print(ans)