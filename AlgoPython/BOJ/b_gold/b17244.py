'''
순열로 푼다 칵씨
'''
import heapq
from collections import deque

m, n = map(int, input().split())
grid = [list(input()) for i in range(n)]
keys = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            sr, sc = i, j
        if grid[i][j] == "X":
            keys.append((i, j))
        if grid[i][j] == "E":
            er, ec = i, j

visited = [False] * len(keys)

sel = [(sr, sc)] + [0] * len(keys) + [(er, ec)]

ans = int(1e9)
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def bfs(r, c, er, ec):
    visited = [[False] * m for i in range(n)]
    visited[r][c] = True
    q = deque([(r, c, 0)])
    while q:
        r, c, d = q.popleft()
        if (r, c) == (er, ec):
            return d
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc] or grid[nr][nc] == "#":
                continue
            visited[nr][nc] = True
            q.append((nr, nc, d + 1))

def perm(idx):
    global ans
    if idx == len(keys) + 1:
        r, c = sel[0]
        dist = 0
        for i in range(1, len(sel)):
            nr, nc = sel[i]
            dist += bfs(r, c, nr, nc)
            r = nr
            c = nc
        ans = min(dist, ans)
        return
    for i in range(len(keys)):
        if not visited[i]:
            visited[i] = True
            sel[idx] = keys[i]
            perm(idx + 1)
            visited[i] = False


perm(1)
print(ans)
