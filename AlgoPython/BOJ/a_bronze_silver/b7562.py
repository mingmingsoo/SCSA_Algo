T = int(input())
for tc in range(T):
    '''
    시작점, 목적지
    dr, dc 변형
    '''
    from collections import deque

    n = int(input())
    grid = [[0] * n for i in range(n)]

    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())


    def bfs(sr, sc, er, ec):
        q = deque([(sr, sc, 0)])
        v = [[0] * n for i in range(n)]
        v[sr][sc] = True

        row = [2, 1, -1, -2, -2, -1, 1, 2]
        col = [1, 2, 2, 1, -1, -2, -2, -1]
        while q:
            r, c, cnt = q.popleft()

            if (r == er and c == ec):
                print(cnt)
                return
            for k in range(8):
                nr = r + row[k]
                nc = c + col[k]
                if (0 <= nr < n and 0 <= nc < n and not v[nr][nc]):
                    q.append((nr, nc, cnt + 1))
                    v[nr][nc] = True


    bfs(sr, sc, er, ec)
