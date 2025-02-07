'''
2차원 토마토와 동일하지만
3차원이다.


로직은 비슷하게 bfs후에
안익은토마토인데 방문한적이 없으면 안익은거라
-1 출력이다..

익은 토마토가 없을 떄 탐색을 안하고 바로 -1 출력하고 exit 해도 되는데 맘이 급해서 못했다.
그 로직을 추가하겠음 !

'''
from collections import deque

M, N, H = map(int, input().split())

grid = [[list(map(int, input().split())) for i in range(N)] for _ in range(H)]
# print(grid)

q = deque([])

row = [-1, 1, 0, 0, 0, 0]
col = [0, 0, 1, -1, 0, 0]
hei = [0, 0, 0, 0, 1, -1] # 높이도 만들어준다.
ans = 0
visited = [[[0] * M for i in range(N)] for _ in range(H)]


def bfs():
    global ans
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if (grid[h][i][j] == 1):  # 1이면 바로 q에 넣어준다.
                    q.append((h, i, j, ans))
                    visited[h][i][j] = True
    if(not q):
        print(-1)
        exit()

    while q:
        h, r, c, day = q.popleft()
        # print(h,r,c,day)
        ans = max(day, ans)
        for k in range(6):
            nh = h + hei[k]
            nr = r + row[k]
            nc = c + col[k]

            if (not (0 <= nr < N and 0 <= nc < M and 0 <= nh < H)):
                continue

            if (not visited[nh][nr][nc] and grid[nh][nr][nc] == 0):
                q.append((nh, nr, nc, day + 1))
                visited[nh][nr][nc] = True

bfs()


def valid():
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if (grid[h][i][j] == 0 and not visited[h][i][j]):
                    return False
    return True


if (not valid()):
    ans = -1

print(ans)
