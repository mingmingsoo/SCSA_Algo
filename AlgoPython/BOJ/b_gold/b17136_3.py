n = 10
grid = [list(map(int, input().split())) for i in range(n)]

ans = 5 * 5 + 1


def all_one(r, c, size):
    if r + size > 10 or c + size > 10:
        return False
    for i in range(r, r + size):
        for j in range(c, c + size):
            if grid[i][j] == 0:
                return False
    return True


def fill_one(r, c, size):
    for i in range(r, r + size):
        for j in range(c, c + size):
            grid[i][j] = 1


def fill_zero(r, c, size):
    for i in range(r, r + size):
        for j in range(c, c + size):
            grid[i][j] = 0


def btk(lo, cnt):
    global ans
    if lo == n * n:
        ans = min(ans, cnt)
        return
    rr = lo // 10
    cc = lo % 10
    if grid[rr][cc] == 0:
        btk(lo + 1, cnt)
        return

    for i in range(5):
        if paper[i] > 0:
            if all_one(rr, cc, i + 1):
                fill_zero(rr, cc, i + 1)
                paper[i] -= 1
                btk(lo + i + 1, cnt + 1)
                fill_one(rr, cc, i + 1)
                paper[i] += 1


paper = [5, 5, 5, 5, 5]
btk(0, 0)  # 색종이 1,2,3,4,5, 몇개썼는지
if ans == 26:
    print(-1)
else:
    print(ans)
