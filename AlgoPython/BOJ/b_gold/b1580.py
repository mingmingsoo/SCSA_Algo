'''
구슬탈출이랑 비슷한듯
방향이...
'''
from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]

sar = sac = sbr = sbc = -1

for i in range(n):
    for j in range(m):
        if grid[i][j] == "A":
            sar, sac = i, j
        elif grid[i][j] == "B":
            sbr, sbc = i, j

ans = -1
row = [0, -1, 1, 0, 0, 1, 1, -1, -1]  # 안움직이는 거 + 8방
col = [0, 0, 0, 1, -1, 1, -1, 1, -1]


def bfs(sar, sac, sbr, sbc):
    global ans
    q = deque([(sar, sac, sbr, sbc, 0)])
    visited = [[[[0] * m for i in range(n)] for i in range(m)] for i in range(n)]
    visited[sar][sac][sbr][sbc] = 1
    while q:
        ar, ac, br, bc, cnt = q.popleft()
        if (ar, ac) == (sbr, sbc) and (br, bc) == (sar, sac):
            ans = cnt
            return

        for k in range(9):
            for kk in range(9):
                nar = ar + row[k]
                nac = ac + col[k]

                nbr = br + row[kk]
                nbc = bc + col[kk]

                if not (0 <= nar < n and 0 <= nac < m and 0 <= nbr < n and 0 <= nbc < m) or \
                        grid[nar][nac] == "X" or grid[nbr][nbc] == "X" or \
                        visited[nar][nac][nbr][nbc]:
                    continue
                if (nar, nac) == (br, bc) and (nbr, nbc) == (ar, ac):
                    continue  # 교차
                if (nar, nac) == (nbr, nbc):
                    continue  # 같은 위치
                visited[nar][nac][nbr][nbc] = 1
                q.append((nar, nac, nbr, nbc, cnt + 1))


bfs(sar, sac, sbr, sbc)
print(ans)
