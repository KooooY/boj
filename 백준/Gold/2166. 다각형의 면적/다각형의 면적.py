import sys
input = sys.stdin.readline

N = int(input())
x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())
answer = 0

for _ in range(N - 2):
    x_3, y_3 = map(int, input().split())
    answer += ((x_1 * y_2) + (x_2 * y_3) + (x_3 * y_1) - (y_1 * x_2) - (y_2 * x_3) - (y_3 * x_1)) / 2
    x_2, y_2 = x_3, y_3

print(round(abs(answer), 1))