'''
# 코드트리 청소는 즐거워
2025.04.02.수
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 1회 - > 녹화본 날라감 ㅠㅠ
    딕셔너리 열심히 만들기!!!!

  메모리 56 MB
  시간 397 ms

  회고
    1. 녹화 일시정지 한번 했었는데 녹화 중단하고 동영상 보려니까 맞는 코덱이 없다고 뜨네요 ㅜㅜ
    2. 룩업테이블 만들어서 중복되는 로직 줄여서 풀었다!

'''

# 녹화본이 날라갔어요 ,,
n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

r, c = n // 2, n // 2
d = 0
two, num, cnt = 0, 1, 0
location = []
row_ = [0, 1, 0, -1]
col_ = [-1, 0, 1, 0]
while not (r == 0 and c == 0):
    location.append((r, c, d))
    r += row_[d]
    c += col_[d]

    cnt += 1
    if cnt == num:
        cnt = 0
        two += 1
        d = (d + 1) % 4
    if two == 2:
        num += 1
        two = 0
# 0123
# 좌하우상
dir_dict = {0: ((-1, 1, -2, 2, 0, -1, 1, -1, 1, 0),
                (1, 1, 0, 0, -2, 0, 0, -1, -1, -1)),
            1: ((-1, -1, 0, 0, 2, 0, 0, 1, 1, 1),
                (-1, 1, -2, 2, 0, -1, 1, -1, 1, 0)),
            2: ((-1, 1, -2, 2, 0, -1, 1, -1, 1, 0),
                (-1, -1, 0, 0, 2, 0, 0, 1, 1, 1)),
            3: ((1, 1, 0, 0, -2, 0, 0, -1, -1, -1),
                (-1, 1, -2, 2, 0, -1, 1, -1, 1, 0))
            }
percent = [(1, 0, 1), (2, 2, 3), (5, 4), (7, 5, 6), (10, 7, 8)]
ans = 0
for r, c, d in location:
    nr = r + row_[d]  # 다음 청소할 곳.
    nc = c + col_[d]
    munji = grid[nr][nc]
    grid[nr][nc] = 0  # 청소햇슈유..
    spread = 0
    for i in range(5):
        p, range_ = percent[i][0], percent[i][1:]
        for _ in range_:
            row, col = dir_dict[d][0][_], dir_dict[d][1][_]
            if not (0 <= nr + row < n and 0 <= nc + col < n):
                spread += (munji * p) // 100
                ans += (munji * p) // 100
            else:
                grid[nr + row][nc + col] += (munji * p) // 100
                spread += (munji * p) // 100
    a = munji - spread
    if (0 <= nr + dir_dict[d][0][9] < n and 0 <= nc + dir_dict[d][1][9] < n):
        grid[nr + dir_dict[d][0][9]][nc + dir_dict[d][1][9]] += a
    else:
        ans += a

print(ans)

'''
# 백준 20057 마법사 상어와 토네이도
# 체감난이도 골4 인데 예시가 없어서 골3이 맞다.

# 문제 풀고 나서 기록

    문제 시작 15:50
    문제 종료 16:41
    총 풀이시간 51분
        50~53   : 문제 이해(3)
        53~55   : 문제 구상 및 초기 주석(2)
        55~02 : 달팽이 구현(7)
                (중앙 ->0,0)으로 가는거 잘 모르겠어서 0,0에서부터 갔음

                1차 디버깅
                달팽이 잘 안돼서 보니까 while r != n // 2 and c != n // 2: 여서 2개밖에 안들어감
                -> or이 맞음 not(r==c==n//2) 니까.
        02~28 : 토네이도 1차 구현(26)
                1. 방향 확인하려면 달팽이에서 방향 넣어줘야하는거 깨닫고 방향 넣어줌!
                근데 d가 아니라 꺼꾸로 달팽이라 d+2 로 넣어줌
                2. 회전시켜야 하는게 생각이 안나서 일단 d ==2 일때 구현했음
                 그리고 퍼센트마다 방향을 설정해줘야해서 row2, col2를 만듬
                3. 1~10% , a의 로직 설계
                4. 왼쪽으로 갈 때는 잘 되는거 확인!
        28~40 : 토네이도 2차구현(12)
                d = 0,1,3 일때를 처리하기 위해 각 방향별 퍼센트 방향을 담는 dict 를 만들어줌
                혹시라도 잘못 쓰면 디버깅도 안될 것 같아서 이때 엄청 꼼꼼히봤다.......... dirs만 10분동안 만듬
        40~42 : 테케 확인!(2)
                헷갈렸던 점은 혹시 0,0에 다다라서도 뿌리나? 해서
                location에 0,0을 넣어보고돌려봄 ->테케 틀리게나옴
                다시 제외하고 제출!


    메모리 150996 KB
    시간 (첫코드 328ms, 두번째 코드 348ms)

    회고
    1. 중앙 -> 0,0으로 가는 달팽이로 다시 풀어보기!!!!! 꼭!!!
    2. 내 코드는 까딱하면 디버깅으로 한 세월 보낼 코드...... 남들 코드 이해하기!!!!!!!!
    3. 최적화 하고 내지.. 머가 그리 급하다고.... 하드코딩을 줄이자!!!!!!!!!!!!

# 문제 풀면서의 기록
문제설명
    토네이도가 중심점에서 0,0을 향해 회전한다.
    이동하는 매 칸마다 모래가 흩뿌려진다.
    이때 격자 밖으로 나가는 모래양의 합은?
구상
    성실히 구현.....
    1. 일단 달팽이 구현 -> 중앙에서 들어가는게 어려워서 0,0에서 시작해서 중앙으로 가는 좌표 담기.
    2. 그다음에 흩뿌려지는거 구현
    3. 그다음에 회전 구현 -> 은 안했다.
'''
######################################################################
# 두번째 풀이(코드최적화: 시간은 아니고 dict 사용)
n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

# [1] 달팽이 구현

r, c, d = 0, 0, 0
location = []
row = [0, 1, 0, -1]  # 달팽이용 row, col
col = [1, 0, -1, 0]
visited = [[0] * n for i in range(n)]
visited[0][0] = 1
while r != n // 2 or c != n // 2:  # 0,0 에서 시작해서 중앙으로 들어가면서 위치와 좌표를 담아준다.
    if not (0 <= r + row[d] < n and 0 <= c + col[d] < n) or visited[r + row[d]][c + col[d]]:
        d = (d + 1) % 4
    nr = r + row[d]
    nc = c + col[d]
    visited[nr][nc] = 1
    r = nr
    c = nc
    location.append((r, c, (d + 2) % 4))  # 180도 회전한걸 담아줘야함! 내가 꺼꾸로 달팽이라서!

# [2] 토네이도 구현

dirs = {  # 토네이도용 방향좌표
    0: [(-1, 1, -2, 2, 0, -1, 1, -1, 1, 0), (-1, -1, 0, 0, 2, 0, 0, 1, 1, 1)],  # 우
    1: [(-1, -1, 0, 0, 2, 0, 0, 1, 1, 1), (-1, 1, -2, 2, 0, -1, 1, -1, 1, 0)],  # 아래
    2: [(-1, 1, -2, 2, 0, -1, 1, -1, 1, 0, 0), (1, 1, 0, 0, -2, 0, 0, -1, -1, -1, -1)],  # 왼
    3: [(1, 1, 0, 0, -2, 0, 0, -1, -1, -1), (-1, 1, -2, 2, 0, -1, 1, -1, 1, 0)]}  # 위
munji_list = {1: (0, 1), 2: (2, 3), 5: (4,), 7: (5, 6), 10: (7, 8)}  # 해당하는 위치 인덱스 지정
out = 0

while location:
    r, c, d = location.pop()
    nr = r + row[d]  # nr,nc 근방으로
    nc = c + col[d]
    origin_mungi = grid[nr][nc]
    a = origin_mungi
    for m in (1, 2, 5, 7, 10):
        munji = origin_mungi * m // 100
        for k in munji_list[m]:
            nnr = nr + dirs[d][0][k]
            nnc = nc + dirs[d][1][k]
            if not (0 <= nnr < n and 0 <= nnc < n):
                out += munji
                a -= munji
            else:
                grid[nnr][nnc] += munji
                a -= munji
    # a 계산.
    grid[nr][nc] = 0  # 이동했다.
    anr = nr + dirs[d][0][9]
    anc = nc + dirs[d][1][9]
    if not (0 <= anr < n and 0 <= anc < n):
        out += a
    else:
        grid[anr][anc] += a

print(out)
######################################################################
# 첫번째 풀이
'''
문제설명
    토네이도가 중심점에서 0,0을 향해 회전한다.
    이동하는 매 칸마다 모래가 흩뿌려진다.
    이때 격자 밖으로 나가는 모래양의 합은?
구상
    성실히 구현.....
    1. 일단 달팽이 구현 -> 중앙에서 들어가는게 어려워서 0,0에서 시작해서 중앙으로 가는 좌표 담기.
    2. 그다음에 흩뿌려지는거 구현
    3. 그다음에 회전 구현
'''
n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

r, c, d = 0, 0, 0
location = []
row = [0, 1, 0, -1]
col = [1, 0, -1, 0]
# 위 3 아래 1 왼 2 우 0
dirs = [
    [(-1, 1, -2, 2, 0, -1, 1, -1, 1, 0), (-1, -1, 0, 0, 2, 0, 0, 1, 1, 1)],
    [(-1, -1, 0, 0, 2, 0, 0, 1, 1, 1), (-1, 1, -2, 2, 0, -1, 1, -1, 1, 0)],
    [(-1, 1, -2, 2, 0, -1, 1, -1, 1, 0, 0), (1, 1, 0, 0, -2, 0, 0, -1, -1, -1, -1)],
    [(1, 1, 0, 0, -2, 0, 0, -1, -1, -1), (-1, 1, -2, 2, 0, -1, 1, -1, 1, 0)]
]

visited = [[0] * n for i in range(n)]
visited[0][0] = 1
while r != n // 2 or c != n // 2:
    if not (0 <= r + row[d] < n and 0 <= c + col[d] < n) or visited[r + row[d]][c + col[d]]:
        d = (d + 1) % 4
    nr = r + row[d]
    nc = c + col[d]
    visited[nr][nc] = 1
    r = nr
    c = nc
    location.append((r, c, (d + 2) % 4))
# 위 3 아래 1 왼 2 우 0
out = 0
while location:
    r, c, d = location.pop()
    nr = r + row[d]
    nc = c + col[d]
    # nr,nc 근방으로
    origin_mungi = grid[nr][nc]
    # 1%
    # 11(01) 22(23) 5(4) 77(56) 10(78)
    munji = origin_mungi * 1 // 100
    for k in (0, 1):
        nnr = nr + dirs[d][0][k]
        nnc = nc + dirs[d][1][k]
        if not (0 <= nnr < n and 0 <= nnc < n):
            out += munji
        else:
            grid[nnr][nnc] += munji
    # 2%
    munji = origin_mungi * 2 // 100
    for k in (2, 3):
        nnr = nr + dirs[d][0][k]
        nnc = nc + dirs[d][1][k]
        if not (0 <= nnr < n and 0 <= nnc < n):
            out += munji
        else:
            grid[nnr][nnc] += munji
    # 5%
    munji = origin_mungi * 5 // 100
    for k in (4,):
        nnr = nr + dirs[d][0][k]
        nnc = nc + dirs[d][1][k]
        if not (0 <= nnr < n and 0 <= nnc < n):
            out += munji
        else:
            grid[nnr][nnc] += munji
    # 7%
    munji = origin_mungi * 7 // 100
    for k in (5, 6):
        nnr = nr + dirs[d][0][k]
        nnc = nc + dirs[d][1][k]
        if not (0 <= nnr < n and 0 <= nnc < n):
            out += munji
        else:
            grid[nnr][nnc] += munji
    # 10%
    munji = origin_mungi * 10 // 100
    for k in (7, 8):
        nnr = nr + dirs[d][0][k]
        nnc = nc + dirs[d][1][k]
        if not (0 <= nnr < n and 0 <= nnc < n):
            out += munji
        else:
            grid[nnr][nnc] += munji
    # a
    a = origin_mungi - (origin_mungi * 1 // 100) * 2 - (origin_mungi * 2 // 100) * 2 - \
        (origin_mungi * 5 // 100) * 1 - (origin_mungi * 7 // 100) * 2 - (origin_mungi * 10 // 100) * 2

    grid[nr][nc] = 0
    anr = nr + dirs[d][0][9]
    anc = nc + dirs[d][1][9]
    if not (0 <= anr < n and 0 <= anc < n):
        out += a
    else:
        grid[anr][anc] += a

print(out)
