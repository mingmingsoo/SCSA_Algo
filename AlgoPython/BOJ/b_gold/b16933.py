import heapq
from collections import deque

n, m, limit = map(int, input().split())

grid = [list(map(int, input())) for i in range(n)]

sr, sc, er, ec = 0, 0, n - 1, m - 1

ans = -1
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
ans = int(1e9)


def bfs(sr, sc, er, ec):
    global ans
    visited = [[[int(1e9)] * (limit + 1) for i in range(m)] for i in range(n)]
    visited[sr][sc][limit] = 0
    q = deque([(0, sr, sc, limit)])
    while q:
        dist, r, c, bomb = q.popleft()
        if (r, c) == (er, ec):
            ans = min(ans, dist + 1)
            return
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if grid[nr][nc] == 1 and bomb and visited[nr][nc][bomb - 1] > dist + 1:
                if dist % 2 == 0:
                    visited[nr][nc][bomb - 1] = dist + 1
                    q.append((dist + 1, nr, nc, bomb - 1))
                else:
                    q.append((dist + 1, r, c, bomb))
            elif grid[nr][nc] == 0 and visited[nr][nc][bomb] > dist + 1:
                visited[nr][nc][bomb] = dist + 1
                q.append((dist + 1, nr, nc, bomb))


bfs(sr, sc, er, ec)
if ans == int(1e9):
    print(-1)
else:
    print(ans)
