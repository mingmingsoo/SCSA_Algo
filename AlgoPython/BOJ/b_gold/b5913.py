n = 5
grid = [[0] * n for i in range(n)]
bn = int(input())
total = n * n - bn
for b in range(bn):
    r, c = map(int, input().split())
    grid[r - 1][c - 1] = 1
#
# for _ in grid:
#     print(*_)

visited = [[False] * n for i in range(n)]
visited[0][0] = visited[n - 1][n - 1] = 1
ans = 0
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def inb(x1, y1, x2, y2):
    if 0 <= x1 < n and 0 <= x2 < n and 0 <= y1 < n and 0 <= y2 < n:
        return True
    return False


def btk(ar, ac, br, bc, aeat, beat):
    global ans, visited
    if aeat + beat == total:
        ans += 1
        return

    for k in range(4):
        for kk in range(4):
            nar = ar + row[k]
            nac = ac + col[k]

            nbr = br + row[kk]
            nbc = bc + col[kk]

            if inb(nar, nac, nbr, nbc) and grid[nar][nac] == grid[nbr][nbc] == 0 and not visited[nar][nac] and not \
                    visited[nbr][nbc]:
                if (nar, nac) == (nbr, nbc) and beat + aeat == total - 1:
                    visited[nar][nac] = visited[nbr][nbc] = True
                    btk(nar, nac, nbr, nbc, aeat + 1, beat)
                    visited[nar][nac] = visited[nbr][nbc] = False
                elif (nar, nac) != (nbr, nbc):
                    visited[nar][nac] = visited[nbr][nbc] = True
                    btk(nar, nac, nbr, nbc, aeat + 1, beat + 1)
                    visited[nar][nac] = visited[nbr][nbc] = False


btk(0, 0, n - 1, n - 1, 1, 1)
print(ans)
