'''
다시 푼다 . 다시
'''

from collections import deque
import itertools
import sys
input = sys.stdin.readline

def bfs(s, e):
    sr, sc = s
    er, ec = e
    visited = [[False] * m for i in range(n)]
    visited[sr][sc] = True
    q = deque([(sr, sc, 0)])
    while q:
        r, c, d = q.popleft()
        if (r, c) == (er, ec):
            return d
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m) or visited[nr][nc] or grid[nr][nc] == "x":
                continue
            visited[nr][nc] = True
            q.append((nr, nc, d + 1))
    return -1


def combi(sidx, idx):
    if sidx == 2:
        dist = bfs(location_dict[sel[0]], location_dict[sel[1]])
        if dist != -1:
            dist_dict[(sel[0], sel[1])] = dist
        return
    if idx == cnt:
        return
    sel[sidx] = idx
    combi(sidx + 1, idx + 1)
    combi(sidx, idx + 1)


while True:

    m, n = map(int, input().split())
    if m == n == 0:
        break
    grid = [list(input().rstrip()) for i in range(n)]
    # 시작점은 0 아닌 애들은 1부터 넘버링
    num = 1
    cnt = 0
    location_dict = {}
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "o":
                grid[i][j] = 0
                location_dict[0] = (i, j)
                cnt += 1
            elif grid[i][j] == "*":
                grid[i][j] = num
                location_dict[num] = (i, j)
                num += 1
                cnt += 1
    sel = [0] * 2
    dist_dict = {}

    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]

    combi(0, 0)
    arr = list(range(1,cnt))
    ans = int(1e9)
    sel = itertools.permutations(arr)
    for s in sel:
        dist = 0
        if (0, s[0]) in dist_dict:
            dist = dist_dict[(0, s[0])]
        else:
            continue
        no = False
        for i in range(cnt - 2):
            x, y = s[i], s[i + 1]
            if x > y:
                x, y = y, x
            if (x, y) in dist_dict:
                dist += dist_dict[(x, y)]
            else:
                no = True
                break
        if no:
            continue
        ans = min(ans, dist)
    if ans == int(1e9):
        print(-1)
    else:
        print(ans)