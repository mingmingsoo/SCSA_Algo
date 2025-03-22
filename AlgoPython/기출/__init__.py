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

umb.append((er, ec))
visited = [False] * len(umb)
ans = -1


def dfs(r, c, hp, uhp, time):
    global ans
    if (r, c) == (er, ec):
        if (hp + uhp) >= 0:
            ans = time
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
                else:
                    if uhp >= dist:  # 우산으로만 갈 수 있으면
                        visited[i] = True
                        dfs(ur, uc, hp, uhp - dist, time + dist)
                        visited[i] = False
                    else:  # 같이 줄어들면
                        visited[i] = True
                        dist2 = dist - uhp
                        dfs(ur, uc, hp - dist2, 0, time + dist)
                        visited[i] = False


dfs(sr, sc, power, 0, 0)
print(ans)
