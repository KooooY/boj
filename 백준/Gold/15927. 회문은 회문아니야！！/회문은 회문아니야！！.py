string = input()
str_len = len(string)


if string != string[::-1]:
    print(str_len)
else:
    if len(set(list(string))) == 1:
        print(-1)
    else:
        print(str_len - 1)