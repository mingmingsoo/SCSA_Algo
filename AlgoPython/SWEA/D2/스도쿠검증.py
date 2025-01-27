T =int(input())
for tc in range(T):
    grid = [list(map(int, input().split())) for i in range(9)]

    n = 9
    # 가로체크
    isOk = True
    cnt = 0
    while cnt < 1:
        for i in range(n):
            dupleCheck = set()
            for j in range(n):
                if (grid[i][j] not in dupleCheck):
                    dupleCheck.add(grid[i][j])
                else:
                    isOk = False
                    break
            if (isOk == False):
                break
        if (isOk == False):
            break

        for j in range(n):
            dupleCheck = set()
            for i in range(n):
                if (grid[i][j] not in dupleCheck):
                    dupleCheck.add(grid[i][j])
                else:
                    isOk = False
                    break
            if (isOk == False):
                break
        if (isOk == False):
            break

        for i in range(0, n, 3):
            for j in range(0, n, 3):
                dupleCheck = set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if (grid[r][c] not in dupleCheck):
                            dupleCheck.add(grid[r][c])
                        else:
                            isOk = False
                            break
                    if (isOk == False):
                        break
                if (isOk == False):
                    break
            if (isOk == False):
                break

        cnt += 1
    if (isOk):
        print(f"#{tc+1} 1")
    else:
        print(f"#{tc+1} 0")
