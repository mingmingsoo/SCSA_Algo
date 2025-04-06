'''
아니 다른 기물이 없는데요
아 왕한테 한번에 도달인거임?
'''
from collections import deque

n, m = 10, 9
row = [-3, -3, 3, 3, -2, 2, -2, 2]
col = [-2, 2, -2, 2, -3, -3, 3, 3]

dir_dict = {0: [(-1, -2), (0, -1)],
            1: [(-1, -2), (0, 1)],
            2: [(1, 2), (0, -1)],
            3: [(1, 2), (0, 1)],
            4: [(0, -1), (-1, -2)],
            5: [(0, 1), (-1, -2)],
            6: [(0, -1), (1, 2)],
            7: [(0, 1), (1, 2)],
            }

grid = [[0] * m for i in range(n)]
sr, sc = map(int, input().split())
er, ec = map(int, input().split())

ans = -1
visited = [[False] * m for i in range(n)]
visited[sr][sc] = True


def bfs():
    global ans
    q = deque([(sr, sc, 0)])
    while q:
        r, c, cnt = q.popleft()
        if (r, c) == (er, ec):
            ans = cnt
            return
        for k in range(8):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc]:
                continue

            nr1 = r + dir_dict[k][0][0]
            nc1 = c + dir_dict[k][1][0]
            nr2 = r + dir_dict[k][0][1]
            nc2 = c + dir_dict[k][1][1]
            if (nr1, nc1) == (er, ec) or (nr2, nc2) == (er, ec):
                continue
            visited[nr][nc] = True
            q.append((nr, nc, cnt + 1))


bfs()
print(ans)
