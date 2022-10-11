n = int(input())

if n == 0:
    print(0)
    print(0)
else:
    Fibonacci = [0, 1]

    for i in range(2, abs(n)+1):
        Fibonacci.append((Fibonacci[i-1]+Fibonacci[i-2])%1000000000)

    if n > 0 :
        print(1)
        print(Fibonacci[n])

    else:
        if (-n)%2 == 0:
            print(-1)
        else:
            print(1)
        print(Fibonacci[(-n)])