T = int(input())
for tc in range(T):

    n = int(input())
    grid = [list(map(int, input().split())) for i in range(n)]

    minH = 11
    maxH = -1
    total = 0

    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]


    def mountain(r, c):
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if (grid[nr][nc] >= grid[r][c]):
                return False
        return True


    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if (mountain(i, j)):
                total += 1
                if (grid[i][j] > maxH):
                    maxH = grid[i][j]
                if (grid[i][j] < minH):
                    minH = grid[i][j]

    if (total < 2):
        print(f"#{tc+1} -1")
    else:
        print(f"#{tc + 1} {maxH - minH}")
