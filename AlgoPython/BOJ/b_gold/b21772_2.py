'''
dfs로 풀어보기
'''
n, m, time = map(int, input().split())
grid = [list(input()) for i in range(n)]
sr, sc = -1, -1

def find_dog():
    global sr, sc, total_potato
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "G":
                grid[i][j] = "."
                sr, sc = i, j
                return

find_dog()
ans = 0
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def dfs(r, c, eat, t):
    global ans
    if ((time - t)+ eat <= ans): # 남은 횟수만큼 다 고구마 먹어도 ans 안되면 return
        return
    if t >= time:
        ans = max(ans, eat)
        return

    for k in range(4):
        nr = r + row[k]
        nc = c + col[k]
        if not (0 <= nr < n and 0 <= nc < m):
            continue
        if grid[nr][nc] == "#":
            continue
        elif grid[nr][nc] == "S":
            grid[nr][nc] = "."
            dfs(nr, nc, eat + 1, t + 1)
            grid[nr][nc] = "S"
        else:
            dfs(nr, nc, eat, t + 1)


dfs(sr, sc, 0, 0)  # 위치, 고구마, 시간
print(ans)
