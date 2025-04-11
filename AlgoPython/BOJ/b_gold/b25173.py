'''
씩 패딩을 준다.
주변은 9 6칸씩 벽으로 패딩
'''
from collections import deque

n, m = map(int, input().split())
dongul = n * m
maxnm = max(n, m) - 1
grid = [[9] * (m + maxnm * 2) for i in range(maxnm)] + [[9] * maxnm + list(map(int, input().split())) + [9] * maxnm for
                                                        i in range(n)] + [[9] * (m + maxnm * 2) for i in range(maxnm)]

n += maxnm * 2
m += maxnm * 2

ari_hp, ari_power, boss_hp, boss_power = map(int, input().split())

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


def find():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 3:
                br, bc = i, j
                grid[i][j] = 0
                for k in range(4):
                    nr = i + row[k]
                    nc = j + col[k]
                    if grid[nr][nc] == 2:
                        grid[nr][nc] = 0
                        bd = k
                        ar, ac, ad = nr, nc, k
                        return ar, ac, ad, br, bc, bd


ar, ac, ad, br, bc, bd = find()


def find_suksoon():
    r, c, d = br, bc, bd  # 보스 위치, 방향
    ele = 0  # ele 가 dongul 이 될 떄 까지...
    cnt, two, num = 0, 0, 1
    while ele != dongul:
        if grid[r][c] == 1:  # 석순 발견!!!
            return r, c
        if grid[r][c] < 9:
            ele += 1  # 동굴  탐험

        r += row[d]
        c += col[d]

        cnt += 1
        if cnt == num:
            d = (d + 1) % 4
            cnt = 0
            two += 1
        if two == 2:
            two = 0
            num += 1

    return -1, -1


def suksoon_bfs(sr, sc, ar, ac):
    visited = [[False] * m for i in range(n)]
    visited[sr][sc] = True
    q = deque([(sr, sc, 0)])
    while q:
        r, c, cnt = q.popleft()
        if (r, c) == (ar, ac):
            return cnt
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if grid[nr][nc] == 0 and not visited[nr][nc] and (nr, nc) != (br, bc):  # 보스 위치도 안댐.
                visited[nr][nc] = True
                q.append((nr, nc, cnt + 1))

    return -1


while True:
    # 1. 아리 공격
    boss_hp -= ari_power  # 죽었나 검사하기
    if boss_hp <= 0:
        print("VICTORY!")
        break
    before_ar, before_ac = ar, ac
    # 2. 아리 이동 : 0 인 곳으로만 이동 가능
    nad = ad
    minus = 0
    move = False
    for k in range(4):
        nar = ar + row[nad]
        nac = ac + col[nad]
        if grid[nar][nac] == 0 and (nar, nac) != (br, bc):
            ad = nad
            minus = k
            move = True
            break
        else:
            nad = (nad + 1) % 4
    if move:
        ari_hp -= minus  # 죽는거 검사
        if ari_hp <= 0:
            print("CAVELIFE...")
            break
        ar = ar + row[ad]
        ac = ac + col[ad]
    else:
        ari_hp -= 4  # 혹시 이거..? 장난하나 ''''''''''''''''''''''''''''''''''''''
        if ari_hp <= 0:
            print("CAVELIFE...")
            break
    # 3. 보스 석순 찾기..
    sr, sc = find_suksoon()
    if (sr, sc) != (-1, -1):
        # 공격 시작
        # print(sr, sc)
        dist = suksoon_bfs(sr, sc, ar, ac)
        if dist != -1:
            if boss_power - dist > 0:
                ari_hp -= boss_power - dist  # 죽는지 검사
                if ari_hp <= 0:
                    print("CAVELIFE...")
                    break
    # 4. 보스 이동
    if move:  # 아리가 움직였다면.
        br, bc = before_ar, before_ac
        bd = ad
