# 풀이시간: 50분
# 제출횟수: 1회
# 시간: 176ms
# 메모리: 75,196kb

'''
빠른 탈출 조건은 없음 완탐해야함
'''
from collections import deque

T = int(input())


for tc in range(T):

    n, kk = map(int, input().split())  # 맵 크기와 깎을 수 있는 높이
    grid = [[] for i in range(n)]
    maxH = -1
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            grid[i] = tmp
            if (grid[i][j] > maxH):
                maxH = grid[i][j]
    # 안깎았으면 0 에 True 깎았으면 1에 True

    # print(maxH, high_list)

    ans = 0
    row = [0, 1, -1, 0]
    col = [-1, 0, 0, 1]

    visited = [[[False] * 2 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if (grid[i][j] == maxH):
                q = deque()  # q에 바로담기
                q.append((i, j, i,j, 1, True, maxH))
                visited[i][j][0] = True


    while q:
        r, c, br,bc, cnt, bomb, hei = q.popleft() # 부모 높이를 담아줌
        print(r,c,cnt,bomb,hei)
        ans = max(ans, cnt)

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if (not (0 <= nr < n and 0 <= nc < n)):
                continue

            # 부셨든 안부셨든 나보다 낮으면 가.
            if not visited[nr][nc][bomb] and grid[nr][nc] < hei:
                q.append((nr, nc, cnt + 1, bomb, grid[nr][nc]))
                visited[nr][nc][bomb] = True  # 안부셨어요
            elif not visited[nr][nc][1] and grid[nr][nc] - kk < hei and bomb:
                q.append((nr, nc, cnt + 1, False, hei - 1))
                visited[nr][nc][1] = True  # 부셨어요

    print(f"#{tc + 1} {ans}")
