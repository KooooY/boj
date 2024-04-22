import sys
sys.setrecursionlimit(10 ** 8)


def checkT(end):
    global answer
    if end == S:
        answer = 1
        return
    if len(end) <= len(S):
        return
    if end[-1] == 'A':
        checkT(end[:len(end)-1])
    if end[0] == 'B':
        tmp = end[::-1]
        checkT(tmp[:len(end)-1])
    return



S = input()
T = input()
answer = 0
checkT(T)
print(answer)
