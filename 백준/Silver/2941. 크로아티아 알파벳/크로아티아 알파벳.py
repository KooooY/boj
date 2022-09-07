original_word = input()
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatian:
    if i in original_word:
        original_word = original_word.replace(i, '+')

print(len(original_word))
