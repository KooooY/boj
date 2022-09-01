n, m = map(int, input().split())
dna_list = []

for i in range(n):
    dna_list.append(str(input()))

result = ''
for j in range(m):
    count = []
    for k in range(n):
        count.append(dna_list[k][j])
    a = 0
    c = 0
    g = 0
    t = 0
    for l in count:
        if l == 'A':
            a += 1
        elif l == 'C':
            c += 1
        elif l == 'G':
            g += 1
        elif l == 'T':
            t += 1
    if a >= c and a >= g and a >= t:
        result += 'A'
    elif c > a and c >= g and c >= t:
        result += 'C'
    elif g > a and g > c and g >= t:
        result += 'G'
    elif t > a and t >=c and t >=g:
        result += 'T'

        
print(result)

ham_d = 0
for p in range(m):
    for q in range(n):
        if result[p] != dna_list[q][p]:
                ham_d += 1

print(ham_d)