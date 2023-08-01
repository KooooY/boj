while True:
    pills = int(input())
    if not pills:
        break
    numerate = 1
    denominator = 1

    for p in range(pills+1, 2*pills+1):
        numerate *= p
    for q in range(1, pills+2):
        denominator *= q

    print(numerate//denominator)