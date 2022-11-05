import sys
input =sys.stdin.readline 

N, H_a = map(int, input().split())
damage_max = 0
damage = 0

for i in range(1, N+1):
    t, a, h = map(int, input().split())
    if t == 1:
        temp = 0
        if h % H_a:
            temp = (h//H_a)*a
        else:
            temp = (h//H_a-1)*a
        damage += temp

    else:
        H_a += a
        if damage > damage_max:
            damage_max = damage
        if h > damage:
            damage = 0
        else:
            damage -= h

print(max(damage_max,damage)+1)