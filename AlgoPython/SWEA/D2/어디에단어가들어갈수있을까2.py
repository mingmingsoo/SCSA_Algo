T = int(input())
for tc in range(T):
    n, k = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(n)]
    ans = 0

    row = [1, 0]
    col = [0, 1]


    def check(r, c):
        sum = 0
        for d in range(2):
            isOk = True
            for l in range(1, k):
                nr = r + row[d] * l
                nc = c + col[d] * l
                if (not (0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1)):
                    isOk = False
                    break

            if (0 <= r + row[d] * (k) < n and 0 <= c + col[d] * (k) < n and grid[r + row[d] * (k)][
                c + col[d] * (k)] == 1):
                isOk = False
            if (0 <= r + row[d] * (-1) < n and 0 <= c + col[d] * (-1) < n and grid[r + row[d] * (-1)][
                c + col[d] * (-1)] == 1):
                isOk = False

            if (isOk):
                # print(r, c, d, sum)
                sum += 1
        return sum


    for i in range(n):
        for j in range(n):
            if (grid[i][j] == 1):
                ans += check(i, j)
    print(f"#{tc+1} {ans}")