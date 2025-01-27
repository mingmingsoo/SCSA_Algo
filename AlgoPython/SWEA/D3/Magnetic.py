T = 10
for tc in range(T):
    size = int(input())
    grid = [list(map(int, input().split())) for i in range(size)]
    # for row in grid:
    #     print(*row)

    '''
    1이면 N - 바닥으로 감
    2이면 S - 위로감
    '''


    def magnetic():
        sum = 0
        for j in range(0, size):
            for i in range(0, size):
                if (grid[i][j] == 2 and i == 0):
                    grid[i][j] = 0
                    sum += 1
                elif (grid[i][j] == 2 and i != 0 and grid[i - 1][j] == 0):
                    grid[i][j] = 0
                    grid[i - 1][j] = 2
                    sum += 1
        for j in range(0, size):
            for i in range(size - 1, -1, -1):
                if (grid[i][j] == 1 and i == size - 1):
                    grid[i][j] = 0
                    sum += 1
                elif (grid[i][j] == 1 and i != size - 1 and grid[i + 1][j] == 0):
                    grid[i][j] = 0
                    grid[i + 1][j] = 1
                    sum += 1
        # print("----------")
        # for row in grid:
        #     print(*row)
        return sum


    while True:
        move = magnetic()
        if (move == 0):
            break


    def count():
        cnt = 0
        for j in range(0, size):
            for i in range(0, size - 1):
                if (grid[i][j] == 1 and grid[i + 1][j] == 2):
                    cnt += 1
        return cnt


    ans = count()
    print(f"#{tc+1} {ans}")