'''
문제시작
0830~ 0911

문제설명
M개의 조합을 선택해서 바이러스를 퍼뜨린다
모두 퍼졌을 때 최소 시간

놓친부분
활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.

제출횟수
3회

3 1
0 2 0
2 2 0
0 0 2
정답 2
'''
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
arr = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            arr.append((i, j))

sel = [0] * m

ans = int(1e9)
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def combi(sidx, idx):
    global ans
    if sidx == m:
        grid_copy = [_[:] for _ in grid]
        q = deque()
        for r, c in sel:
            grid_copy[r][c] = 3
            q.append((r, c, 0))
        ele_time = 0
        while q:
            r, c, time = q.popleft()
            if grid_copy[r][c] != 3:
                ele_time = time
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if not (0 <= nr < n and 0 <= nc < n):
                    continue
                if grid_copy[nr][nc] == 0:
                    grid_copy[nr][nc] = 1
                    q.append((nr, nc, time + 1))
                elif grid_copy[nr][nc] == 2:
                    grid_copy[nr][nc] = 3
                    q.append((nr, nc, time + 1))
        isok = True
        for i in range(n):
            for j in range(n):
                if grid_copy[i][j] == 0:
                    isok = False
                    break
            if not isok:
                break
        if isok:
            ans = min(ans, ele_time)

        return
    if idx == len(arr):
        return
    sel[sidx] = arr[idx]
    combi(sidx + 1, idx + 1)
    combi(sidx, idx + 1)


combi(0, 0)
if ans == int(1e9):
    print(-1)
else:
    print(ans)
