from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]

sr, sc = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "D":
            sr, sc = i, j
            grid[i][j] = "."

ans = -1
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


def rotation(k, dice):
    if k == 0:
        new_dice = [dice[2], dice[3], dice[1], dice[0], dice[4], dice[5]]
        return new_dice
    elif k == 2:
        new_dice = [dice[3], dice[2], dice[0], dice[1], dice[4], dice[5]]
        return new_dice
    elif k == 1:
        new_dice = [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]
        return new_dice
    elif k == 3:
        new_dice = [dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]]
        return new_dice


def bfs(sr, sc):
    global ans
    q = deque([(sr, sc, [0, 1, 0, 0, 0, 0], 0)])
    visited = [[[False] * 6 for i in range(m)] for i in range(n)]
    visited[sr][sc][1] = True
    while q:
        r, c, dice, cnt = q.popleft()
        print(r,c,dice,cnt)
        if grid[r][c] == "R" and dice[1]:
            ans = cnt
            return
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            dice = rotation(k, dice)
            idx = dice.index(1)
            if grid[nr][nc] != "#" and not visited[nr][nc][idx]:
                visited[nr][nc][idx] = True
                q.append((nr, nc, dice, cnt + 1))


bfs(sr, sc)
print(ans)
