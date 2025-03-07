'''
각 좌표마다 무슨 색종이로 덮을건지 dfs
색종이는 5장씩 가지고 있다.
불가능하면 -1 출력
'''

grid = [list(map(int, input().split())) for i in range(10)]
ans = 26


def isOk(r, c, size):
    if r + size >= 11 or c + size >= 11:
        return False
    for i in range(r, r + size):
        for j in range(c, c + size):
            if grid[i][j] == 0:
                return False
    return True


def isfill(r, c, size):
    for i in range(r, r + size):
        for j in range(c, c + size):
            grid[i][j] = 0


def isrestore(r, c, size):
    for i in range(r, r + size):
        for j in range(c, c + size):
            grid[i][j] = 1


def is_all_fill():
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 1:
                return False
    return True


def btk(idx, A, B, C, D, E):
    global ans
    if idx == 100:
        if is_all_fill():
            ans = min(ans, 25 - (A + B + C + D + E))
        return
    r = idx // 10
    c = idx % 10

    if grid[r][c] == 0:
        btk(idx + 1, A, B, C, D, E)
        return

    if E > 0 and isOk(r, c, 5):
        isfill(r, c, 5)
        btk(idx + 1, A, B, C, D, E - 1)
        isrestore(r, c, 5)
    if D > 0 and isOk(r, c, 4):
        isfill(r, c, 4)
        btk(idx + 1, A, B, C, D - 1, E)
        isrestore(r, c, 4)
    if C > 0 and isOk(r, c, 3):
        isfill(r, c, 3)
        btk(idx + 1, A, B, C - 1, D, E)
        isrestore(r, c, 3)
    if B > 0 and isOk(r, c, 2):  # 두장가능?
        isfill(r, c, 2)
        btk(idx + 1, A, B - 1, C, D, E)
        isrestore(r, c, 2)
    if A > 0:  # 한장가능?
        grid[r][c] = 0
        btk(idx + 1, A - 1, B, C, D, E)
        grid[r][c] = 1


btk(0, 5, 5, 5, 5, 5)  # 위치, 색종이 남은 갯수
if ans == 26:
    print(-1)
else:
    print(ans)
