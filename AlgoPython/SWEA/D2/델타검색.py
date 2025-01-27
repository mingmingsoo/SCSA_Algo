T = int(input())
for tc in range(T):
    n = int(input())

    grid = [list(map(int, input().split())) for i in range(5)]
    # print(grid)

    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]

    total = 0


    def calAbsSum(r, c):
        sum = 0
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if (nr >= 0 and nr < n and nc >= 0 and nc < n):
                sum += abs(grid[nr][nc] - grid[r][c])
        return sum


    for i in range(n):
        for j in range(n):
            total += calAbsSum(i, j)
    print(f"#{tc+1} {total}")