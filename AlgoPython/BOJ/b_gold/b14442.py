'''
b14442
문제 설명
    벽을 K개 까지 이동가능
    visited를 k+1,m,n 으로 관리
    최단경로이므로 기본 bfs사용

두번쨰 풀이
    힙큐써서 최대한 목적지를 향해서 가게하기
    -> 이러면 시간초과나네 ;;ㅋㅋ

세번쨰 풀이
    3차원 visited 말고 set써보기
    이래도 시간초과나네
'''
from collections import deque

n, m, limit = map(int, input().split())
grid = [list(map(int, input())) for i in range(n)]


def bfs(sr, sc, er, ec):
    global ans
    visited = set()
    visited.add((sr,sc,0))
    q = deque([(0, 0, 1, 0)])  # r,c,dist, 벽 몇번 부쉈는지
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]
    while q:
        r, c, dist, bomb = q.popleft()

        if (r == er and c == ec):
            ans = dist
            return

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]

            if not (0 <= nr < n and 0 <= nc < m):
                continue
            # 그냥 이동 가능
            if (nr,nc,bomb) not in visited and grid[nr][nc] == 0:
                visited.add((nr,nc,bomb))
                q.append((nr, nc, dist + 1, bomb))

            # 벽을 부술 수 있으면 이동 가능
            if bomb < limit and (nr,nc,bomb+1) not in visited and grid[nr][nc] == 1:
                visited.add((nr,nc,bomb+1))
                q.append((nr, nc, dist + 1, bomb + 1))

ans = -1
bfs(0, 0, n - 1, m - 1)
print(ans)
