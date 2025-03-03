'''
10트만에 성공
문제설명
    가희는 이동하거나 혹은 머무름 -> 이건 굳이 안해도,,
    이동했는데 고구마있으면 먹음
    T초만큼 이동했을 때 최대한 많은 고구마 먹고싶음

구상
    기본적인 bfs 대신 return 없이
# 틀린이유
    아 고구마 아 다른 경로로 아.. ㅇㅋㅇㅋ

반례
5 5 6
SSGSS
.....
.....
.....
.....
visited를 고구마만 관리
'''
from collections import deque

n, m, time = map(int, input().split())

grid = [list(input()) for i in range(n)]

sr, sc = -1, -1

def find_dog():
    global sr, sc
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "G":
                grid[i][j] = "."
                sr, sc = i, j
                return
find_dog()
ans = 0

def bfs(sr, sc):
    global ans
    q = deque([(sr, sc, 0, 0,[])])  # 위치, 고구마, 시간 , 그리고 고구마
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]
    while q:
        r, c, eat, t, visited = q.popleft()
        # print(r,c,eat,t,visited)
        visited_copy = visited[:]
        if (t > time): # 아 이게 순서가 아나
            return # 이거때문에 틀림
        ans = max(eat, ans)

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if grid[nr][nc] == "#":
                continue
            if grid[nr][nc] == "S" and (nr,nc) not in visited_copy:
                q.append((nr, nc, eat + 1, t + 1, visited_copy+[(nr,nc)]))
            else:
                q.append((nr, nc, eat, t + 1, visited_copy))

bfs(sr, sc)
print(ans)
