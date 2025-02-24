'''
문제설명
    L 인 모든점에서 구함.
    bfs풀이
'''
from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]

ans = 0
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def bfs(r, c):
    global ans
    visited[r][c] = True
    q = deque([(r, c, 0)])

    while q:
        r, c, dist = q.popleft()
        ans = max(ans, dist)
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]

            if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] == "W":
                continue
            if not visited[nr][nc]:
                q.append((nr, nc, dist + 1))
                visited[nr][nc] = True


for i in range(n):
    for j in range(m):
        if grid[i][j] == "L":
            visited = [[False] * m for i in range(n)]
            bfs(i,j)

print(ans)
