sample_str = input()
str_bomb = list(input())
answer = []

for i in sample_str:
    answer.append(i)
    if answer[len(answer) - len(str_bomb):] == str_bomb:
        for _ in str_bomb:
            answer.pop()

if answer:
    print(''.join(map(str, answer)))
else:
    print('FRULA')