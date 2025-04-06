'''
<<<<<<< HEAD
문제 설명
    1. 정민이는 상하좌우 이동하거나 게이트를 탄다
        그 후에 블랙홀이 한 칸씩 확산한다
    2. 블랙홀 확산도 q이긴 하다
    3. 정민이가 우주선에 도착해도 한 턴 기다려 줘야한다. q에 한번 더 넣어주기
    4. 게이트 좌표는 .. dict로 만들자
    5. 게이트 타면 3초 턴 먹는데 턴이면 q에 숫자를 넣어주지 뭐
        q에 차원,r,c,gate(3), end(1)

입력
    블랙홀 갯수, 정민 차원 nm , 우주선 차원 nm
    이동게이트 길이 ab
    정민 차원 게이트 시작 위치 rc
    우주선 차원 게이트 시작위치 rc
    블랙홀 정보 1이면 정민 2면 우주선
출력
    최단 시간 도달 못하면 hing
'''
=======
시간 비교해서 q에 넣어주기
'''
import heapq
>>>>>>> e66c5acebc845e6b91c3bd32666f6707f5ffc7f1
from collections import deque

b, n1, m1, n2, m2 = map(int, input().split())
x, y = map(int, input().split())
sr1, sc1 = map(int, input().split())
sr2, sc2 = map(int, input().split())
b1 = [[n1 * m1 + 1] * m1 for i in range(n1)]
b2 = [[n2 * m2 + 1] * m2 for i in range(n2)]
black_grid = [b1] + [b2]
b_q = deque()
for _ in range(b):
    h, br, bc = map(int, input().split())
    b_q.append((h - 1, br, bc, 0))


def black_bfs():
    while b_q:
        bh, br, bc, b_t = b_q.popleft()
        black_grid[bh][br][bc] = min(b_t, black_grid[bh][br][bc])
        if bh == 0:
            if (br, bc) == (n1 - 1, 0):
                if black_grid[bh][0][0] == n1 * m1 + 1:
                    b_q.append((bh, 0, 0, b_t + 1))
            elif br % 2 == 0 and bc + 1 < m1:
                if black_grid[bh][br][bc + 1] == n1 * m1 + 1:
                    b_q.append((bh, br, bc + 1, b_t + 1))
            elif br % 2 == 0 and bc + 1 >= m1:
                if black_grid[bh][br + 1][bc] == n1 * m1 + 1:
                    b_q.append((bh, br + 1, bc, b_t + 1))
            elif br % 2 == 1 and bc - 1 >= 0:
                if black_grid[bh][br][bc - 1] == n1 * m1 + 1:
                    b_q.append((bh, br, bc - 1, b_t + 1))
            elif br % 2 == 1 and bc - 1 < 0:
                if black_grid[bh][br + 1][bc] == n1 * m1 + 1:
                    b_q.append((bh, br + 1, bc, b_t + 1))
        else:
            if (br, bc) == (n2 - 1, 0):
                if black_grid[bh][0][0] == n2 * m2 + 1:
                    b_q.append((bh, 0, 0, b_t + 1))
            elif br % 2 == 0 and bc + 1 < m2:
                if black_grid[bh][br][bc + 1] == n2 * m2 + 1:
                    b_q.append((bh, br, bc + 1, b_t + 1))
            elif br % 2 == 0 and bc + 1 >= m2:
                if black_grid[bh][br + 1][bc] == n2 * m2 + 1:
                    b_q.append((bh, br + 1, bc, b_t + 1))
            elif br % 2 == 1 and bc - 1 >= 0:
                if black_grid[bh][br][bc - 1] == n2 * m2 + 1:
                    b_q.append((bh, br, bc - 1, b_t + 1))
            elif br % 2 == 1 and bc - 1 < 0:
                if black_grid[bh][br + 1][bc] == n2 * m2 + 1:
                    b_q.append((bh, br + 1, bc, b_t + 1))


black_bfs()

<<<<<<< HEAD
# for _ in black_grid:
#     print("-----------------")
#     for __ in _:
#         print(__)

TMP = []
map1 = [[0] * m1 for i in range(n1)]
map2 = [[0] * m2 for i in range(n2)]
v1 = [[int(1e9)] * m1 for i in range(n1)]
v2 = [[int(1e9)] * m2 for i in range(n2)]
=======
TMP = []
map1 = [[0] * m1 for i in range(n1)]
map2 = [[0] * m2 for i in range(n2)]
>>>>>>> e66c5acebc845e6b91c3bd32666f6707f5ffc7f1
tmp = []
for i in range(sr1, sr1 + x):
    for j in range(sc1, sc1 + y):
        map1[i][j] = 1  # gate
        tmp.append((0, i, j))
TMP.append(tmp)
tmp = []
for i in range(sr2, sr2 + x):
    for j in range(sc2, sc2 + y):
        map2[i][j] = 1  # gate
        tmp.append((1, i, j))
TMP.append(tmp)
gate_dict = {}

for j in range(len(TMP[0])):
    gate_dict[TMP[0][j]] = TMP[1][j]
    gate_dict[TMP[1][j]] = TMP[0][j]

grid = [map1] + [map2]
<<<<<<< HEAD
visited = [v1] + [v2]

sh, sr, sc = 0, 0, 0
eh, er, ec = 1, n2 - 1, m2 - 1
q = deque([(sh, sr, sc, 0)])  # 위치, 게이트 인지, 게이트 대기시간
=======
visited = [[[int(1e9)] * m1 for i in range(n1)]] + [[[int(1e9)] * m2 for i in range(n2)]]

sh, sr, sc = 0, 0, 0
eh, er, ec = 1, n2 - 1, m2 - 1
q = []
heapq.heappush(q, (0, sh, sr, sc))
>>>>>>> e66c5acebc845e6b91c3bd32666f6707f5ffc7f1
visited[sh][sr][sc] = 0
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

# for _ in grid:
#     print("-----------------")
#     for __ in _:
#         print(__)
ans = int(1e9)


<<<<<<< HEAD
=======
def is_range(nr, nc, h):
    if h == 0 and 0 <= nr < n1 and 0 <= nc < m1:
        return True
    if h == 1 and 0 <= nr < n2 and 0 <= nc < m2:
        return True


>>>>>>> e66c5acebc845e6b91c3bd32666f6707f5ffc7f1
def bfs():
    global ans

    while q:

<<<<<<< HEAD
        h, r, c, time = q.popleft()
=======
        time, h, r, c = heapq.heappop(q)
>>>>>>> e66c5acebc845e6b91c3bd32666f6707f5ffc7f1
        # print(h, r, c, time)
        if (h, r, c) == (eh, er, ec):
            if time < black_grid[eh][er][ec]:
                ans = min(ans, time)
<<<<<<< HEAD

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if h == 0:
                if not (0 <= nr < n1 and 0 <= nc < m1) or time >= black_grid[h][nr][nc]:
                    continue
                if grid[h][nr][nc] == 0:
                    if visited[h][nr][nc] > time + 1:
                        q.append((h, nr, nc, time + 1))
                        visited[h][nr][nc] = time + 1
                if grid[h][nr][nc] == 1:
                    if visited[h][nr][nc] > time + 1:
                        q.append((h, nr, nc, time + 1))
                        visited[h][nr][nc] = time + 1
                    nh, nr, nc = gate_dict[(h, nr, nc)]
                    if visited[nh][nr][nc] > time + 4:
                        q.append((nh, nr, nc, time + 4))
                        visited[nh][nr][nc] = time + 4
            if h == 1:
                if not (0 <= nr < n2 and 0 <= nc < m2) or time >= black_grid[h][nr][nc]:
                    continue
                if grid[h][nr][nc] == 0:
                    if visited[h][nr][nc] > time + 1:
                        q.append((h, nr, nc, time + 1))
                        visited[h][nr][nc] = time + 1
                if grid[h][nr][nc] == 1:
                    if visited[h][nr][nc] > time + 1:
                        q.append((h, nr, nc, time + 1))
                        visited[h][nr][nc] = time + 1
                    nh, nr, nc = gate_dict[(h, nr, nc)]
                    if visited[nh][nr][nc] > time + 4:
                        q.append((nh, nr, nc, time + 4))
                        visited[nh][nr][nc] = time + 4
=======
                return
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not is_range(nr, nc, h) or time >= black_grid[h][nr][nc]:
                continue
            if grid[h][nr][nc] == 0:
                if visited[h][nr][nc] > time + 1:
                    heapq.heappush(q, (time + 1, h, nr, nc))
                    visited[h][nr][nc] = time + 1
            if grid[h][nr][nc] == 1:
                if visited[h][nr][nc] > time + 1:
                    heapq.heappush(q, (time + 1, h, nr, nc))
                    visited[h][nr][nc] = time + 1
                nh, nr, nc = gate_dict[(h, nr, nc)]
                if visited[nh][nr][nc] > time + 4:
                    heapq.heappush(q, (time +4, nh, nr, nc))
                    visited[nh][nr][nc] = time + 4
>>>>>>> e66c5acebc845e6b91c3bd32666f6707f5ffc7f1


bfs()
if ans == int(1e9):
    print("hing...")
else:
    print(ans)
