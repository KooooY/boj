import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    direction = 1
    num_list = []
    numbers = input().rstrip()
    flag = 1

    if len(numbers) > 2:
        num_list = deque(map(int, numbers[1:-1].split(',')))

    for action in p:
        if action == 'R':
            if direction:
                direction = 0
            else:
                direction = 1
        else:
            if num_list:
                if direction:
                    num_list.popleft()
                else:
                    num_list.pop()
            else:
                print('error')
                flag = 0
                break
    if flag:
        if direction:
            print(''.join(str(list(num_list)).split(' ')))
        else:
            num_list.reverse()
            print(''.join(str(list(num_list)).split(' ')))