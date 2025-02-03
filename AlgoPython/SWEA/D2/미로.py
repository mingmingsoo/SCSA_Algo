T = int(input())
for tc in range(T):
    '''
    2에서 출발해서 0인통로를 따라 3에 도착할 수 있는지
    도착 가능 1 불가능 0
    '''
    n = int(input())
    grid = [[0] * n for i in range(n)]
    sr, sc, er, ec = -1, -1, -1, -1

    for i in range(n):
        tmp = list(map(int, input()))
        for j in range(n):
            grid[i][j] = tmp[j]
            if (grid[i][j] == 2):
                sr, sc = i, j
            elif (grid[i][j] == 3):
                er, ec = i, j

    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]

    ans = 0

    visited = [[0] * n for i in range(n)]


    def dfs(r, c):
        global ans
        if (r == er and c == ec):
            ans = 1
            return
        visited[r][c] = 1

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if (0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0 and grid[nr][nc] != 1):
                dfs(nr, nc)


    dfs(sr, sc)
    print(f"#{tc+1} {ans}")
