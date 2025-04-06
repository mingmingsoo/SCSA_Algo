import heapq

n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]
num = 1

for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            grid[i][j] = "."
            sr, sc = i, j
        elif grid[i][j] == "C":
            grid[i][j] = num
            num += 1

ans = -1
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

visited = [[0] * n for i in range(n)]


def bfs():
    global ans
    visited = [[[[int(1e9)] * 4 for i in range(4)] for i in range(m)] for i in range(n)]
    visited[sr][sc][0][0] = 0
    visited[sr][sc][1][0] = 0
    visited[sr][sc][2][0] = 0
    visited[sr][sc][3][0] = 0
    q = []
    heapq.heappush(q, (0, sr, sc, -1, 0))
    first = False
    while q:
        cnt, r, c, before_d, have = heapq.heappop(q)
        if not first and visited[r][c][before_d][have] > cnt:
            first = True
            continue

        if have == 3:
            ans = cnt
            return
        for k in range(4):
            if k == before_d:
                continue
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] == "#":
                continue
            if grid[nr][nc] in (1, 2) and have != grid[nr][nc]:
                if visited[nr][nc][k][have + grid[nr][nc]] > cnt + 1:
                    visited[nr][nc][k][have + grid[nr][nc]] = cnt + 1
                    heapq.heappush(q, (cnt + 1, nr, nc, k, have + grid[nr][nc]))
            else:
                if visited[nr][nc][k][have] > cnt + 1:
                    visited[nr][nc][k][have] = cnt + 1
                    heapq.heappush(q, (cnt + 1, nr, nc, k, have))


bfs()
print(ans)
