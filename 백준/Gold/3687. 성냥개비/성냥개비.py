import sys
input = sys.stdin.readline

T = int(input())
numbers = {7: 8, 6: 6, 5: 2, 4: 4, 3: 7, 2: 1}

for _ in range(T):
    n = int(input())

    max_num = 0
    if n % 2:
        max_num = int('7' + '1' * ((n - 3) // 2))
    else:
        max_num = int('1' * (n // 2))

    min_num = 0
    if not n % 7:
        min_num = int('8' * (n // 7))
    elif n < 8:
        min_num = numbers[n]
    else:
        if n % 7 == 1:
            min_num = int('10' + '8' * ((n // 7) - 1))
        elif n % 7 == 2:
            min_num = int('18' + '8' * ((n // 7) - 1))
        elif n == 10:
            min_num = 22
        elif n % 7 == 3:
            min_num = int('200' + '8' * ((n // 7) - 2))
        elif n % 7 == 4:
            min_num = int('20' + '8' * ((n // 7) - 1))
        elif n % 7 == 5:
            min_num = int('28' + '8' * ((n // 7) - 1))
        elif n % 7 == 6:
            min_num = int('68' + '8' * ((n // 7) - 1))

    print(min_num, max_num)