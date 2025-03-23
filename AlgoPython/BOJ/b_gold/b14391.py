'''
생각을 해보자
색종이 붙이기 처럼
죱죱죱 죱죱죱?
'''

n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]

ans = 0
visited = [[False] * m for i in range(n)]


def dfs(idx, numbers):
    global ans, visited

    if idx == n * m:
        sm = 0
        for num in numbers:
            sm += int(num)
        ans = max(ans, sm)
        return

    r = idx // m
    c = idx % m
    if visited[r][c]:
        dfs(idx + 1, numbers)
        return

    # 가로로 고를램
    visited_copy = [_[:] for _ in visited]
    cur = ""
    for j in range(c, m):
        if not visited[r][j]:
            visited[r][j] = True
            cur += grid[r][j]
            dfs(idx + 1, numbers + [cur])
        else:
            break
    visited = [_[:] for _ in visited_copy]

    # 세로로 고를램
    cur = ""
    for i in range(r, n):
        if not visited[i][c]:
            visited[i][c] = True
            cur += grid[i][c]
            dfs(idx + 1, numbers + [cur])
        else:
            break
    visited = [_[:] for _ in visited_copy]


dfs(0, [])
print(ans)
