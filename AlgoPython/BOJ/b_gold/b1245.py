from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

visited = [[False] * m for i in range(n)]
ans = 0
row = [-1, 1, 0, 0, 1, 1, -1, -1]
col = [0, 0, 1, -1, 1, -1, 1, -1]


def bfs(sr, sc):
    h = grid[sr][sc]
    q = deque([(sr, sc)])
    high = True
    while q:
        r, c = q.popleft()
        for k in range(8):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if grid[nr][nc] == h and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True
            if grid[nr][nc] > h:
                high = False
    if high:
        return 1
    else:
        return 0


for i in range(n):
    for j in range(m):
        if not visited[i][j] and grid[i][j]:
            visited[i][j] = True
            ans += bfs(i, j)
print(ans)
