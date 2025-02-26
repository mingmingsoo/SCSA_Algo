'''
미친토마토
'''
import sys
from collections import deque
input = sys.stdin.readline
w, v, u, t, s, r, q, p, o, n, m = map(int, input().split())
grid = [[[[[[[[[[list(map(int, input().split())) for i in range(v)] for i in range(u)] for i in range(t)] for i in
              range(s)] for i in range(r)] for i in range(q)] for i in range(p)] for i in range(o)] for i in range(n)]
        for i in range(m)]

md = [1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nd = [0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
od = [0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pd = [0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
qd = [0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0]
td = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 0]
ud = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0]
vd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0]
wd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1]

# visited = [[[[[[[[[[[False] * w for i in range(v)] for i in range(u)] for i in range(t)] for i in
#                  range(s)] for i in range(r)] for i in range(q)] for i in range(p)] for i in range(o)] for i in
#             range(n)]
#            for i in range(m)]

# w, v, u, t, s, r, q, p, o, n, m

deq = deque()
for mm in range(m):
    for nn in range(n):
        for oo in range(o):
            for pp in range(p):
                for qq in range(q):
                    for rr in range(r):
                        for ss in range(s):
                            for tt in range(t):
                                for uu in range(u):
                                    for vv in range(v):
                                        for ww in range(w):
                                            # print(mm, nn, oo, pp, qq, rr, ss, tt, uu, vv, ww)
                                            # if (grid[ww][vv][uu][tt][ss][rr][qq][pp][oo][nn][mm] == 1):
                                            if (grid[mm][nn][oo][pp][qq][rr][ss][tt][uu][vv][ww] == 1):
                                                # 1이 익은 토마토
                                                deq.append((mm, nn, oo, pp, qq, rr, ss, tt, uu, vv, ww, 0))
                                                # visited[mm][nn][oo][pp][qq][rr][ss][tt][uu][vv][ww] = True

ans = 0


def bfs():
    global ans
    while deq:
        mi, ni, oi, pi, qi, ri, si, ti, ui, vi, wi, cnt = deq.popleft()
        ans = cnt

        for k in range(22):
            nm = mi + md[k]
            nn = ni + nd[k]
            no = oi + od[k]
            np = pi + pd[k]
            nq = qi + qd[k]
            nr = ri + rd[k]
            ns = si + sd[k]
            nt = ti + td[k]
            nu = ui + ud[k]
            nv = vi + vd[k]
            nw = wi + wd[k]

            if not (0 <= nm < m and
                    0 <= nn < n and
                    0 <= no < o and
                    0 <= np < p and
                    0 <= nq < q and
                    0 <= nr < r and
                    0 <= ns < s and
                    0 <= nt < t and
                    0 <= nu < u and
                    0 <= nv < v and
                    0 <= nw < w):
                continue
            if grid[nm][nn][no][np][nq][nr][ns][nt][nu][nv][nw] == 0:
                deq.append((nm, nn, no, np, nq, nr, ns, nt, nu, nv, nw, cnt + 1))
                grid[nm][nn][no][np][nq][nr][ns][nt][nu][nv][nw] = 1

            # if not visited[nm][nn][no][np][nq][nr][ns][nt][nu][nv][nw] and \
            #         grid[nm][nn][no][np][nq][nr][ns][nt][nu][nv][nw] == 0:
            #     visited[nm][nn][no][np][nq][nr][ns][nt][nu][nv][nw] = True
            #     deq.append((nm, nn, no, np, nq, nr, ns, nt, nu, nv, nw, cnt + 1))


def valid():
    global ans
    for mm in range(m):
        for nn in range(n):
            for oo in range(o):
                for pp in range(p):
                    for qq in range(q):
                        for rr in range(r):
                            for ss in range(s):
                                for tt in range(t):
                                    for uu in range(u):
                                        for vv in range(v):
                                            for ww in range(w):
                                                if (grid[mm][nn][oo][pp][qq][rr][ss][tt][uu][vv][ww] == 0):
                                                # if (grid[mm][nn][oo][pp][qq][rr][ss][tt][uu][vv][ww] == 0 and not
                                                # visited[mm][nn][oo][pp][qq][rr][ss][tt][uu][vv][ww]):
                                                    ans = -1
                                                    return


bfs()
valid()
print(ans)
