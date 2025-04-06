# 고대 ###############################
'''
문제 설명
    1. 격자 선택
    2. bfs 진행 (while)
'''
from collections import deque

n = 5
turn, fn = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
fill = list(map(int, input().split()))
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def rotation(small_grid):
    ro = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            ro[i][j] = small_grid[3 - j - 1][i]
    return ro


def bfs():
    total = 0
    visited = [[False] * n for i in range(n)]
    lo = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                ele = 0
                visited[i][j] = True
                q = deque([(i, j)])
                ele_lo = []
                while q:
                    qr, qc = q.popleft()
                    ele_lo.append((qr, qc))
                    ele += 1
                    for k in range(4):
                        nqr = qr + row[k]
                        nqc = qc + col[k]
                        if not (0 <= nqr < n and 0 <= nqc < n) or visited[nqr][nqc] or grid[nqr][nqc] != grid[i][j]:
                            continue
                        visited[nqr][nqc] = True
                        q.append((nqr, nqc))
                if ele >= 3:
                    lo.extend(ele_lo)
                    total += ele

    return total, lo


for t in range(turn):
    ans = 0
    sel = []

    for r in range(3):
        for c in range(3):
            grid_origin = [_[:] for _ in grid]
            for degree in range(90, 360, 90):
                small_grid = [_[c:c + 3] for _ in grid[r:r + 3]]
                ro = rotation(small_grid)
                for i in range(3):
                    for j in range(3):
                        grid[i + r][j + c] = ro[i][j]
                cnt, location = bfs()
                if cnt:
                    sel.append((-cnt, degree, c, r, [_[:] for _ in grid]))
                small_grid = ro
            grid = [_[:] for _ in grid_origin]

    if not sel:
        break
    sel.sort()
    score, degree, cc, rr, new_grid = sel[0]
    grid = new_grid

    while True:
        cnt, location = bfs()
        if cnt:
            ans += cnt
            for r, c in location:
                grid[r][c] = 0
        else:
            break
        for j in range(n):
            for i in range(n - 1, -1, -1):
                if not grid[i][j]:
                    grid[i][j] = fill.pop(0)
    print(ans, end=" ")
############# 마법
'''
문제설명
    1. 골렘 이동
    2. 정령 탈출
중심좌표 r,c
'''
from collections import deque

n, m, pn = map(int, input().split())
n += 3
grid = [[0] * m for i in range(n)]
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


def oob(r, c):
    if 0 <= r < n and 0 <= c < m:
        return True
    return False


def down():
    global r
    # 중심 r,c
    #       왼 r,c-1 하 r+1,c 우 r,c+1
    # 그 밑   r+1,c-1  r+2,c   r+1,c+1
    while oob(r + 1, c - 1) and oob(r + 2, c) and oob(r + 1, c + 1) and not grid[r + 1][c - 1] and not grid[r + 2][
        c] and not grid[r + 1][c + 1]:
        r += 1


def left():
    global r, c, d
    # 중심 r,c
    #       위왼 r-1,c-1 왼왼 r,c-2 아왼 r+1,c-1
    #                       r+1,c-2    r+2,c-1
    if oob(r - 1, c - 1) and oob(r, c - 2) and oob(r + 1, c - 1) and oob(r + 1, c - 2) and oob(r + 2, c - 1) and not \
            grid[r - 1][c - 1] and not grid[r][c - 2] and not grid[r + 1][c - 1] and not grid[r + 1][c - 2] and not \
            grid[r + 2][c - 1]:
        d = (d - 1) % 4
        r += 1
        c -= 1
        return True
    return False


def right():
    global r, c, d
    # 중심 r,c
    #       위오 r-1,c+1 오오 r,c+2  아오 r+1,c+1
    #                       r+1,c+2     r+2,c+1
    if oob(r - 1, c + 1) and oob(r, c + 2) and oob(r + 1, c + 1) and oob(r + 1, c + 2) and oob(r + 2, c + 1) and not \
            grid[r - 1][c + 1] and not grid[r][c + 2] and not grid[r + 1][c + 1] and not grid[r + 1][c + 2] and not \
            grid[r + 2][c + 1]:
        d = (d + 1) % 4
        r += 1
        c += 1
        return True
    return False


def bfs(sr, sc):
    visited = [[False] * m for i in range(n)]
    visited[sr][sc] = True
    q = deque([(sr, sc, grid[sr][sc])])
    maxi = sr
    while q:
        r, c, p = q.popleft()
        maxi = max(maxi, r)
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not oob(nr, nc) or visited[nr][nc]:
                continue
            if abs(grid[nr][nc]) == p:
                visited[nr][nc] = True
                q.append((nr, nc, abs(grid[nr][nc])))
            if grid[r][c] < 0 and grid[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc, abs(grid[nr][nc])))

    return maxi

ans = 0
for p in range(pn):
    c, d = map(int, input().split())
    c -= 1
    r = 1
    while True:
        down()
        move = False
        if left():
            move = True
        if right():
            move = True
        if not move:
            break
    if r <= 3:
        grid = [[0] * m for i in range(n)]
        continue

    # 흔적 남기기
    grid[r][c] = grid[r + 1][c] = grid[r - 1][c] = grid[r][c - 1] = grid[r][c + 1] = p + 1
    if d == 0:
        grid[r - 1][c] = -(p + 1)
    elif d == 2:
        grid[r + 1][c] = -(p + 1)
    elif d == 1:
        grid[r][c + 1] = -(p + 1)
    elif d == 3:
        grid[r][c - 1] = -(p + 1)

    maxi = bfs(r, c)
    ans += maxi - 2
print(ans)
#############################루돌푸
'''
문제설명
    1. 루돌프 이동
    2. 산타 이동
입력
    맵 n 턴 수 m 산타 수 p 루돌프 힘 c 산타 힘 d
    루돌프 위치
    산타 번호와 위치

5 1 4 1 1
5 1
1 4 2
2 3 3
3 2 4
4 1 5

5 2 4 1 1
5 1
1 5 2
2 5 3
3 5 4
4 5 5

'''
from collections import deque

n, turn, sn, rp, sp = map(int, input().split())
rr, rc = map(lambda x: int(x) - 1, input().split())
grid = [[0] * n for i in range(n)]
santa_lst = [0] * (sn + 1)
row = [-1, 0, 1, 0, 1, 1, -1, -1]
col = [0, 1, 0, -1, 1, -1, 1, -1]
change = [2, 3, 0, 1]
for s in range(sn):
    idx, r, c = map(int, input().split())
    santa_lst[idx] = [r - 1, c - 1, 0]  # 기절 시간
    grid[r - 1][c - 1] = idx
score = [0] * (sn + 1)


def cal(rr, rc, sr, sc):
    return (rr - sr) ** 2 + (rc - sc) ** 2


def jump(nr, nc, d):
    q = deque([(nr, nc)])
    tmp = []
    while q:
        qr, qc = q.popleft()
        tmp.append(grid[qr][qc])
        nqr, nqc = qr + row[d], qc + col[d]
        if 0 <= nqr < n and 0 <= nqc < n and grid[nqr][nqc]:
            q.append((nqr, nqc))
    return tmp


def merge(rr, rc, idx, d, power):
    global score
    # 점수 맥이고 기절
    santa_lst[idx][2] = t  # 기절!
    score[idx] += power
    grid[rr][rc] = 0

    # 산타 이동
    nr = rr + row[d] * power
    nc = rc + col[d] * power
    if not (0 <= nr < n and 0 <= nc < n):  # 쥬금
        santa_lst[idx] = 0
        return
    if grid[nr][nc] == 0:  # 빈 공간이면 충돌 없성
        grid[nr][nc] = idx
        santa_lst[idx][0] = nr
        santa_lst[idx][1] = nc
    else:
        # 충돌 발생....
        move_lst = jump(nr, nc, d)
        move_lst.reverse()
        for jdx in move_lst:
            # 한 칸 씩만 밀리넹..
            sr, sc, stun = santa_lst[jdx]
            nsr = sr + row[d]
            nsc = sc + col[d]
            if not (0 <= nsr < n and 0 <= nsc < n):
                santa_lst[jdx] = 0  # 쥬금
                grid[sr][sc] = 0
            else:
                santa_lst[jdx][0] = nsr
                santa_lst[jdx][1] = nsc
                grid[sr][sc], grid[nsr][nsc] = grid[nsr][nsc], grid[sr][sc]

        grid[nr][nc] = idx
        santa_lst[idx][0] = nr
        santa_lst[idx][1] = nc


def ru_move():
    global rr, rc
    lst = []
    for idx, santa in enumerate(santa_lst):
        if santa == 0:  # 쥬근애 빼고
            continue
        sr, sc, stun = santa
        dist = cal(rr, rc, sr, sc)
        lst.append((dist, -sr, -sc, idx))

    lst.sort()
    dist, sr, sc, idx = lst[0]
    sr *= -1
    sc *= -1
    lst = []
    for k in range(8):
        nr = rr + row[k]
        nc = rc + col[k]
        dist = cal(nr, nc, sr, sc)
        lst.append((dist, nr, nc, idx, k))
    lst.sort()
    dist, nr, nc, idx, d = lst[0]
    rr, rc = nr, nc  # 루돌프 위치 변환
    if grid[rr][rc]:  # 충돌 발생
        merge(rr, rc, idx, d, rp)


def santa_move():
    for idx, santa in enumerate(santa_lst):
        if santa == 0:  # 쥬근애 빼고
            continue
        sr, sc, stun = santa
        if stun and stun >= t - 1:  # 기절빼고
            continue
        cur = cal(rr, rc, sr, sc)
        lst = []
        for k in range(4):
            nr = sr + row[k]
            nc = sc + col[k]
            next = cal(rr, rc, nr, nc)
            if 0 <= nr < n and 0 <= nc < n and next < cur and grid[nr][nc] == 0:
                lst.append((next, k, nr, nc))
        if lst:
            lst.sort()
            dist, d, nr, nc = lst[0]
            santa_lst[idx][0] = nr
            santa_lst[idx][1] = nc
            grid[sr][sc], grid[nr][nc] = grid[nr][nc], grid[sr][sc]
            if (nr, nc) == (rr, rc):
                merge(rr, rc, idx, change[d], sp)
        # print(idx,"번 산타 이동 후")
        # myprint()

def myprint():
    for i in range(n):
        for j in range(n):
            if (i, j) == (rr, rc):
                print("R", end=" ")
            else:
                print(grid[i][j], end=" ")
        print()

# myprint()
for t in range(1, turn + 1):
    # print("---",t,"---")
    # 1. 루돌프 이동
    ru_move()
    # print("루돌프 이동 후")
    # myprint()
    # 2. 산타 이동
    santa_move()
    # myprint()
    all_die = True
    for idx, santa in enumerate(santa_lst):
        if santa:
            score[idx] += 1
            all_die = False
    if all_die:
        break
    # print(santa_lst)
print(*score[1:])


########################################
# 메두사
'''
8 4
3 3 7 7
5 2 5 5 2 6 2 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

4 1
0 0 3 3
2 3
0 1 0 0
1 1 0 0
0 0 0 0
0 0 0 0
'''
from collections import deque

medusa_dict = {0: (7, 0, 1),
               1: (5, 4, 3),
               2: (7, 6, 5),
               3: (1, 2, 3)}
junsa_dict = {(0, -1): (7, 0), (0, 0): (0,), (0, 1): (0, 1),
              (1, -1): (5, 4), (1, 0): (4,), (1, 1): (4, 3),
              (2, -1): (7, 6), (2, 0): (6,), (2, 1): (6, 5),
              (3, -1): (1, 2), (3, 0): (2,), (3, 1): (2, 3)}

n, jn = map(int, input().split())
sr, sc, er, ec = map(int, input().split())
tmp = list(map(int, input().split()))
junsa_lst = []
for j in range(0, jn * 2, 2):
    jr, jc = tmp[j], tmp[j + 1]
    junsa_lst.append((jr, jc))
grid = [list(map(int, input().split())) for i in range(n)]
row = [-1, -1, 0, 1, 1, 1, 0, -1]
col = [0, 1, 1, 1, 0, -1, -1, -1]


def bfs():
    visited = [[False] * n for i in range(n)]
    visited[sr][sc] = True
    q = deque([(sr, sc, [])])
    while q:
        r, c, path = q.popleft()
        if (r, c) == (er, ec):
            return path
        for k in (0, 4, 6, 2):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or grid[nr][nc]:
                continue
            visited[nr][nc] = True
            q.append((nr, nc, path + [(nr, nc)]))
    return -1

def medusa_view(r, c, v):
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        for k in medusa_dict[v]:
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or view_grid[nr][nc]:
                continue
            view_grid[nr][nc] = 1
            q.append((nr, nc))


def junsa_view(jr, jc, v, booho):
    q = deque([(jr, jc)])
    while q:
        jr, jc = q.popleft()
        for k in junsa_dict[(v, booho)]:
            nr = jr + row[k]
            nc = jc + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or not view_grid[nr][nc]:
                continue
            view_grid[nr][nc] = 0
            q.append((nr, nc))


def booho(c, jc):
    if c - jc > 0:
        return -1
    elif c == jc:
        return 0
    else:
        return 1

path = bfs()  # -1 이면 -1 출력
if path == -1:
    print(-1)
else:
    for r, c in path:
        if (r, c) == (er, ec):
            print(0)
            break
        total_dist, total_doll, total_attack = 0, 0, 0
        # 1. 이동한 곳에 전사 위치
        for i in range(len(junsa_lst) - 1, -1, -1):
            jr, jc = junsa_lst[i]
            if (r, c) == (jr, jc):
                junsa_lst.pop(i)

        # 2. 메두사의 시선
        lst = []
        for v in range(4):  # v 방향
            view_grid = [[0] * n for i in range(n)]
            medusa_view(r, c, v)
            for jr, jc in junsa_lst:
                if view_grid[jr][jc]:
                    if v in (0, 1):
                        junsa_view(jr, jc, v, booho(c, jc))
                    else:
                        junsa_view(jr, jc, v, booho(r, jr))
            doll = 0
            for jr, jc in junsa_lst:
                if view_grid[jr][jc]:
                    doll += 1
            lst.append((-doll, v, view_grid))

        lst.sort()
        doll, v, view = lst[0]
        total_doll += abs(doll)

        # 3. 전사 이동 1
        for idx, junsa in enumerate(junsa_lst):
            jr, jc = junsa
            if view[jr][jc]:
                continue
            cur = abs(jr - r) + abs(jc - c)
            for k in (0, 4, 6, 2):
                nr = jr + row[k]
                nc = jc + col[k]
                next = abs(nr - r) + abs(nc - c)
                if 0 <= nr < n and 0 <= nc < n and not view[nr][nc] and next < cur:
                    total_dist += 1
                    junsa_lst[idx] = (nr, nc)
                    break
        # 4. 전사 이동 2
        for idx, junsa in enumerate(junsa_lst):
            jr, jc = junsa
            if view[jr][jc]:
                continue
            cur = abs(jr - r) + abs(jc - c)
            for k in (6, 2, 0, 4):
                nr = jr + row[k]
                nc = jc + col[k]
                next = abs(nr - r) + abs(nc - c)
                if 0 <= nr < n and 0 <= nc < n and not view[nr][nc] and next < cur:
                    total_dist += 1
                    junsa_lst[idx] = (nr, nc)
                    break

        # 5. 이동한 곳에 메두사 위치
        for i in range(len(junsa_lst) - 1, -1, -1):
            jr, jc = junsa_lst[i]
            if (r, c) == (jr, jc):
                junsa_lst.pop(i)
                total_attack += 1
        print(total_dist, total_doll, total_attack)
