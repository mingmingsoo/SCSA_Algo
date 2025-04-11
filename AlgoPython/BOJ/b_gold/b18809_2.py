from collections import deque


def perm(idx):
    if idx == gn + rn:
        color_set.add(tuple(color_sel))
        return
    for i in range(gn + rn):
        if not visited[i]:
            visited[i] = True
            color_sel[idx] = color_arr[i]
            perm(idx + 1)
            visited[i] = False


def combi(sidx, idx):
    global grid, ans

    if sidx == gn + rn:
        # 여기서 bfs
        grid_origin = [_[:] for _ in grid]
        for color_order in color_set:
            q = deque()
            flower = 0
            time_grid = [[0] * m for i in range(n)]
            for idx, color in enumerate(color_order):
                r, c = sel[idx]
                grid[r][c] = color
                time_grid[r][c] = 1
                q.append((r, c, color, 2))

            while q:
                r, c, color, time = q.popleft()
                if grid[r][c] == "F":
                    continue
                for k in range(4):
                    nr = r + row[k]
                    nc = c + col[k]
                    if not (0 <= nr < n and 0 <= nc < m):
                        continue
                    if grid[nr][nc] in (1, 2):
                        grid[nr][nc] = color
                        time_grid[nr][nc] = time
                        q.append((nr, nc, grid[nr][nc], time + 1))
                    elif grid[nr][nc] in ("G", "R") and grid[nr][nc] != color and time_grid[nr][nc] == time:
                        grid[nr][nc] = "F"
                        flower += 1

            ans = max(ans, flower)
            grid = [_[:] for _ in grid_origin]
        return

    if idx == len(arr):
        return
    sel[sidx] = arr[idx]
    combi(sidx + 1, idx + 1)
    combi(sidx, idx + 1)


n, m, gn, rn = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

arr = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            arr.append((i, j))

color_arr = ["G"] * gn + ["R"] * rn

color_set = set()
color_sel = [0] * (gn + rn)

visited = [False] * (gn + rn)
perm(0)

sel = [0] * (gn + rn)  # 위치 sel
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

ans = 0

combi(0, 0)
print(ans)
