'''
path set으로
열쇠 먹으면 visited 초기화.
'''
from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]

sr, sc, er, ec = -1, -1, -1, -1

for i in range(n):
    for j in range(m):
        if grid[i][j] == "@":
            sr, sc = i, j
            grid[i][j] = "*"
        elif grid[i][j] == "!":
            er, ec = i, j
            grid[i][j] = "*"

visited = [[False] * m for i in range(n)]
key = set()
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

cnt = 0


def bfs():
    global visited, cnt
    visited[sr][sc] = True
    q = deque([(sr, sc)])
    path = set()
    while q:
        r, c = q.popleft()
        path.add((r, c))
        if (r, c) == (er, ec):
            print(len(path))
            for pr, pc in path:
                print(pr + 1, pc + 1)
            return
        yam_lst = []
        v_lst = []
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if grid[nr][nc] == "#" or visited[nr][nc]:
                continue
            if "a" <= grid[nr][nc] <= "z":
                if chr(ord(grid[nr][nc]) - 32) not in key: # 틀린이유 여기서... 대문자로 검사해야하는데 소문자로 검사해서 set에 계속 들어갔었음!
                    key.add(chr(ord(grid[nr][nc]) - 32))
                    yam_lst.append((nr, nc))
                else:
                    v_lst.append((nr, nc))
            elif "A" <= grid[nr][nc] <= "Z" and grid[nr][nc] in key:
                v_lst.append((nr, nc))
            elif grid[nr][nc] == "*":
                v_lst.append((nr, nc))
        if yam_lst:
            cnt += 1
            visited = [[False] * m for i in range(n)]
            for yr, yc in yam_lst:
                visited[yr][yc] = True
                q.append((yr, yc))
            for vr, vc in v_lst:
                visited[vr][vc] = True
                q.append((vr, vc))
        else:
            for vr, vc in v_lst:
                visited[vr][vc] = True
                q.append((vr, vc))


bfs()
