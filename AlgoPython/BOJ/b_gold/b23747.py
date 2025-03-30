from collections import deque, defaultdict

n, m = map(int, input().split())

grid = [list(input()) for i in range(n)]
r, c = map(lambda x: int(x) - 1, input().split())
d_list = list(input())
visited = [["#"] * m for i in range(n)]

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


def bfs(r, c, region):
    visited[r][c] = "."
    q = deque([(r, c)])

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] != region or visited[nr][nc] == ".":
                continue
            q.append((nr, nc))
            visited[nr][nc] = "."


for dirs in d_list:
    if dirs == "W":
        # 와드
        if visited[r][c] == "#":
            bfs(r, c, grid[r][c])
    else:
        d = "URDL".index(dirs)
        r = r + row[d]
        c = c + col[d]
visited[r][c] = "."
for k in range(4):
    nr = r + row[k]
    nc = c + col[k]
    if not (0 <= nr < n and 0 <= nc < m):
        continue
    visited[nr][nc] = "."
for _ in visited:
    print("".join(_))
from collections import deque, defaultdict

n, m = map(int, input().split())

grid = [list(input()) for i in range(n)]
r, c = map(lambda x: int(x) - 1, input().split())
d_list = list(input())
visited = [["#"] * m for i in range(n)]

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


def bfs(r, c, region):
    visited[r][c] = "."
    q = deque([(r, c)])

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] != region or visited[nr][nc] == ".":
                continue
            q.append((nr, nc))
            visited[nr][nc] = "."


for dirs in d_list:
    if dirs == "W":
        # 와드
        if visited[r][c] == "#":
            bfs(r, c, grid[r][c])
    else:
        d = "URDL".index(dirs)
        r = r + row[d]
        c = c + col[d]
visited[r][c] = "."
for k in range(4):
    nr = r + row[k]
    nc = c + col[k]
    if not (0 <= nr < n and 0 <= nc < m):
        continue
    visited[nr][nc] = "."
for _ in visited:
    print("".join(_))
