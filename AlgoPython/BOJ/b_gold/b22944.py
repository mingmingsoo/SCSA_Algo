import sys

sys.setrecursionlimit(10 ** 5)
n, power, plus = map(int, input().split())
grid = [list(input()) for i in range(n)]
sr, sc, er, ec = -1, -1, -1, -1
umb = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == "S":
            sr, sc = i, j
        elif grid[i][j] == "E":
            er, ec = i, j
        elif grid[i][j] == "U":
            umb.append((i, j))

visited = [False] * len(umb)
ans = int(1e9)


def dfs(r, c, hp, uhp, time):
    global ans
    if abs(er - r) + abs(ec - c) <= hp + uhp:
        ans = min(time + abs(er - r) + abs(ec - c), ans)
        return

    for i in range(len(umb)):
        if not visited[i]:
            ur, uc = umb[i]
            dist = abs(ur - r) + abs(uc - c)
            if (hp + uhp) >= dist:
                if uhp == 0:
                    visited[i] = True
                    dfs(ur, uc, hp - dist, plus, time + dist)
                    visited[i] = False
                elif uhp > dist:
                    visited[i] = True
                    dfs(ur, uc, hp, plus, time + dist)
                    visited[i] = False
                elif uhp <= dist:
                    visited[i] = True
                    dist2 = dist - uhp
                    dfs(ur, uc, hp - dist2, plus, time + dist)
                    visited[i] = False


dfs(sr, sc, power, 0, 0)
if ans == int(1e9):
    print(-1)
else:
    print(ans)
