import heapq
T = int(input())
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
for tc in range(T):

    size = 90001
    n = int(input())
    sr, sc, er, ec = map(int, input().split())
    grid = [list(map(int, input())) for i in range(n)]
    d = [[size] * n for i in range(n)]
    start = grid[sr][sc]
    d[sr][sc] = start


    def bfs(start, sr, sc):
        q = [(start,sr, sc)]
        heapq.heapify(q)
        while q:
            dist,r,c = heapq.heappop(q)

            if (dist > d[r][c]):
                continue

            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if (not (0 <= nr < n and 0 <= nc < n)):
                    continue
                if (d[nr][nc] > d[r][c] + grid[nr][nc]):
                    d[nr][nc] = d[r][c] + grid[nr][nc]
                    heapq.heappush(q, (d[nr][nc],nr, nc))


    bfs(start,sr, sc)
    print(f"#{tc+1} {d[er][ec]}")