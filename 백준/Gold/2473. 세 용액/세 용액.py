N = int(input())
solution_info = list(map(int, input().split()))
solution_info.sort()
answer = [1000000000, 1000000000, 1000000000]

for i in range(N):
    start = i + 1
    end = N - 1

    while start < end:
        temp = solution_info[start] + solution_info[i] + solution_info[end]
        if abs(temp) < abs(sum(answer)):
            answer = [solution_info[i], solution_info[start], solution_info[end]]

        if not temp:
            break
        elif temp < 0:
            start += 1
        else:
            end -= 1

print(*answer)