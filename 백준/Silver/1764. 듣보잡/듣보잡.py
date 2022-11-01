N, M = map(int, input().split())
dbj_set = set()
ans = []

for _ in range(N+M):
    person = input()
    if person not in dbj_set:
        dbj_set.add(person)
    else:
        ans.append(person)

ans.sort()
print(len(ans))
for p in ans:
    print(p)