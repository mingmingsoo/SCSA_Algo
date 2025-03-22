'''
visited를 쓰면안됨!!
.##
.##
.## 이런 맵일 경우 기다리면 되기 때문에..

'''
from collections import deque

n = 8
grid = [list(input()) for i in range(n)]

ans = 0
row = [0, 0, 0, 1, -1, 1, 1, -1, -1]
col = [0, 1, -1, 0, 0, 1, -1, 1, -1]


def bfs():
    global ans
    r, c = n - 1, 0
    q = deque([(r, c)])
    while q:
        q_size = len(q)
        for qs in range(q_size):
            r, c = q.popleft()
            if r == 0 and c == n - 1:
                ans = 1
                return
            if grid[r][c] == "#":
                continue
            for k in range(9):
                nr = r + row[k]
                nc = c + col[k]
                if not (0 <= nr < n and 0 <= nc < n) or grid[nr][nc] =="#":
                    continue
                q.append((nr, nc))

        grid.pop()
        grid.insert(0, ["."] * n)

bfs()
print(ans)