import heapq
from collections import deque

# print(4 * 4 * 4 * 4 * 4 * 5 * 4 * 3 * 2 * 1 * 4) # 491520
# 회전시킨다.

hyper = [[list(map(int, input().split())) for i in range(5)] for h in range(5)]


h_list = []
visited = [False] * 5
sel = [0] * 5
ans = 126


def perm(idx):
    if idx == 5:
        h_list.append(sel[:])
        return
    for i in range(5):
        if not visited[i]:
            visited[i] = True
            sel[idx] = i
            perm(idx + 1)
            visited[i] = False


perm(0)
# print(h_list)
hei = [1, -1, 0, 0, 0, 0]
row = [0, 0, 1, -1, 0, 0]
col = [0, 0, 0, 0, 1, -1]

find = False
def bfs(h, r, c, eh, er, ec, hyper):
    global find
    if find:
        return
    global ans
    visited = [[[False] * 5 for i in range(5)] for i in range(5)]
    visited[h][r][c] = True

    q = deque([(0, h, r, c)])

    while q:
        dist, h, r, c = q.popleft()
        if dist >= ans:
            return
        if h == eh and c == ec and r == er:
            ans = min(ans, dist)
            if ans == 12:
                find = True
                return
            return
        for k in range(6):
            nh = h + hei[k]
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nh < 5 and 0 <= nr < 5 and 0 <= nc < 5) or visited[nh][nr][nc]:
                continue
            if hyper[nh][nr][nc] == 1:
                visited[nh][nr][nc] = True
                q.append((dist + 1, nh, nr, nc))


def rotate(hyper, idx, origin_hyper):
    for i in range(5):
        for j in range(5):
            hyper[idx][i][j] = origin_hyper[idx][j][5 - i - 1]


def btk(idx):
    global find
    if find:
        return
    if idx == 5:
        for h_arr in h_list:
            new_hyper = []
            for h in h_arr:
                new_hyper.append(hyper[h])
            # print("---------------------")
            # for _ in new_hyper:
            #     print(_)
            if new_hyper[0][0][0] == 1:
                bfs(0, 0, 0, 4, 4, 4, new_hyper)
            if new_hyper[0][4][0] == 1:
                bfs(0, 4, 0, 4, 0, 4, new_hyper)
            if new_hyper[0][4][4] == 1:
                bfs(0, 4, 4, 4, 0, 0, new_hyper)
            if new_hyper[0][0][4] == 1:
                bfs(0, 0, 4, 4, 4, 0, new_hyper)
        return

    # 회전 없이 간다.
    btk(idx + 1)

    # origin_hyper = [[ii[:] for ii in jj] for jj in hyper]
    origin_hyper = [[[0] * 5 for i in range(5)] for i in range(5)]
    for h in range(5):
        for i in range(5):
            for j in range(5):
                origin_hyper[h][i][j] = hyper[h][i][j]

    # 1번 회전
    rotate(hyper, idx, origin_hyper)
    btk(idx + 1)

    # 2번 회전
    for h in range(5):
        for i in range(5):
            for j in range(5):
                origin_hyper[h][i][j] = hyper[h][i][j]
    rotate(hyper, idx, origin_hyper)

    btk(idx + 1)

    # 3번 회전
    for h in range(5):
        for i in range(5):
            for j in range(5):
                origin_hyper[h][i][j] = hyper[h][i][j]
    rotate(hyper, idx, origin_hyper)
    btk(idx + 1)


btk(0)
if ans == 126:
    print(-1)
else:
    print(ans)
