T = int(input())

for t in range(T):
    k = int(input())
    n = int(input())

    grid = [[0] * (n + 1) for i in range(k + 1)]

    for j in range(1, n + 1):
        grid[0][j] = j
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    print(grid[k][n])

