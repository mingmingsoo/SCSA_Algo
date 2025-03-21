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
    global ans

    if idx == n * m:
        print(numbers)
        return
    r = idx // m
    c = idx % m
    if visited[r][c]:
        dfs(idx+1,numbers)
        return
    # 하나만 고를램
    visited[r][c] = True
    dfs(idx + 1, numbers + [grid[r][c]])
    visited[r][c] = False

    # 가로로 고를램
    cur = grid[r][c]
    for j in range(c + 1, m):
        if not visited[r][j]:
            visited[r][j] = True
            cur += grid[r][j]
            visited[r][c] = True
            dfs(idx + 1, numbers + [cur])
        else:
            break
    for j in range(c, m):
        if visited[r][j]:
            visited[r][j]= False
        else:
            break


    # 세로로 고를램
    cur = grid[r][c]
    for i in range(r+1, n):
        if not visited[i][c]:
            visited[i][c] = True
            cur += grid[i][c]
            visited[i][c] = True
            dfs(idx + 1, numbers + [cur])
        else:
            break
    for i in range(r, n):
        if visited[i][c]:
            visited[i][c]= False
        else:
            break

dfs(0, [])
print(ans)