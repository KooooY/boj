N = int(input())
tip_list = []
total_tip = 0

for _ in range(N):
    tip_list.append(int(input()))
tip_list.sort(reverse=True)

for i, v in enumerate(tip_list):
    if v - i >= 0:
        total_tip += v - i

print(total_tip)