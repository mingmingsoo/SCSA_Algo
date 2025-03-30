'''
먼소리고..
진우에서 시작해서 선생님 만나면 선생님으로 바꿔줌.

5 5
T####
J####
.####
.####
....S
'''
from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]

sr, sc, er, ec = -1, -1, -1, -1
visited_j = [[0] * m for i in range(n)]
visited_t = [[0] * m for i in range(n)]
jq = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == "J":
            sr, sc = i, j
            jq.append((i, j))
        elif grid[i][j] == "S":
            er, ec = i, j

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

visited_j[sr][sc] = 1
time = 0
tq = []


def bfs():
    global time
    while jq or tq:
        if time % 2 == 0:
            for jqs in range(len(jq)):
                r, c = jq.pop(0)
                if (r, c) == (er, ec):
                    return time + 2
                for k in range(4):
                    nr = r + row[k]
                    nc = c + col[k]
                    if not (0 <= nr < n and 0 <= nc < m) or visited_j[nr][nc] or grid[nr][nc] == "#":
                        continue
                    if grid[nr][nc] == "T":
                        visited_t[nr][nc] = 1
                        tq.append((nr, nc))
                    else:
                        visited_j[nr][nc] = 1
                        jq.append((nr, nc))

        for tqs in range(len(tq)):
            r, c = tq.pop(0)
            if (r, c) == (er, ec):
                return time + 2
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if not (0 <= nr < n and 0 <= nc < m) or visited_t[nr][nc] or grid[nr][nc] == "#":
                    continue
                visited_t[nr][nc] = 1
                tq.append((nr, nc))
        time += 1
    return -1


ans = bfs()
print(ans)
