'''
섬 갯수라 함은
1의 군집의 갯수
'''
from collections import deque

row = [-1, 1, 0, 0, 1, 1, -1, -1]
col = [0, 0, 1, -1, 1, -1, 1, -1]
while True:

    m, n = map(int, input().split())
    if m == n == 0:
        break
    grid = [list(map(int, input().split())) for i in range(n)]


    def bfs(r, c):
        q = deque([(r, c)])
        while q:
            r, c = q.popleft()
            for k in range(8):
                nr = r + row[k]
                nc = c + col[k]
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                if not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    q.append((nr, nc))


    ans = 0
    visited = [[False] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j)
                ans += 1
    print(ans)
