N = int(input())
acidity = list(map(int, input().split()))

left = 0
right = N - 1
answer = [left, right]
property_value = acidity[left] + acidity[right]

while left < right:
    if acidity[left] + acidity[right] <= 0:
        left += 1
    else:
        right -= 1
    if left < right and abs(acidity[left] + acidity[right]) < abs(property_value):
        answer = [left, right]
        property_value = acidity[left] + acidity[right]

print(acidity[answer[0]], acidity[answer[1]])