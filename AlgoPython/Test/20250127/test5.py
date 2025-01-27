T = int(input())
for tc in range(T):
    n, m = map(int, input().split())

    grid = [list(input()) for i in range(n)]
    ans = 200


    def cal(start, end, color):
        sum = 0
        for i in range(start, end):
            for j in range(m):
                if (grid[i][j] != color):
                    sum += 1
        return sum


    for i in range(0, 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # print(i, j, k)
                white = cal(i, j, 'W')
                blue = cal(j, k, 'B')
                red = cal(k, n, 'R')
                ans = min(white + blue + red, ans)
    print(f"#{tc+1} {ans}")
