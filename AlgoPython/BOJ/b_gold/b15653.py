from collections import deque

def move(r, c):
    while True:
        nr = r + row[k]
        nc = c + col[k]
        if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] == "#":
            break
        r = nr
        c = nc
        if r == er and c == ec:
            break
    return r, c


def duple(oar, oac, obr, obc, ar, ac, br, bc, k):
    # 북남동서
    if k == 0:
        if obr < oar: ar += 1
        else: br += 1
    elif k == 1:
        if obr > oar: ar -= 1
        else: br -= 1
    elif k == 2:
        if obc > oac: ac -= 1
        else: bc -= 1
    elif k == 3:
        if obc < oac: ac += 1
        else: bc += 1
    return ar, ac, br, bc


n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]

ar = ac = br = bc = er = ec = -1
for i in range(n):
    for j in range(m):
        if grid[i][j] == "R":
            ar, ac = i, j
            grid[i][j] = "."
        elif grid[i][j] == "B":
            br, bc = i, j
            grid[i][j] = "."
        elif grid[i][j] == "O":
            er, ec = i, j
            grid[i][j] = "."
visited = set()
visited.add((ar, ac, br, bc))
ans = -1
q = deque([(ar, ac, br, bc, 0)])
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

while q:
    oar, oac, obr, obc, time = q.popleft()
    if obr == er and obc == ec:
        continue
    if oar == er and oac == ec:
        ans = time
        break
    for k in range(4):
        ar, ac, br, bc = oar, oac, obr, obc
        ar, ac = move(ar, ac)
        br, bc = move(br, bc)
        if (ar, ac) == (oar, oac) and (br, bc) == (obr, obc):
            continue
        if (ar, ac) == (br, bc) and (ar, ac) != (er, ec):
            ar, ac, br, bc = duple(oar, oac, obr, obc, ar, ac, br, bc, k)
        if (ar, ac, br, bc) not in visited:
            visited.add((ar, ac, br, bc))
            q.append((ar, ac, br, bc, time + 1))
print(ans)
