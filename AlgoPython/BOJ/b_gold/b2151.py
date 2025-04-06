'''
! 에서 방향전환
'''
import heapq
from collections import deque

n = int(input())
grid = [list(input()) for i in range(n)]

sr, sc, er, ec = -1, -1, -1, -1

for i in range(n):
    for j in range(n):
        if grid[i][j] == "#" and sr == sc == -1:
            sr, sc = i, j
            grid[i][j] = "."
        if grid[i][j] == "#" and (sr, sc) != (-1, -1):
            er, ec = i, j
            grid[i][j] = "."
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def bfs():
    visited = [[[int(1e9)] * 4 for i in range(n)] for i in range(n)]
    q = []

    heapq.heappush(q, (0, sr, sc, 0))
    heapq.heappush(q, (0, sr, sc, 1))
    heapq.heappush(q, (0, sr, sc, 2))
    heapq.heappush(q, (0, sr, sc, 3))

    visited[sr][sc][0] = 0
    visited[sr][sc][1] = 0
    visited[sr][sc][2] = 0
    visited[sr][sc][3] = 0

    while q:
        cnt, r, c, bk = heapq.heappop(q)
        if visited[r][c][bk] > cnt:
            continue
        if (r, c) == (er, ec):
            print(cnt)
            return

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or grid[nr][nc] == "*":
                continue
            if grid[r][c] == "." and (grid[nr][nc] == "." or grid[nr][nc] == "!") and k == bk:
                if visited[nr][nc][k] > cnt:
                    heapq.heappush(q, (cnt, nr, nc, k))
                    visited[nr][nc][k] = cnt
            elif grid[r][c] == "!" and (grid[nr][nc] == "." or grid[nr][nc] == "!") and k != bk:
                if visited[nr][nc][k] > cnt + 1:
                    heapq.heappush(q, (cnt + 1, nr, nc, k))
                    visited[nr][nc][k] = cnt + 1
            elif grid[r][c] == "!" and (grid[nr][nc] == "." or grid[nr][nc] == "!") and k == bk:
                if visited[nr][nc][k] > cnt:
                    heapq.heappush(q, (cnt, nr, nc, k))
                    visited[nr][nc][k] = cnt


bfs()
