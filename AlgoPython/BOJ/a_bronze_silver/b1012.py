import sys
sys.setrecursionlimit(10**5)
T = int(input())
for tc in range(T):
    '''
    군집? 구하기
    r,c 가 반대네
    '''
    m, n, k = map(int, input().split())
    grid = [[0] * m for i in range(n)]

    for i in range(k):
        c, r = map(int, input().split())
        grid[r][c] = 1

    visited = [[0] * m for i in range(n)]

    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]


    def dfs(r, c):
        visited[r][c] = 1
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if (0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0 and grid[nr][nc] == 1):
                dfs(nr, nc)

    ans = 0
    for i in range(n):
        for j in range(m): # n으로 해서 헤맸음
            if (grid[i][j] == 1 and visited[i][j] == 0):
                ans += 1
                dfs(i, j)
    print(ans)