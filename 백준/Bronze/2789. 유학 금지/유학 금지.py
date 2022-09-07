origin_word = input()
new_word = ''

for i in origin_word:
    if i in 'CAMBRIDGE':
        continue
    else:
        new_word += i

print(new_word)