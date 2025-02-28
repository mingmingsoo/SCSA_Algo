'''
다익스트라 문제
'''

import heapq

m, n = map(int, input().split())
grid = [list(map(int, input())) for i in range(n)]

sr, sc, er, ec = 0, 0, n - 1, m - 1

d = [[10001] * m for i in range(n)]

d[0][0] = grid[0][0]


def dijk(sr, sc, er, ec):
    q = []
    heapq.heappush(q, (d[0][0], sr, sc))
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]
    while q:
        cost, r, c = heapq.heappop(q)
        if r == er and c == ec:
            break
        if cost > d[r][c]:
            continue

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m):
                continue

            if d[nr][nc] > cost + grid[nr][nc]:
                d[nr][nc] = cost + grid[nr][nc]
                heapq.heappush(q, (d[nr][nc], nr, nc))


dijk(sr, sc, er, ec)
print(d[n - 1][m - 1])
