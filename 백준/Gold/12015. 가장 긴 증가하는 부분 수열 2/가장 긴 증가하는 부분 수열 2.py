N = int(input())
numbers = list(map(int, input().split()))
result = [0]

for number in numbers:
    if result[-1] < number:
        result.append(number)
    else:
        left = 0
        right = len(result) - 1
        while left <= right:
            mid = (left + right) // 2
            if result[mid] >= number:
                right = mid - 1
            else:
                left = mid + 1
        result[right + 1] = number

print(len(result) - 1)