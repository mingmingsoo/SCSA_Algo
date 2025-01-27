T = int(input())
n = 9

for tc in range(T):

    def checkCondition():

        for row in grid:
            if (len(set(row)) != n):
                return False

        for col in zip(*grid):
            if (len(set(col)) != n):
                return False

        for i in range(0, n, 3):
            for j in range(0, n, 3):
                # 시작점
                dupleSet = set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if grid[r][c] not in dupleSet:
                            dupleSet.add(grid[r][c])
                        else:
                            return False

        return True


    grid = [list(map(int, input().split())) for i in range(n)]

    if (checkCondition()):
        print(f"#{tc + 1} 1")
    else:
        print(f"#{tc + 1} 0")
