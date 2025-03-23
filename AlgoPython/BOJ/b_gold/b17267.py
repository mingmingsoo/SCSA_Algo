'''
외틀려
'''
from collections import deque

n, m = map(int, input().split())
L, R = map(int, input().split())
grid = [list(map(int, input())) for i in range(n)]

visited = [[0] * m for i in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            q.append((i, j, L, R))
            visited[i][j] = 1
            grid[i][j] = 0

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
dir_dict = {"L": 3, "R": 2}
while q:
    r, c, L, R = q.popleft()
    ori_r, ori_c = r, c
    for k in range(2):  # 상, 하 무제한
        r = ori_r
        c = ori_c
        while True:
            nr = r + row[k]
            nc = c + col[k]
            if (0 <= nr < n and 0 <= nc < m) and not visited[nr][nc] and grid[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append((nr, nc, L, R))
                r = nr
                c = nc
            else:
                break
    r, c = ori_r, ori_c
    if L > 0:
        k = dir_dict["L"]
        nr = r + row[k]
        nc = c + col[k]
        if (0 <= nr < n and 0 <= nc < m) and not visited[nr][nc] and grid[nr][nc] == 0:
            visited[nr][nc] = 1
            q.append((nr, nc, L - 1, R))
    if R > 0:
        k = dir_dict["R"]
        nr = r + row[k]
        nc = c + col[k]
        if (0 <= nr < n and 0 <= nc < m) and not visited[nr][nc] and grid[nr][nc] == 0:
            visited[nr][nc] = 1
            q.append((nr, nc, L, R - 1))
print(sum(map(sum, visited)))
