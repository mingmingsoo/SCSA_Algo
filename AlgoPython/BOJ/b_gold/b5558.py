'''
각각의 목표 치즈를 향해 bfs 매번 실행
'''
from collections import deque


def find():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "S":
                return i, j


def bfs(r, c, taret):
    global sr, sc
    q = deque([(r, c, 0)])
    while q:
        r, c, time = q.popleft()

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] == "X" or visited[nr][nc]:
                continue
            if grid[nr][nc] == str(taret):
                sr, sc = nr, nc
                return time + 1
            else:
                q.append((nr, nc, time + 1))
                visited[nr][nc] = True


n, m, last = map(int, input().split())
grid = [list(input()) for i in range(n)]

sr, sc = find()
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
ans = 0

for target in range(1, last + 1):
    visited = [[False] * m for i in range(n)]
    visited[sr][sc] = True
    ans += bfs(sr, sc, target)

print(ans)
