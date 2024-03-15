import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    answer = n
    for i in range(1, n + 1):
        if students[i]:
            count = 1
            Q = [i]
            team = [i]
            while Q:
                cur = Q.pop()
                if students[cur] == i:
                    answer -= count
                elif students[cur] == cur:
                    count = 1
                    answer -= count
                elif students[cur]:
                    Q.append(students[cur])
                    team.append(students[cur])
                    count += 1
                else:
                    if count > 2 and cur in team:
                        answer -= (count - team.index(cur) - 1)
                students[cur] = 0
    print(answer)