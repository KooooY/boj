N, a, b = map(int, input().split())
buildings = []

if a + b < N + 2:
    if a <= b:
        if a > 1:
            if a + b < N + 1:
                for _ in range(N + 1 - a - b):
                    buildings.append(1)

            for i in range(1, a):
                buildings.append(i)

            for j in range(b, 0, -1):
                buildings.append(j)

        if a == 1:
            buildings.append(b)

            for _ in range(N - b):
                buildings.append(1)

            for k in range(b - 1, 0, -1):
                buildings.append(k)

    else:
        if b > 1:
            if a + b < N + 1:
                for _ in range(N + 1 - a - b):
                    buildings.append(1)

            for i in range(1, a + 1):
                buildings.append(i)

            for j in range(b - 1, 0, -1):
                buildings.append(j)

        if b == 1:
            for _ in range(N - a):
                buildings.append(1)

            for k in range(1, a + 1):
                buildings.append(k)

else:
    buildings.append(-1)

print(*buildings)