'''
문제시작 15:20 ~ 17:12

문제 설명
    통나무를 최소횟수로 옮긴다.
    불가능하면 0
구상
    q로 관리.
틀린이유
    회전로직에서 minC+3 까지 봐줘야하는데 그게 틀렷음
'''
from collections import deque

n = int(input())
grid = [list(input()) for i in range(n)]

sr1, sc1, sr2, sc2, sr3, sc3 = -1, -1, -1, -1, -1, -1
er1, ec1, er2, ec2, er3, ec3 = -1, -1, -1, -1, -1, -1

row = [0, 1, 0, -1]
col = [1, 0, -1, 0]


def find_b():
    global sr1, sc1, sr2, sc2, sr3, sc3
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "B":
                sr1, sc1 = i, j
                for k in range(2):
                    nr = i + row[k]
                    nc = j + col[k]
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == "B":
                        sr2, sc2, sr3, sc3, = nr, nc, nr + row[k], nc + col[k]
                        grid[sr1][sc1], grid[sr2][sc2], grid[sr3][sc3] = '0', '0', '0'
                        return


def find_e():
    global er1, ec1, er2, ec2, er3, ec3
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "E":
                er1, ec1 = i, j
                for k in range(2):
                    nr = i + row[k]
                    nc = j + col[k]
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == "E":
                        er2, ec2, er3, ec3 = nr, nc, nr + row[k], nc + col[k]
                        grid[er1][ec1], grid[er2][ec2], grid[er3][ec3] = '0', '0', '0'
                        return

find_b()
find_e()


def is_range(nr1, nc1, nr2, nc2, nr3, nc3):
    if 0 <= nr1 < n and 0 <= nc1 < n and 0 <= nr2 < n and 0 <= nc2 < n and 0 <= nr3 < n and 0 <= nc3 < n:
        return True
    return False


def is_not_one(nr1, nc1, nr2, nc2, nr3, nc3):
    if grid[nr1][nc1] == '0' and grid[nr2][nc2] == '0' and grid[nr3][nc3] == '0':
        return True
    return False


def is_rotate(r1, c1, r2, c2, r3, c3):
    if (r1 == r2 == r3):
        # 이거면 통나무가 가로로 놓여있음
        minC = min(c1, c2, c3)
        for r in range(r1 - 1, r1 + 2):
            for c in range(minC, minC + 3): # 아 이게 틀렸네 +3 까지 봐줘야함.
                if not (0 <= r < n and 0 <= c < n):
                    return False
                if grid[r][c] == '1':
                    return False
        return True
    else:  # 이거면 통나무가 세로로
        minR = min(r1, r2, r3)
        for r in range(minR, minR + 3):
            for c in range(c1 - 1, c1 + 2):
                if not (0 <= r < n and 0 <= c < n):
                    return False
                if grid[r][c] == '1':
                    return False
        return True


def myprint(r1, c1, r2, c2, r3, c3, cnt):
    print("========", cnt, "========")
    for i in range(n):
        for j in range(n):
            if (i, j) in {(r1, c1), (r2, c2), (r3, c3)}:
                print("O", end=" ")
            else:
                print("X", end=" ")
        print()


def bfs():
    global ans
    q = deque([(sr1, sc1, sr2, sc2, sr3, sc3, 0)])
    visited = set()
    visited.add((sr1, sc1, sr2, sc2, sr3, sc3))

    while q:
        r1, c1, r2, c2, r3, c3, cnt = q.popleft()
        # myprint(r1, c1, r2, c2, r3, c3, cnt)
        # print((r1, c1), (r2, c2), (r3, c3), cnt)
        if (r1, c1) == (er1, ec1) and (r2, c2) == (er2, ec2) and (r3, c3) == (er3, ec3):
            ans = cnt
            return

        for k in range(4):
            nr1, nc1 = r1 + row[k], c1 + col[k]
            nr2, nc2 = r2 + row[k], c2 + col[k]
            nr3, nc3 = r3 + row[k], c3 + col[k]

            if is_range(nr1, nc1, nr2, nc2, nr3, nc3) and is_not_one(nr1, nc1, nr2, nc2, nr3, nc3) and (
                    nr1, nc1, nr2, nc2, nr3, nc3) not in visited:
                q.append((nr1, nc1, nr2, nc2, nr3, nc3, cnt + 1))
                visited.add((nr1, nc1, nr2, nc2, nr3, nc3))
        if is_rotate(r1, c1, r2, c2, r3, c3):
            # 회전 가능하면 회전.
            # r2,c2를 1,1로 만들어주기
            minus_r = r2 - 1
            minus_c = c2 - 1
            nr1, nr2, nr3 = r1 - minus_r, r2 - minus_r, r3 - minus_r
            nc1, nc2, nc3 = c1 - minus_c, c2 - minus_c, c3 - minus_c
            # 회전
            nr1, nr2, nr3, nc1, nc2, nc3 = 3 - nc1 - 1, 3 - nc2 - 1, 3 - nc3 - 1, nr1, nr2, nr3
            nr1, nr2, nr3 = nr1 + minus_r, nr2 + minus_r, nr3 + minus_r # 원상복구
            nc1, nc2, nc3 = nc1 + minus_c, nc2 + minus_c, nc3 + minus_c

            # 오름차순으로 바꿔주기,,;;
            tmp = [(nr1, nc1), (nr2, nc2), (nr3, nc3)]
            tmp.sort()
            nr1, nc1, nr2, nc2, nr3, nc3 = tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1], tmp[2][0], tmp[2][1]
            if (nr1, nc1, nr2, nc2, nr3, nc3) not in visited:
                q.append((nr1, nc1, nr2, nc2, nr3, nc3, cnt + 1))
                visited.add((nr1, nc1, nr2, nc2, nr3, nc3))



ans = 0
bfs()
print(ans)
