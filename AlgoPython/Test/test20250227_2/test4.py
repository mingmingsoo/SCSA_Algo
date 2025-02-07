T = int(input())
for tc in range(T):
    '''
    bfs로 정점 갯수를 확인하고
    1인데 vistied False 인 애들 갯수를 센다
    '''
    from collections import deque

    n, m = map(int, input().split())
    # m = n
    grid = [list(map(int, input().split())) for i in range(n)]
    sr, sc = map(lambda x: int(x) - 1, input().split())

    visited = [[False] * m for i in range(n)]
    sick = 1


    def bfs(sr, sc):

        global sick
        q = deque([(sr, sc)])
        visited[sr][sc] = True

        row = [-1, 1, 0, 0]
        col = [0, 0, 1, -1]

        while q:
            r, c = q.popleft()

            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if (not (0 <= nr < n and 0 <= nc < m)):
                    continue
                if (not visited[nr][nc] and grid[nr][nc] == 1):
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    sick += 1


    bfs(sr, sc)
    not_sick = 0
    for i in range(n):
        for j in range(m):
            if (grid[i][j] == 1 and not visited[i][j]):
                not_sick += 1
    print(f"#{tc+1} {sick} {not_sick}")
