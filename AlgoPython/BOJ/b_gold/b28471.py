'''
시작지점의 갯수니까
F에서 시작해서 visited 의 갯수
'''
from collections import deque

n = int(input())
grid = [list(input()) for i in range(n)]
visited = [[False] * n for i in range(n)]


def find():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "F":
                return i, j


sr, sc = find()
visited[sr][sc] = True

row = [-1, 0, 0, 1, 1, -1, -1]
col = [0, 1, -1, 1, -1, 1, -1]


def bfs(sr, sc):
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for k in range(7):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or grid[nr][nc] == "#":
                continue
            visited[nr][nc] = True
            q.append((nr, nc))


bfs(sr, sc)
visited[sr][sc] = False
print(sum(map(sum, visited)))
