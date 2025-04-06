# 1:55~14:33
# 미리 조합 만들어놓고 이미 만들어진 애들은 pop하기
# 좋은 문제 땡스투 완진

from collections import Counter

domino_origin = []
sel = [0] * 2
row = [1, 0]
col = [0, 1]


def combi(sidx, idx):
    if sidx == 2:
        domino_origin.append(sel[:])
        return
    if idx == 10:
        return

    sel[sidx] = idx
    combi(sidx + 1, idx + 1)
    combi(sidx, idx + 1)


def is_possible():
    # 스도쿠 검사
    for dr in grid:
        cnt = Counter(dr)
        for k, v in cnt.items():
            if k != 0 and v > 1:
                return False
    grid_T = list(map(list, zip(*grid)))
    for dr in grid_T:
        cnt = Counter(dr)
        for k, v in cnt.items():
            if k != 0 and v > 1:
                return False
    for sr in range(0, 9, 3):
        for sc in range(0, 9, 3):
            tmp = []
            for i in range(sr, sr + 3):
                for j in range(sc, sc + 3):
                    tmp.append(grid[i][j])
            cnt = Counter(tmp)
            for k, v in cnt.items():
                if k != 0 and v > 1:
                    return False
    return True


def btk(lo):
    global find, grid
    if find:
        return
    if lo == n * n:
        find = True
        for _ in grid:
            print("".join(map(str, _)))
        return
    r, c = lo // n, lo % n
    if grid[r][c]:
        btk(lo + 1)
        return

    for i in range(len(domino)):
        if visited[i]:
            continue
        num1, num2 = domino[i]
        for k in range(2):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or grid[nr][nc]:
                continue
            grid[r][c] = num1
            grid[nr][nc] = num2
            visited[i] = True
            if is_possible():
                btk(lo + 1)
                grid[r][c] = 0
                grid[nr][nc] = 0
                visited[i] = False
            else:
                grid[r][c] = 0
                grid[nr][nc] = 0
                visited[i] = False

            grid[r][c] = num2
            grid[nr][nc] = num1
            visited[i] = True
            if is_possible():
                btk(lo + 1)
                grid[r][c] = 0
                grid[nr][nc] = 0
                visited[i] = False
            else:
                grid[r][c] = 0
                grid[nr][nc] = 0
                visited[i] = False


combi(0, 1)
n = 9
tc = 1
while True:

    domino = domino_origin[:]
    grid = [[0] * n for i in range(n)]
    init_num = int(input())
    if init_num == 0:
        break
    for _ in range(init_num):
        num1, lo1, num2, lo2 = input().split()
        r1, c1 = ord(lo1[0]) - 65, int(lo1[1]) - 1
        r2, c2 = ord(lo2[0]) - 65, int(lo2[1]) - 1
        num1, num2 = int(num1), int(num2)
        grid[r1][c1] = num1
        grid[r2][c2] = num2
        if num1 > num2:
            num1, num2 = num2, num1
        for i in range(len(domino) - 1):
            if domino[i] == [num1, num2]:
                domino.pop(i)
                break
    tmp = list(input().split())
    for num, info in enumerate(tmp):
        r, c = ord(info[0]) - 65, int(info[1]) - 1
        grid[r][c] = num + 1

    find = False
    visited = [False] * len(domino)
    print("Puzzle", tc)
    btk(0)
    tc += 1
