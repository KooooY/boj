import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x
    time = 1
    while True:
        if distance >= time ** 2:
            time += 1
        else:
            time -= 1
            break
    if time ** 2 == distance:
        time = time * 2 - 1
    else:
        rest = (distance - time ** 2) // time + bool((distance - time ** 2) % time)
        time = time * 2 + rest - 1

    print(time)