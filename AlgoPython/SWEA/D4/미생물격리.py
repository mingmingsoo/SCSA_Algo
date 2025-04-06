T = int(input())
for tc in range(T):
    '''
    3차원으로 안하고 2차원으로
    안돼 이러면 안돼 3차원으로 해야돼.
    '''

    n, time, player_num = map(int, input().split())
    grid = [[[] for i in range(n)] for i in range(n)]

    for p in range(player_num):
        r, c, power, d = map(int, input().split())
        grid[r][c].append((power, d - 1))

    row = [-1, 1, 0, 0]
    col = [0, 0, -1, 1]
    change_d = [1, 0, 3, 2]


    for t in range(time):
        new_grid = [[[] for i in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    power, d = grid[i][j][0]
                    nr = i + row[d]
                    nc = j + col[d]
                    if nr == 0 or nr == n - 1 or nc == 0 or nc == n - 1:
                        # 반띵
                        power //= 2
                        if power > 0:
                            d = change_d[d]
                            new_grid[nr][nc].append((power, d))
                    else:
                        new_grid[nr][nc].append((power, d))  # 일단 그냥 가.

        for i in range(n):
            for j in range(n):
                if new_grid[i][j]:
                    sm = 0
                    ele = 0
                    nd = 0
                    for power, d in new_grid[i][j]:
                        sm += power
                        if ele < power:
                            nd = d
                            ele = power
                    new_grid[i][j] = [(sm,nd)]

        grid = new_grid

    ans = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j]: ans += grid[i][j][0][0]
    print(f"#{tc + 1} {ans}")
