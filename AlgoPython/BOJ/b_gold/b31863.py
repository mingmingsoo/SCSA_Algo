'''
와라라ㅏ락!! q가 없어질 때 까지
'''
from collections import deque, defaultdict

n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]
q = deque()
find = False
strong_build = defaultdict(int)
total_build = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "@":  # 진원
            q.append((i, j, 2))
        elif grid[i][j] == "#":
            strong_build[(i, j)] += 1
            total_build += 1
        elif grid[i][j] == "*":
            total_build += 1

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
destroy = 0

while q:
    r, c, power = q.popleft()
    for k in range(4):
        for l in range(1, power + 1):
            nr = r + row[k] * l
            nc = c + col[k] * l
            if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] == "|":
                break
            if grid[nr][nc] == "*":
                grid[nr][nc] = "."
                destroy += 1
                q.append((nr, nc, 1))
            elif grid[nr][nc] == "#":
                if strong_build[(nr, nc)] > 0:
                    strong_build[(nr, nc)] -= 1
                elif strong_build[(nr, nc)] == 0:
                    grid[nr][nc] = "."
                    destroy += 1
                    q.append((nr, nc, 1))

print(destroy, total_build - destroy)
