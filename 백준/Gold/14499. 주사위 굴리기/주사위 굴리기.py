M, N, R, C, K = map(int, input().split())
mm = []
for i in range(M):
    mm += [list(map(int, input().split()))]

cmds = list(map(int, input().split()))

from collections import deque
dice = [-1,0,0,0,0,0,0]
direc = {4:[1,0], 3:[-1,0], 2:[0,-1],1:[0,1]}
for c in cmds:
    tr = R + direc[c][0]
    tc = C + direc[c][1]
    if tr < 0 or tc < 0 or tr >= M or tc >= N:
        continue
    R = tr
    C = tc
    if c == 4: ## South
        st = deque([dice[5]])
        dice[5] = dice[1]
        st += [dice[6]]
        dice[6] = st.popleft()
        st += [dice[2]]
        dice[2] = st.popleft()
        st += [dice[1]]
        dice[1] = st.popleft()
    elif c == 3: ## North
        st = deque([dice[1]])
        dice[1] = dice[5]
        st += [dice[2]]
        dice[2] = st.popleft()
        st += [dice[6]]
        dice[6] = st.popleft()
        st += [dice[5]]
        dice[5] = st.popleft()
    elif c == 2: ## West
        q = deque([dice[4]])
        dice[4] = dice[1]
        q += [dice[6]]
        dice[6] = q.popleft()
        q += [dice[3]]
        dice[3] = q.popleft()
        q += [dice[1]]
        dice[1] = q.popleft()
    elif c == 1: ## East
        q = deque([dice[3]])
        dice[3] = dice[1]
        q += [dice[6]]
        dice[6] = q.popleft()
        q += [dice[4]]
        dice[4] = q.popleft()
        q += [dice[1]]
        dice[1] = q.popleft()

    if mm[R][C] == 0:
        mm[R][C] = dice[6]
    else:
        dice[6] = mm[R][C]
        mm[R][C] = 0
    print(dice[1])