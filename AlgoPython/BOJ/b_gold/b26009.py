from collections import deque

n, m = map(int, input().split())
block = int(input())

grid = [[0] * m for i in range(n)]

for b in range(block):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    origin_r = r
    origin_d = d
    while d >= 0 and r >= 0:  # 일단 위로,,,
        nc1 = c - d
        nc2 = c + d
        if 0 <= r < n and 0 <= nc1 < m:
            grid[r][nc1] = 1
        if 0 <= r < n and 0 <= nc2 < m:
            grid[r][nc2] = 1
        r -= 1
        d -= 1
    d = origin_d
    r = origin_r
    while d >= 0 and r < n:  # 아래로..
        nc1 = c - d
        nc2 = c + d
        if 0 <= r < n and 0 <= nc1 < m:
            grid[r][nc1] = 1
        if 0 <= r < n and 0 <= nc2 < m:
            grid[r][nc2] = 1
        r += 1
        d -= 1

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def bfs():
    visited = [[False] * m for i in range(n)]
    visited[0][0] = True
    q = deque([(0, 0, 0)])
    while q:
        r, c, d = q.popleft()
        if (r, c) == (n - 1, m - 1):
            return d
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc] or grid[nr][nc]:
                continue
            visited[nr][nc] = True
            q.append((nr, nc, d + 1))
    return -1


cnt = bfs()
if cnt == -1:
    print("NO")
else:
    print("YES")
    print(cnt)
