p, on = map(int, input().split())
n = 2 ** (p)

grid = [list(map(int, input().split())) for i in range(n)]

order_lst = [list(map(int, input().split())) for i in range(on)]


def one():
    m = 2 ** l
    for sr in range(0, n, m):
        for sc in range(0, n, m):
            # sr, sc: 시작점
            small_grid = [_[sc:sc + m] for _ in grid[sr:sr + m]]
            small_grid.reverse()
            for i in range(m):
                for j in range(m):
                    grid[i + sr][j + sc] = small_grid[i][j]


def two():
    m = 2 ** l
    for sr in range(0, n, m):
        for sc in range(0, n, m):
            # sr, sc: 시작점
            small_grid = [_[sc:sc + m] for _ in grid[sr:sr + m]]
            # 전치
            small_grid = list(map(list, zip(*small_grid)))
            small_grid.reverse()
            small_grid = list(map(list, zip(*small_grid)))
            for i in range(m):
                for j in range(m):
                    grid[i + sr][j + sc] = small_grid[i][j]


def rotation_right(small_grid):
    ro = [[0] * len(small_grid) for i in range(len(small_grid))]
    for i in range(len(small_grid)):
        for j in range(len(small_grid)):
            ro[i][j] = small_grid[len(small_grid) - j - 1][i]
    return ro


def rotation_left(small_grid):
    ro = [[0] * len(small_grid) for i in range(len(small_grid))]
    for i in range(len(small_grid)):
        for j in range(len(small_grid)):
            ro[i][j] = small_grid[j][len(small_grid) - i - 1]

    return ro


def three():
    m = 2 ** l
    for sr in range(0, n, m):
        for sc in range(0, n, m):
            # sr, sc: 시작점
            small_grid = [_[sc:sc + m] for _ in grid[sr:sr + m]]
            small_grid = rotation_right(small_grid)
            for i in range(m):
                for j in range(m):
                    grid[i + sr][j + sc] = small_grid[i][j]


def four():
    m = 2 ** l
    for sr in range(0, n, m):
        for sc in range(0, n, m):
            # sr, sc: 시작점
            small_grid = [_[sc:sc + m] for _ in grid[sr:sr + m]]
            small_grid = rotation_left(small_grid)
            for i in range(m):
                for j in range(m):
                    grid[i + sr][j + sc] = small_grid[i][j]


def five():  # 크게 만들어서 reverse
    global grid
    m = 2 ** l
    big = []
    for sr in range(0, n, m):
        tmp = []
        for sc in range(0, n, m):
            # sr, sc: 시작점
            small_grid = [_[sc:sc + m] for _ in grid[sr:sr + m]]
            tmp.append(small_grid)
        big.append(tmp)

    big.reverse()
    sr = 0
    for small_x in big:
        sc = 0
        for small_y in small_x:
            for i in range(m):
                for j in range(m):
                    grid[i + sr][j + sc] = small_y[i][j]

            sc += m
        sr += m



def six():
    m = 2 ** l
    big = []
    for sr in range(0, n, m):
        tmp = []
        for sc in range(0, n, m):
            # sr, sc: 시작점
            small_grid = [_[sc:sc + m] for _ in grid[sr:sr + m]]
            tmp.append(small_grid)
        big.append(tmp)

    big = list(map(list, zip(*big)))
    big.reverse()
    big = list(map(list, zip(*big)))
    sr = 0
    for small_x in big:
        sc = 0
        for small_y in small_x:
            for i in range(m):
                for j in range(m):
                    grid[i + sr][j + sc] = small_y[i][j]

            sc += m
        sr += m
def seven():
    m = 2 ** l
    big = []
    for sr in range(0, n, m):
        tmp = []
        for sc in range(0, n, m):
            # sr, sc: 시작점
            small_grid = [_[sc:sc + m] for _ in grid[sr:sr + m]]
            tmp.append(small_grid)
        big.append(tmp)

    big = rotation_right(big)
    sr = 0
    for small_x in big:
        sc = 0
        for small_y in small_x:
            for i in range(m):
                for j in range(m):
                    grid[i + sr][j + sc] = small_y[i][j]

            sc += m
        sr += m


def eight():
    m = 2 ** l
    big = []
    for sr in range(0, n, m):
        tmp = []
        for sc in range(0, n, m):
            # sr, sc: 시작점
            small_grid = [_[sc:sc + m] for _ in grid[sr:sr + m]]
            tmp.append(small_grid)
        big.append(tmp)

    big = rotation_left(big)
    sr = 0
    for small_x in big:
        sc = 0
        for small_y in small_x:
            for i in range(m):
                for j in range(m):
                    grid[i + sr][j + sc] = small_y[i][j]

            sc += m
        sr += m


func_dict = {1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight}
for order, l in order_lst:
    func_dict[order]()
for _ in grid:
    print(*_)
