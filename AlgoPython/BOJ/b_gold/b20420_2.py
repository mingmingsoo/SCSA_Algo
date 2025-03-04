'''
갈수 있는 방향을 제외하고
추가
'''
import sys
from collections import deque

input = sys.stdin.readline

n, m, card = map(int, input().split())
grid = [list(input().rstrip()) for i in range(n)]
for i in range(n):
    for j in range(m):
        grid[i][j] = "URDL".index(grid[i][j])
ans = "No"
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


def bfs(sr, sc, er, ec):
    global ans
    q = deque()
    q.append((sr, sc, card, card))
    visited = [[[[False] * (card + 1) for c in range(card + 1)] for mm in range(m)] for nn in
               range(n)]
    visited[sr][sc][card][card] = True
    while q:
        r, c, left, right = q.popleft()
        if r == er and c == ec:
            ans = "Yes"
            return

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            right_count = (4 + grid[r][c] - k) % 4
            if right - right_count >= 0 and not visited[nr][nc][left][right - right_count]:
                q.append((nr, nc, left, right - right_count))
                visited[nr][nc][left][right - right_count] = True

            left_count = (4 + k - grid[r][c]) % 4
            if left - left_count >= 0 and not visited[nr][nc][left - left_count][right]:
                q.append((nr, nc, left - left_count, right))
                visited[nr][nc][left - left_count][right] = True


bfs(0, 0, n - 1, m - 1)

print(ans)
