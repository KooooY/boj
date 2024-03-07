import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    Q_asc = []
    Q_desc = []
    put_number = dict()
    answer = []
    count = 0

    for i in range(k):
        s, t = map(str, input().split())
        if s == 'I':
            if int(t) in put_number:
                put_number[int(t)] += 1
            else:
                put_number[int(t)] = 1
            heapq.heappush(Q_asc, int(t))
            heapq.heappush(Q_desc, (int(t) * (-1), int(t)))
            count += 1
        else:
            if count > 0:
                count -= 1
                if int(t) == 1:
                    while True:
                        get_desc = heapq.heappop(Q_desc)[1]
                        if put_number[get_desc] > 0:
                            put_number[get_desc] -= 1
                            break
                else:
                    while True:
                        get_asc = heapq.heappop(Q_asc)
                        if put_number[get_asc] > 0:
                            put_number[get_asc] -= 1
                            break
            else:
                Q_asc = []
                Q_desc = []

    if count > 0:
        while len(answer) < 1:
            temp_desc = heapq.heappop(Q_desc)[1]
            if put_number[temp_desc] > 0:
                answer.append(temp_desc)
        while len(answer) < 2:
            temp_asc = heapq.heappop(Q_asc)
            if put_number[temp_asc] > 0:
                answer.append(temp_asc)
        print(*answer)
    else:
        print('EMPTY')