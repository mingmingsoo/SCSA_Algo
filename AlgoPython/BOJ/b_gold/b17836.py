'''
문제 설명
    용사는 공주를 향해 T시간안에 가야한다
    1. 그냥 길따라 가던지
    2. 검을 얻고 공주에게 가던지 둘 중 하나
구상
    일단 검 여부를 True, False로 하고
    검이 있으면 백이 있어도 갈 수 있게 조건을 걸어야 할 듯
    visited 가 3차원이 필요함
    -> 검이없는 상태에서 먼저 어딘가 가버리면 검이 있어도 그 자리를 못가기 때문
    bfs로 풀겠따.
틀린이유:
    T시간안에 조건을 빼먹음
'''
from collections import deque

n, m, T = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

ans = "Fail"


def bfs(sr, sc, er, ec):
    global ans
    q = deque([(sr, sc, 0, False,0)])  # 위치와 거리, 검이 있는지 여부, 시간
    visited = [[[False] * m for i in range(n)] for i in range(2)]
    visited[sr][sc][0] = True  # 처음엔 검이 없으요
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]
    while q:
        r, c, cnt, have_knife,time = q.popleft()
        if(time>T):
            continue
        if (r == er and c == ec):
            ans = cnt
            return

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if (grid[nr][nc] == 0 and not visited[have_knife][nr][nc]):  # 그냥 갈 수 있는 길들
                visited[have_knife][nr][nc] = True
                q.append((nr, nc, cnt + 1, have_knife,time+1))
            elif(grid[nr][nc] == 2 and not visited[have_knife][nr][nc]):
                visited[have_knife][nr][nc] = True
                q.append((nr, nc, cnt + 1, True,time+1))
            elif (grid[nr][nc] == 1 and have_knife and not visited[have_knife][nr][nc]):  # 벽인데 검이 있으면 갈 수 이썽
                visited[have_knife][nr][nc] = True
                q.append((nr, nc, cnt + 1, have_knife,time+1))


bfs(0, 0, n - 1, m - 1)
print(ans)
