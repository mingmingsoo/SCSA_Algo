'''
낮에 올때랑 밤에올때랑 다른가 . 아 ㅇㅇ뭐야 안움직일 때 생각해야함
'''
from collections import deque

n, m, bomb = map(int, input().split())
grid = [list(input()) for i in range(n)]
visited = [[[[False] * 2 for i in range(bomb + 1)] for i in range(m)] for i in range(n)]

sr, sc, er, ec = 0, 0, m - 1, n - 1
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
q = deque([(sr, sc, 0, 0)])
ans = -1
while q:
    r, c, bomb, time = q.popleft()
    if (r, c) == (er, ec):
        ans = time
        break

    for k in range(4):
        nr = r + row[k]
        nc = c + col[k]
        if grid[nr][nc] == 0 and not visited[nr][nc][]
