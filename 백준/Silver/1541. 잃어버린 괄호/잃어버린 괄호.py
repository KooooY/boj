input_word = input().split('-')
ans = 0

for idx, val in enumerate(input_word):
    temp_sum = 0
    if '+' in val:
        temp = list(map(int, val.split('+')))
        temp_sum = sum(temp)
    else:
        temp_sum = int(val)

    if not idx:
        ans += temp_sum
    else:
        ans -= temp_sum

print(ans)