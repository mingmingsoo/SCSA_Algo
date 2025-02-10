'''
빔.
물*
돌X
고슴S

고슴도치는 상하좌우 이동
물도 확장
물, 고슴은 돌 통과 불가
고슴은 물로 못가, 물도 비버집 못가
고슴도치가 안전하게 비버굴 가고싶어요

물먼저차고 고슴도치이동해야됨

아 D랑 S 서로 바꿔서봐서
테케 이해를 못해서 한참 걸림

'''
from collections import deque
n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]

water_q = deque([])
kosum_q = deque([])
visited = [[False]*m for i in range(n)]
visited_kosum = [[False]*m for i in range(n)]


sr,sc,er,ec = -1,-1,-1,-1
ans = "KAKTUS"
for i in range(n):
    for j in range(m):
        if(grid[i][j]=="S"):
            sr, sc = i,j
            visited_kosum[i][j] = True
            kosum_q.append((i,j,0))
            grid[i][j] = "."
        elif(grid[i][j]=="*"):
            water_q.append((i,j))
            visited[i][j] = True
        elif(grid[i][j]=="D"):
            er,ec = i,j


def bfs():
    global ans
    row = [-1,1,0,0]
    col = [0,0,1,-1]
    while water_q:

        # 물먼저 채우고
        qsize = len(water_q)
        for s in range(qsize):
            wr,wc = water_q.popleft()
            for k in range(4):
                wnr = wr+row[k]
                wnc = wc+col[k]
                if(not(0<=wnr<n and 0<=wnc<m)):
                    continue
                if(not visited[wnr][wnc] and grid[wnr][wnc]=="."):
                    visited[wnr][wnc] = True
                    grid[wnr][wnc] = "*" # 물이 됐옹
                    water_q.append((wnr,wnc))
        # for _ in grid:
        #     print(_)

        kosum_size = len(kosum_q)
        for ks in range(kosum_size):
            if kosum_q:
                r, c, cnt = kosum_q.popleft()
                if (r == er and c == ec):
                    ans = cnt
                    return
                # 고슴도치 이동
                for k in range(4):
                    nr = r + row[k]
                    nc = c + col[k]
                    if (not (0 <= nr < n and 0 <= nc < m)):
                        continue
                    if (not visited_kosum[nr][nc] and (grid[nr][nc] == "." or grid[nr][nc] == "D")):
                        visited_kosum[nr][nc] = True
                        kosum_q.append((nr, nc, cnt + 1))

bfs()
print(ans)

