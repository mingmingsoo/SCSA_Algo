n = int(input())
g = int(input())
grid_origin = [list(map(int, input().split())) for i in range(n)]
guns = list(map(int, input().split()))
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
ans = 0
# 아.................... 모두 동일한 위치가 아니구나......
sel = [0] * g


def duple_perm(idx):
    global ans
    if idx == g:
        score = 0
        now_grid = [_[:] for _ in grid_origin]
        init_grid = [_[:] for _ in grid_origin]
        for _ in range(g):
            i = sel[_]
            gun = guns[_]
            for j in range(n):
                if 0 < now_grid[i][j] < 10:
                    # 그냥 사격
                    now_grid[i][j] = max(0, now_grid[i][j] - gun)
                    if now_grid[i][j] == 0:  # 점수획득
                        score += init_grid[i][j]
                        if init_grid[i][j] >= 4:
                            for k in range(4):
                                nr = i + row[k]
                                nc = j + col[k]
                                if 0 <= nr < n and 0 <= nc < n and now_grid[nr][nc] == 0:
                                    now_grid[nr][nc] = init_grid[i][j] // 4
                                    init_grid[nr][nc] = init_grid[i][j] // 4
                        init_grid[i][j] = 0
                    break
                elif now_grid[i][j] >= 10:
                    score += now_grid[i][j]
                    now_grid[i][j] = 0
                    break

        ans = max(ans, score)
        return

    for i in range(n):
        sel[idx] = i
        duple_perm(idx + 1)


duple_perm(0)
print(ans)
