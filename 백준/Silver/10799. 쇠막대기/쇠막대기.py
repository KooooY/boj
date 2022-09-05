cutting_count = 0
stick = input()
stick = stick.replace('()', '_')

while '(' in stick:
    i = stick.rfind('(')
    j = stick.find(')',i)
    cutting_count += stick[i:j].count('_') + 1
    stick = stick[:i] + stick[i+1:j] + stick[j+1:]

print(cutting_count)