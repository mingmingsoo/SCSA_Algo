'''
문제 설명
    shoot 번 쏠 수 있고 남은 벽돌의 최소 갯수를 구해야함
    중복순열로 순서를 정하고 들어간다.
    연쇄작용은 q를 사용한다. -> 한번에 제거 그리고 즁력
필요한 함수
    duple_perm
    shoot
    gravity
주의할 점
    인덱스 에러?? 다 없어졌을 때 잘 처리 되는지 확인
'''
from collections import deque


def duple_perm(idx):
    global ans, grid
    if idx == shoot:
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    cnt += 1
        ans = min(cnt, ans)
        return
    for jdx in range(m):
        grid_origin = [_[:] for _ in grid]
        shooting(jdx)
        gravity()
        duple_perm(idx + 1)
        grid = grid_origin


def shooting(jdx):
    # 맨 윗줄에 벽이 있을 수 있구낭..
    idx = -1
    # 내려오는 칸 찾기
    for i in range(n):
        if grid[i][jdx] != 0:
            idx = i
            break
    if idx == -1:
        return
    length = grid[idx][jdx]
    visited = [[False] * m for i in range(n)]
    visited[idx][jdx] = True
    q = deque([(idx, jdx, length)])
    while q:
        r, c, leng = q.popleft()

        for k in range(4):
            for l in range(1, leng):
                nr = r + row[k] * l
                nc = c + col[k] * l
                if not (0 <= nr < n and 0 <= nc < m):
                    break
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc, grid[nr][nc]))

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                grid[i][j] = 0


def gravity():
    for j in range(m):
        while True:
            down = False
            for i in range(n - 1, 0, -1):
                if grid[i][j] == 0 and grid[i - 1][j] != 0:
                    down = True
                    grid[i][j], grid[i - 1][j] = grid[i - 1][j], grid[i][j]
            if not down:
                break


row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

T = int(input())
for tc in range(T):
    shoot, m, n = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(n)]
    sel = [0] * shoot
    ans = n * m + 1

    duple_perm(0)
    print(f"#{tc + 1} {ans}")
