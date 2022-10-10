def make_X(num):
    if num == 1:
        return '0'
    else:
        i = 1
        while True:
            if num > 2**i:
                i += 1
            else:
                break
        if make_X(num-2**(i-1)) == '0':
            return '1'
        else:
            return '0'

print(make_X(int(input())))