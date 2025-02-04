T = int(input())
for tc in range(T):
    n = int(input())

    grid = [list(map(int, input())) for i in range(n)]
    sr, sc, er, ec = -1, -1, -1, -1
    for i in range(n):
        for j in range(n):
            if (grid[i][j] == 2):
                sr, sc = i, j
            elif (grid[i][j] == 3):
                er, ec = i, j


    def bfs(sr, sc, er, ec):
        q = [(sr, sc, 0)]
        visited = [[False] * n for i in range(n)]
        visited[sr][sc] = True

        row = [-1, 1, 0, 0]
        col = [0, 0, 1, -1]

        while q:
            r, c, cnt = q.pop(0)
            if (r == er and c == ec):
                print(f"#{tc+1} {cnt-1}")
                return
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if (0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] != 1):
                    q.append((nr, nc, cnt + 1))
                    visited[nr][nc] = True
        print(f"#{tc+1} 0")


    bfs(sr, sc, er, ec)