N, K = map(int, input().split())
num_list = list(map(int, input().split()))

count_dict = dict()

start = 0
end = 0
answer = 0

while end < N:
    if N - start < answer:
        break

    if num_list[end] in count_dict:
        if count_dict[num_list[end]] < K:
            count_dict[num_list[end]] += 1
            answer = max(answer, end - start + 1)
            end += 1
        else:
            count_dict[num_list[start]] -= 1
            start += 1

    else:
        count_dict.setdefault(num_list[end], 1)
        answer = max(answer, end - start + 1)
        end += 1

print(answer)