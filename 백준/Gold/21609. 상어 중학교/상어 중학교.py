import sys
import heapq
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def gravity():
    global block_info

    for col in range(N):
        black = -1
        need_change = 0
        for row in range(N):
            if block_info[row][col] == -1:
                black = row
                need_change = 0
            elif block_info[row][col] == -999 and need_change:
                for b in range(row, black + 1, -1):
                    block_info[b][col] = block_info[b - 1][col]
                block_info[black + 1][col] = -999
            else:
                need_change = 1


def cnt_block():
    blocks_cnt = []
    normal_visited = set()
    for i in range(N):
        for j in range(N):
            if block_info[i][j] > 0 and (i, j) not in normal_visited:
                blocks = set()
                standard = (i, j)
                stack = [(i, j)]
                blocks.add((i, j))
                cnt = 1
                rainbow = 0
                while stack:
                    cur_r, cur_c = stack.pop()
                    for d in range(4):
                        if 0 <= cur_r + dr[d] < N and 0 <= cur_c + dc[d] < N and block_info[cur_r + dr[d]][cur_c + dc[d]] in {0, block_info[i][j]} and (cur_r + dr[d], cur_c + dc[d]) not in blocks:
                            stack.append((cur_r + dr[d], cur_c + dc[d]))
                            blocks.add((cur_r + dr[d], cur_c + dc[d]))
                            if not block_info[cur_r + dr[d]][cur_c + dc[d]]:
                                rainbow += 1
                            else:
                                normal_visited.add((cur_r + dr[d], cur_c + dc[d]))
                            cnt += 1

                            if cur_r + dr[d] <= standard[0] and block_info[cur_r + dr[d]][cur_c + dc[d]]:
                                if cur_c + dc[d] < standard[1]:
                                    standard = (cur_r + dr[d], cur_c + dc[d])
                heapq.heappush(blocks_cnt, (-1 * cnt, rainbow, standard, blocks))

    if not blocks_cnt or blocks_cnt[0][0] > -2:
        return 0
    else:
        max_block = heapq.heappop(blocks_cnt)
        max_blocks = []
        heapq.heappush(max_blocks, (-1 * max_block[1], max_block[2], max_block[3]))
        while blocks_cnt:
            cur = heapq.heappop(blocks_cnt)
            if cur[0] == max_block[0]:
                heapq.heappush(max_blocks, (-1 * cur[1], cur[2], cur[3]))
            else:
                break
        if len(max_blocks) < 2:
            return max_block[3]
        else:
            max_rainbow = heapq.heappop(max_blocks)
            max_rainbows = []
            heapq.heappush(max_rainbows, (-1 * max_rainbow[1][0], max_rainbow[1][1], max_rainbow[2]))
            while max_blocks:
                cur = heapq.heappop(max_blocks)
                if cur[0] == max_rainbow[0]:
                    heapq.heappush(max_rainbows, (-1 * cur[1][0], cur[1][1], cur[2]))
                else:
                    break
            if len(max_rainbows) < 2:
                return max_rainbow[2]
            else:
                max_standard_r = heapq.heappop(max_rainbows)
                max_standard_rs = []
                heapq.heappush(max_standard_rs, (-1 * max_standard_r[1], max_standard_r[2]))
                while max_rainbows:
                    cur = heapq.heappop(max_rainbows)
                    if cur[0] == max_standard_r[0]:
                        heapq.heappush(max_standard_rs, (-1 * cur[1], cur[2]))
                    else:
                        break
                if len(max_standard_rs) < 2:
                    return max_standard_r[2]
                else:
                    max_standard_c = heapq.heappop(max_standard_rs)
                    return max_standard_c[1]


N, M = map(int, input().split())
block_info = [list(map(int, input().split())) for _ in range(N)]
answer = 0

while True:
    delete_blocks = cnt_block()

    if not delete_blocks:
        break

    answer += len(delete_blocks) ** 2

    for r, c in delete_blocks:
        block_info[r][c] = -999

    gravity()

    new_block_info = []
    for c in range(N - 1, -1, -1):
        temp = []
        for r in range(N):
            temp.append(block_info[r][c])
        new_block_info.append(temp)

    block_info = new_block_info

    gravity()

print(answer)