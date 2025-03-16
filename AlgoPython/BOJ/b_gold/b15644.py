from collections import deque

n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]


def find(type):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == type:
                return i, j


ar, ac = find("R")
br, bc = find("B")
er, ec = find("O")
ans = -1
ans_path = ""
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def bfs(ar, ac, br, bc):
    global ans, ans_path
    q = deque([(ar, ac, br, bc, 0, "")])
    while q:
        oar, oac, obr, obc, time, path = q.popleft()
        if time > 10:
            return
        if obr == er and obc == ec:
            continue
        if oar == er and oac == ec:
            ans = time
            ans_path = path
            return
        for k in range(4):
            ar, ac, br, bc = oar, oac, obr, obc
            # a 옮기기
            while True:
                nar = ar + row[k]
                nac = ac + col[k]
                if not (0 <= nar < n and 0 <= nac < m) or grid[nar][nac] == "#":
                    break
                ar, ac = nar, nac
                if ar == er and ac == ec:
                    break
            # b 옮기기
            while True:
                nbr = br + row[k]
                nbc = bc + col[k]
                if not (0 <= nbr < n and 0 <= nbc < m) or grid[nbr][nbc] == "#":
                    break
                br, bc = nbr, nbc
                if br == er and bc == ec:
                    break
            if ar == oar and ac == oac and br == obr and bc == obc:
                continue
            if ar == br and ac == bc and not (ar == er and ac == ec):
                if k == 0:
                    if obr < oar:
                        ar += 1
                    else:
                        br += 1
                elif k == 1:
                    if obr > oar:
                        ar -= 1
                    else:
                        br -= 1
                elif k == 2:
                    if obc > oac:
                        ac -= 1
                    else:
                        bc -= 1
                elif k == 3:
                    if obc < oac:
                        ac += 1
                    else:
                        bc += 1
            q.append((ar, ac, br, bc, time + 1, path + "UDRL"[k]))


bfs(ar, ac, br, bc)
print(ans)
if ans != -1: print(ans_path)
