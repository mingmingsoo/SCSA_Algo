'''
bfs 군집 k 개 이상이면 한번에 떨어지고 중력 작용
lst에 들고다니면서 한번에 0처리
'''
from collections import deque

n, limit = map(int, input().split())
m = 10
grid = [list(map(int, input())) for i in range(n)]
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def bfs(i, j, num):
    global end
    q = deque([(i, j)])
    location = []
    while q:
        r, c = q.popleft()
        location.append((r, c))
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc] or grid[nr][nc] != num:
                continue
            visited[nr][nc] = True
            q.append((nr, nc))
    if len(location) >= limit:
        end = False
        for r, c in location:
            grid[r][c] = 0


while True:
    # 군집이 없으면 종료
    visited = [[False] * m for i in range(n)]
    end = True
    for i in range(n):
        for j in range(m):
            if grid[i][j] and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j, grid[i][j])
    if end:
        break
    # 그 담에 중력

    for j in range(m):
        while True:
            down = 0
            for i in range(n - 1, 0, -1):
                if grid[i][j] == 0 and grid[i - 1][j] != 0:
                    grid[i][j], grid[i - 1][j] = grid[i - 1][j], grid[i][j]
                    down = 1

            if down == 0:
                break
for _ in grid:
    print("".join(map(str, _)))
