'''
3차원 bfs
'''

from collections import deque


def bfs():
    global ans
    visited = [[[False] * M for i in range(N)] for i in range(H)]
    visited[sh][sr][sc] = True
    q = deque([(sh, sr, sc, 0)])
    while q:
        h, r, c, time = q.popleft()
        # print(h,r,c,time)
        if h == eh and r == er and c == ec:
            ans = time
            return
        for k in range(6):
            nh = h + hei[k]
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nh < H and 0 <= nr < N and 0 <= nc < M) or visited[nh][nr][nc] or cube[nh][nr][nc] == "#":
                continue
            visited[nh][nr][nc] = True
            q.append((nh, nr, nc, time + 1))


while True:

    H, N, M = map(int, input().split())
    if H == N == M == 0:
        break
    cube = []
    sh, sr, sc, eh, er, ec = -1, -1, -1, -1, -1, -1
    for h in range(H):
        grid = [list(input()) for i in range(N)]
        input()
        cube.append(grid)

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if cube[h][i][j] == "S":
                    sh, sr, sc = h, i, j
                    cube[h][i][j] = "."
                elif cube[h][i][j] == "E":
                    eh, er, ec = h, i, j
                    cube[h][i][j] = "."

    hei = [-1, 1, 0, 0, 0, 0]
    row = [0, 0, 1, -1, 0, 0]
    col = [0, 0, 0, 0, 1, -1]

    ans = 30 * 30 * 30 + 1

    bfs()
    if ans == 30 * 30 * 30 + 1:
        print("Trapped!")
    else:
        print(f"Escaped in {ans} minute(s).")
