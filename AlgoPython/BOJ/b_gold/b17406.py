'''
b17406

문제 설명
    시작점, 끝점, size로 배열을 회전하라
    한칸씩 시계방향으로 회전.
    아 근데 순열이 섞인...

'''

n, m, order_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
grid_origin = [_[:] for _ in grid]
size_list = []
for i in range(order_num):
    r, c, s = map(int, input().split())
    size_list.append((r, c, s))

row = [0, 1, 0, -1]
col = [1, 0, -1, 0]


def rotation(r1, r2, c1, c2):
    d = 0
    grid_copy = [[0] * m for i in range(n)]
    or1, or2, oc1, oc2 = r1, r2, c1, c2

    while True:
        r = r1
        c = c1  # 시작점
        if (r == or1 + (or2 - or1) // 2 and c == oc1 + (oc2 - oc1) // 2):
            grid_copy[r][c] = grid[r][c]
            break

        while True:

            if not (r1 <= r + row[d] <= r2 and c1 <= c + col[d] <= c2) or grid_copy[r + row[d]][c + col[d]] != 0:
                d = (d + 1) % 4
            nr = r + row[d]
            nc = c + col[d]

            grid_copy[nr][nc] = grid[r][c]
            r = nr
            c = nc

            if (r == r1 and c == c1):
                break

        r1 += 1
        c1 += 1
        r2 -= 1
        c2 -= 1

    for i in range(or1, or2 + 1):
        for j in range(oc1, oc2 + 1):
            grid[i][j] = grid_copy[i][j]


mini = 100 * 50 + 1
sel = [0] * order_num

visited = [False] * order_num


def perm(idx):
    global mini, grid
    if (idx == order_num):

        for s in sel:
            r, c, s = size_list[s]

            rotation(r - s - 1, r + s - 1, c - s - 1, c + s - 1)

        for _ in grid:
            mini = min(mini, sum(_))
        grid = [_[:] for _ in grid_origin]
        return

    for i in range(order_num):
        if not visited[i]:
            visited[i] = True
            sel[idx] = i
            perm(idx + 1)
            visited[i] = False


perm(0)
print(mini)
