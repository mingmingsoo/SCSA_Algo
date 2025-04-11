'''
문제 설명
    히야 진짜 어려운데
    일단 각 좌표마다 0,1,2,3, 회전시킨 좌표를 3차원에 배열로 미리 생성한다..
    영역은 i,j 에서 4를 나눈 몫이 될거임

'''
from collections import deque

n = int(input())
N = 4 * n
tmp = [list(input()) for i in range(N)]
h, r, c = 0, 0, 0
for i in range(N):
    for j in range(N):
        if tmp[i][j] == "S":
            r, c = i, j
grid = [[[0] * N for i in range(N)] for i in range(4)]


def rotation(small_tmp):
    ro_tmp = [[0] * 4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            ro_tmp[i][j] = small_tmp[4 - j - 1][i]
    return ro_tmp


for sr in range(0, N, 4):
    for sc in range(0, N, 4):
        # 시작점
        small_tmp = [_[sc:sc + 4] for _ in tmp[sr:sr + 4]]
        for i in range(sr, sr + 4):
            for j in range(sc, sc + 4):
                grid[0][i][j] = small_tmp[i - sr][j - sc]
        small_tmp = rotation(small_tmp)
        for i in range(sr, sr + 4):
            for j in range(sc, sc + 4):
                grid[1][i][j] = small_tmp[i - sr][j - sc]
        small_tmp = rotation(small_tmp)
        for i in range(sr, sr + 4):
            for j in range(sc, sc + 4):
                grid[2][i][j] = small_tmp[i - sr][j - sc]
        small_tmp = rotation(small_tmp)
        for i in range(sr, sr + 4):
            for j in range(sc, sc + 4):
                grid[3][i][j] = small_tmp[i - sr][j - sc]
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
ans = -1


def bfs(sh, sr, sc):
    global ans
    q = deque([(sh, sr, sc, 0)])
    visited = [[[False] * N for i in range(N)] for i in range(4)]
    visited[sh][sr][sc] = True
    while q:
        h, r, c, time = q.popleft()
        if grid[h][r][c] == "E":
            ans = time
            return
        # 가만히 있을 때
        nr, nc = r, c
        my_r_area = r // 4
        my_c_area = c // 4
        nr -= my_r_area * 4
        nc -= my_c_area * 4
        nr, nc = nc, 4 - nr - 1
        nr += my_r_area * 4
        nc += my_c_area * 4
        if not visited[(h + 1) % 4][nr][nc]:
            visited[(h + 1) % 4][nr][nc] = True
            q.append(((h + 1) % 4, nr, nc, time + 1))

        # 움직일 때
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            next_r_area = nr // 4
            next_c_area = nc // 4
            if (my_r_area, my_c_area) == (next_r_area, next_c_area):  # 같은 영역이면..
                if grid[h][nr][nc] != "#":
                    nr -= my_r_area * 4
                    nc -= my_c_area * 4
                    nr, nc = nc, 4 - nr - 1
                    nr += my_r_area * 4
                    nc += my_c_area * 4
                    if not visited[(h + 1) % 4][nr][nc]:
                        visited[(h + 1) % 4][nr][nc] = True
                        q.append(((h + 1) % 4, nr, nc, time + 1)) # 다른 영역이면..
            else:
                if grid[0][nr][nc] != "#":
                    nr -= next_r_area * 4
                    nc -= next_c_area * 4
                    nr, nc = nc, 4 - nr - 1
                    nr += next_r_area * 4
                    nc += next_c_area * 4
                    if not visited[1][nr][nc]:
                        visited[1][nr][nc] = True
                        q.append((1, nr, nc, time + 1))

bfs(h, r, c)
print(ans)

