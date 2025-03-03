'''
어렵당.
모든 경우의 수 완탐
'''

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
visited = [[False] * m for i in range(n)]
ans = 0
mx = 0
for row in grid:
    mx = max(max(row), mx)
mx_num = 0
# 최대갯수 -> 근데 이거 없어도 맞는다..;ㅋㅋㅋㅋㅋ
if (n, m) in {(2, 2)}:
    mx_num = 1
elif (n, m) in {(2, 3), (3, 2)}:
    mx_num = 2
elif (n, m) in {(2, 4), (4, 2)}:
    mx_num = 2
elif (n, m) in {(2, 5), (5, 2)}:
    mx_num = 3
elif (n, m) in {(3, 3)}:
    mx_num = 2
elif (n, m) in {(3, 4), (4, 3)}:
    mx_num = 4
elif (n, m) in {(3, 5), (5, 3)}:
    mx_num = 4
elif (n, m) in {(4, 5), (5, 4)}:
    mx_num = 6
elif (n, m) in {(5, 5)}:
    mx_num = 8


def dfs(lo, sm, idx):
    global ans

    if sm + (mx_num - idx) * (mx * 4) <= ans:
        return # 이거 없어도 시간초과 안남
    if lo == n * m:
        ans = max(ans, sm)
        return

    r = lo // m
    c = lo % m
    if visited[r][c]:
        dfs(lo + 1, sm, idx)
        return
    # print(r, c, sm, idx)
    # 4가지 탐색
    # ㄱ
    if r + 1 < n and c + 1 < m:
        if not visited[r][c] and not visited[r][c + 1] and not visited[r + 1][c + 1]:
            visited[r][c] = True
            visited[r][c + 1] = True
            visited[r + 1][c + 1] = True
            dfs(lo+1, sm + grid[r][c] + grid[r][c + 1] * 2 + grid[r + 1][c + 1], idx + 1)
            visited[r][c] = False
            visited[r][c + 1] = False
            visited[r + 1][c + 1] = False

        # ㄴ
        if not visited[r][c] and not visited[r + 1][c] and not visited[r + 1][c + 1]:
            visited[r][c] = True
            visited[r + 1][c] = True
            visited[r + 1][c + 1] = True
            dfs(lo+1, sm + grid[r][c] + grid[r + 1][c] * 2 + grid[r + 1][c + 1], idx + 1)
            visited[r][c] = False
            visited[r + 1][c] = False
            visited[r + 1][c + 1] = False

    if r - 1 >= 0 and c + 1 < m:
        if not visited[r][c] and not visited[r - 1][c] and not visited[r - 1][c + 1]:
            # ㄱ 반대
            visited[r][c] = True
            visited[r - 1][c] = True
            visited[r - 1][c + 1] = True
            dfs(lo+1, sm + grid[r][c] + grid[r - 1][c] * 2 + grid[r - 1][c + 1], idx + 1)
            visited[r][c] = False
            visited[r - 1][c] = False
            visited[r - 1][c + 1] = False

        # ㄴ 반대
        if not visited[r][c] and not visited[r][c + 1] and not visited[r - 1][c + 1]:
            visited[r][c] = True
            visited[r][c + 1] = True
            visited[r - 1][c + 1] = True
            dfs(lo+1, sm + grid[r][c] + grid[r][c + 1] * 2 + grid[r - 1][c + 1], idx + 1)
            visited[r][c] = False
            visited[r][c + 1] = False
            visited[r - 1][c + 1] = False
    # 선택 안함
    dfs(lo + 1, sm, idx)  # idx 선택한 갯수


dfs(0, 0, 0)  # 흠냐링
print(ans)
