face = input()
left = 0
right = 0

for i in face:
    if i == '@':
        left += 1
    elif i == '(':
        break
    else:
        continue

for j in face[::-1]:
    if j == '@':
        right += 1
    elif j == '(':
        break
    else:
        continue

print(left, right)