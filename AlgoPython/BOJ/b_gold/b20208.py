'''
1차원 배열로 관리
'''

n, init, plus = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(n)]
sr, sc = -1, -1
mint = 0
mint_list = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            sr, sc = i, j
        elif grid[i][j] == 2:
            mint_list.append((i, j))
            mint += 1
visited = [False] * (mint)
ans = 0

find = False
def dfs(r, c, idx, hp, eat):
    global ans, find
    if find:
        return
    if abs(r - sr) + abs(c - sc) <= hp:
        ans = max(ans, eat)
        if eat == mint:
            find = True
            return

    for i in range(mint):
        if not visited[i]:
            nr, nc = mint_list[i]
            if abs(nr - r) + abs(nc - c) <= hp:
                visited[i] = True
                dfs(nr, nc, idx + 1, hp - abs(nr - r) - abs(nc - c) + plus, eat + 1)
                visited[i] = False


dfs(sr, sc, 0, init, 0)
print(ans)
