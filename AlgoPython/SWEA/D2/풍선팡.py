T = int(input())
for tc in range(T):
    n, m = map(int, input().split())

    grid = [list(map(int, input().split())) for i in range(n)]
    # print(grid)

    ans = 0
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]


    def calFlower(r, c, len):
        sum = 0

        for k in range(4):
            for l in range(1, len + 1):
                nr = r + row[k] * l
                nc = c + col[k] * l
                if (0 <= nr < n and 0 <= nc < m):
                    sum += grid[nr][nc]
        return sum


    for i in range(n):
        for j in range(m):
            ans = max(calFlower(i, j, grid[i][j]) + grid[i][j], ans)
    print(f"#{tc+1} {ans}")