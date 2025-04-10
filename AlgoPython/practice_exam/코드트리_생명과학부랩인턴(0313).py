'''
3회차
한번에 가보자이
규칙성 2*(r/c-1)

승용이가 채취한 곰팡이 사이즈 합 출력
'''

n, m, vn = map(int, input().split())
grid = [[0] * m for i in range(n)]
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
change = [1, 0, 3, 2]
for v in range(vn):
    r, c, s, d, b = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1
    if d in (0, 1):
        grid[r][c] = (s % (2 * (n - 1)), d, b)
    else:
        grid[r][c] = (s % (2 * (m - 1)), d, b)
ans = 0


# 1. 승용이 열 탐색
def myprint():
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                print(grid[i][j][2], end=" ")
            else:
                print(0, end=" ")
        print()


for j in range(m):

    # 2. 가장 빨리 발견하는 곰팡이 채취
    for i in range(n):
        if grid[i][j]:
            ans += grid[i][j][2]
            grid[i][j] = 0
            break
    # 3. 곰팡이 이동 -> new_grid 필요
    new_grid = [[0] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                s, d, b = grid[i][j]
                r, c = i, j
                for ss in range(s):
                    nr = r + row[d]
                    nc = c + col[d]
                    if not (0 <= nr < n and 0 <= nc < m):
                        d = change[d]
                    nr = r + row[d]
                    nc = c + col[d]
                    r = nr
                    c = nc

                if not new_grid[r][c]:
                    new_grid[r][c] = (s, d, b)
                else:
                    if new_grid[r][c][2] < b:
                        new_grid[r][c] = (s, d, b)

    grid = new_grid

print(ans)


'''
# 코드트리 생명과학부랩인턴
2025.04.04.금
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 14:07
    문제 종료 19:58

    총 풀이시간 47분
        07~16   : 문제 이해 및 구상(9)
        16~54   : 로직 작성(38)
                    원래는 visited를 사용해서 new_grid 없이 하려고 했는데 잘 안돼서 변경했다.

  메모리 29 MB
  시간 344 ms

s를 2(r-1) 로 나눈 나머지로 변환
'''
n, m, virus = map(int, input().split())
grid = [[0] * m for i in range(n)]
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
change_d = [1, 0, 3, 2]
for v in range(virus):
    r, c, s, d, size = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1
    if d in (0, 1):
        s %= 2 * (n - 1)
    else:
        s %= 2 * (m - 1)
    grid[r][c] = (v, s, d, size)

eat = 0


def myprint(grid):
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                print(grid[i][j][3], end=" ")
            else:
                print(0, end=" ")
        print()


# print("------------시작-----------------")
# myprint(grid)
for j in range(m):
    # 1. 곰팡이 채취
    for i in range(n):
        if grid[i][j]:
            eat += grid[i][j][3]
            grid[i][j] = 0
            break
    # print(eat)
    # print("------------먹고난 후-----------------",j)
    # myprint(grid)
    # 2. 곰팡이 이동
    new_grid = [[0] * m for i in range(n)]
    for ii in range(n):
        for jj in range(m):
            if grid[ii][jj]:
                num, s, d, size = grid[ii][jj]
                r, c = ii, jj
                for ss in range(s):
                    nr = r + row[d]
                    nc = c + col[d]
                    if not (0 <= nr < n and 0 <= nc < m):
                        d = change_d[d]
                    nr = r + row[d]
                    nc = c + col[d]
                    r = nr
                    c = nc
                if not new_grid[r][c]:
                    new_grid[r][c] = (num, s, d, size)
                else:
                    if new_grid[r][c][3] < size:
                        new_grid[r][c] = (num, s, d, size)

    # print("------------이동 후-----------------")
    # myprint(new_grid)
    grid = new_grid

print(eat)
#################################################################
# 두번째 풀이 : 시간은 기나 더 간단함
n, m, virus_num = map(int, input().split())  # 맵 크기와 곰팡이 수
grid = [[() for i in range(m)] for i in range(n)]
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
for v in range(virus_num):
    r, c, s, d, b = map(int, input().split())  # 위치, 속력, 방향, 크기
    if d in (1, 2):
        grid[r - 1][c - 1] = (b, d - 1, s % (2 * (n - 1)))  # 크기, 방향, 속력 순으로 넣는다
    else:
        grid[r - 1][c - 1] = (b, d - 1, s % (2 * (m - 1)))
move = {0: 1, 1: 0, 2: 3, 3: 2}
jdx = eat = 0
while jdx < m:  # 승용이 움직임
    for i in range(n):
        if grid[i][jdx]:  # 곰팡이 있으면
            eat += grid[i][jdx][0]  # 크기만큼 먹는다
            grid[i][jdx] = ()  # 비었다!
            break
    # 2. 움직인다.
    move_list = []
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                virus = grid[i][j]
                b, d, s = virus[0], virus[1], virus[2]  # 크기, 방향, 속력
                grid[i][j] = ()
                r, c = i, j
                for ss in range(s):
                    nr = r + row[d]
                    nc = c + col[d]
                    if not (0 <= nr < n and 0 <= nc < m):
                        d = move[d]
                        nr = r + row[d]
                        nc = c + col[d]
                    r = nr
                    c = nc
                move_list.append((r, c, b, d, s))
    for r, c, b, d, s in move_list:
        if not grid[r][c]:
            grid[r][c] = (b, d, s)
        else:
            if b > grid[r][c][0]:
                grid[r][c] = (b, d, s)
    jdx += 1  # 다음 칸 탐색
print(eat)
#################################################################
# 첫 풀이

n, m, virus_num = map(int, input().split())  # 맵 크기와 곰팡이 수
grid = [[[] for i in range(m)] for i in range(n)]
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
for v in range(virus_num):
    r, c, s, d, b = map(int, input().split())  # 위치, 속력, 방향, 크기
    if d in (1, 2):  # 위 아래
        grid[r - 1][c - 1].append((b, d - 1, s % (2 * (n - 1))))  # 크기, 방향, 속력 순으로 넣는다
    else:
        grid[r - 1][c - 1].append((b, d - 1, s % (2 * (m - 1))))

move = {0: 1, 1: 0, 2: 3, 3: 2}
jdx = 0
eat = 0
while jdx < m:  # 승용이 움직임
    # 1. 누구 먹을래
    for i in range(n):
        if grid[i][jdx]:  # 곰팡이 있으면
            eat += grid[i][jdx][0][0]  # 크기만큼 먹는다
            grid[i][jdx] = []  # 비었다!
            break
    # 2. 움직인다.
    new_grid = [[[] for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                for w in range(len(grid[i][j]) - 1, -1, -1):
                    virus = grid[i][j][w]
                    b, d, s = virus[0], virus[1], virus[2]  # 크기, 방향, 속력
                    nr = i + row[d] * s
                    nc = j + col[d] * s
                    if d in (0, 1):
                        size = 2 * (n - 1)
                        nr = (nr + size) % size
                        if nr >= n:
                            nr = size - nr
                            d = move[d]
                    elif d in (2, 3):
                        size = 2 * (m - 1)
                        nc = (nc + size) % size
                        if nc >= m:
                            nc = size - nc
                            d = move[d]
                    new_grid[nr][nc].append((b, d, s))
                    # grid[i][j].pop(w)
    # 3-0. sort 하고
    for i in range(n):
        for j in range(m):
            if new_grid[i][j]:
                new_grid[i][j].sort(reverse=True)
    # 3-1. 겹치는 애들 검사
    for i in range(n):
        for j in range(m):
            if len(new_grid[i][j]) >= 2:
                new_grid[i][j] = [new_grid[i][j][0]]
    grid = new_grid
    jdx += 1  # 다음 칸 탐색

print(eat)
