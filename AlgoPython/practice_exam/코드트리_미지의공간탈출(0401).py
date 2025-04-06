'''
# 체감난이도 플1

# 문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 09:00
    문제 종료 10:47

    총 풀이시간 107분
        00~06   : 문제 이해 및 손코딩(6)
        06~08   : 손코딩 기반 초기 주석 및 필요한 변수/함수 세분화(2)
        08~10   : 입력 받기(2)
        10~20   : 시간 이상 현상 로직(10)
                    (1)
                    시간 이상 시작점들은 0초부터 시작인지 배수초부터 시작인지 헷갈림
                    문제 예시 보면 2배수 시간 이상 지점을 피해가는 걸 볼 수 있고
                    14 0
                    ↑
                    여기를 못가는 거라서 0초부터 시작인걸로!
                    (2)
                    시간 이상은 겹쳐질 수 있으므로 2차원 배열에서 3차원 배열 수정
        20~38   : 필요한 좌표찾기(18)
                    3차원 탈출구 찾는게 어려웠음...
                    각 방향마다 탈출구 잘 찾았는지 확인해야겠다 라고 생각
        38~58   : 3차원 bfs 작성(20)
                    좌표 범위 벗어날 때 처리가 진짜 머리아팠다.
                    큐빙했을 때를 기억하며...... 정신 붙들고 했음
        58~00   : 3차원 bfs 확인(2)
                    bfs가 none 값을 뱉어내네요 디버깅 시작
                    (1)
                    nr <= 0
                    이렇게 되어있어서 죄다 면이동 해버림
                    nr < 0 수정!
                    (2)
                    답은 8이 잘 나오는데
                    디버깅용 path를 찍어봤는데
                    어? 내가 어느 순간부터 동-서를 바꿔서 한 것 같은거임? 하.........오마이갓........
        00~13   : 동-서 헷갈린 것 같아서 좌표 재확인(13)
                    3차원 bfs 좌표 변환하는거 다시 짰음.ㅎ
        13~18   : 2차원 bfs 작성(5)
        18~20   : 2차원 bfs 확인(2)
                    테케 -1 나와서 디버깅
                    (1) 변수 오타 수정
                        sc3 - > sc2 : 내 이럴 줄 알았다.
                    (2) 1만 못가는게 아니라 3도 못간다 조건 추가!
                    (3) (0 <= nr < m and 0 <= nc < m)
                        m으로 되어있어서 n으로 변경!
                    -> 답 나오는 거 확인
        20~47   : 검증 시작(27)
                    (1) 2차원 bfs에서 시간이상현상 잘 검사하는지 디버거로 확인
                        (13초일 때 14초 칸 못가는지 확인)

                    (2) 시간 이상 현상이 2차원 시작점을 점령해버려서 -1 되는지 확인

                    (3) 탈출구 동서남북 방향마다 확인

                        어래레? 남쪽 탈출구 테케에서 3차원 bfs에서 none 을 return함
                        -> 3차원 탈출구가 잘못됐음!! 좌표 계산 확인
                        남 , 북을 반대로 했네 수정!

                        그래도 none을 return함
                        아 내가 실수한게 아니라
                        내가 넣은 테케가 3차원 cube에서 아예 3차원 탈출구로 가지 못하는 경우였음!
                        -1 return 하게 수정!

  메모리 17 MB
  시간 55 ms

    회고
        1. 시간이상현상 배열을 처음엔 2차원 배열로 하려고 했는데
            한 좌표에서 겹칠 수도 있겠다 해서 3차원으로 변경
            근데 생각해보면 2차원 배열로 하고 가장 작은값으로만 유지되게 해주면됨. -> 해보기
        2. 왤케 동/서 헷갈려하는지 모르겠다 그것 때문에 좌표 수정 엄청 많이함
            이런 문제 나오면 정신 꽉 붙잡고 하기......
        3. "변수명 확인 잘해라" <- 적었는데 진짜 오타찾음
        4. 어려워...........................................................ㅠㅠㅠㅠ
            하드코딩하면 정신 정신 정신!!! 붙잡기!!!!!!!!

# 문제 풀면서의 기록
문제 설명
    1. 시간 이상
        시간 이상은 3차원 배열로 미리 만들어 놓기.
    2. 이동 bfs
        (1) 3차원 탈출
        (2) 2차원 탈출
            -> 탈출구를 찾는게 관건...

필요한 변수
cube = [h,r,c] : 면과 좌표
grid = [r,c] : 좌표

필요한 함수
bfs3 : 3차원
bfs2 : 2차원

시간 이상이 좀 헷갈리네. bfs 작성 후 보완하기
변수명 확인 잘해라
3차원 탈출구 찾는거 엣지케이스 넣어봐라

시간 이상때문에 -1 되는지
8 3 3
4 0 0 0 0 0 0 0
0 1 1 1 1 1 0 0
0 1 3 3 3 1 0 1
0 1 3 3 3 1 0 1
0 1 3 3 3 0 0 0
0 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1
1 1 1
0 0 0
0 1 1
1 1 1
1 0 1
1 1 1
0 0 1
1 0 0
1 0 1
0 0 0
1 0 0
1 1 1
2 0 0
0 1 0
0 0 0
0 7 1 14
6 3 3 2
4 7 1 1




다른 면일 때 확인 (북쪽)
8 3 2
4 0 0 0 0 0 0 0
0 1 1 1 1 1 0 0
0 1 3 3 3 1 0 1
0 1 3 3 3 1 0 1
0 1 3 3 3 1 0 0
0 1 1 0 1 1 1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1
1 1 1
0 0 0
0 1 1
1 1 1
1 0 1
1 1 1
0 0 1
1 0 0
1 0 1
0 0 0
1 0 0
1 1 1
2 0 0
0 1 0
0 0 0
0 7 1 14
6 3 3 2






8 3 2
4 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0
0 0 0 0 1 3 3 3
0 0 0 0 1 3 3 3
0 0 0 0 1 3 3 3
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 2
7 0 1 100
7 0 1 100



8 3 2
4 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 1 0 1 1
0 0 0 0 1 3 3 3
0 0 0 0 1 3 3 3
0 0 0 0 1 3 3 3
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 2
7 0 1 100
7 0 1 100




8 4 2
4 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 1 1 0 1 1 1 0
0 1 3 3 3 3 1 0
0 1 3 3 3 3 1 0
0 1 3 3 3 3 1 0
0 1 3 3 3 3 1 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 2
7 7 1 100
7 7 1 100






8 3 2
4 0 0 0 0 0 0 0
0 1 1 1 1 1 0 0
0 1 3 3 3 1 0 1
0 1 3 3 3 1 0 1
0 1 3 3 3 0 0 0
0 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1
0 0 0
0 1 1
1 1 1
1 0 1
1 1 1
0 0 1
1 0 0
1 0 1
0 0 0
1 0 0
1 1 1
2 0 0
0 1 0
0 0 0
7 0 0 14
7 7 1 2
'''
# --------------------------------- 입력, 좌표찾기 ---------------------------------

from collections import deque

n, m, time_attack_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
cube = []
for _ in range(5):
    tmp = [list(map(int, input().split())) for i in range(m)]
    cube.append(tmp)

row = [0, 0, 1, -1]
col = [1, -1, 0, 0]

sh3, sr3, sc3 = -1, -1, -1  # 3차원 시작점
eh3, er3, ec3 = -1, -1, -1  # 3차원 탈출구
sr2, sc2 = -1, -1,  # 2차원 시작점
er2, ec2 = -1, -1  # 2차원 탈출구


def find():  # 3 시작 위치 찾기
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 3:
                return i, j


startx, starty = find()

for i in range(n):  # 2차원 목적지 찾기
    for j in range(n):
        if grid[i][j] == 4:
            er2, ec2 = i, j

for h in range(5):  # 3차원 시작점 찾기
    for i in range(m):
        for j in range(m):
            if cube[h][i][j] == 2:
                sh3, sr3, sc3 = h, i, j

for i in range(n):  # 2차원 시작점, 3차원 목적지 찾기
    for j in range(n):
        if grid[i][j] == 3:
            for k in range(4):
                nr = i + row[k]
                nc = j + col[k]
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    sr2, sc2 = nr, nc  # 2차원 시작점
                    # 이제 3차원 목적지 찾기
                    eh3 = k  # k가 면 idx가 될거임.
                    er3 = m - 1  # r은 무조건 2임.
                    if k == 0:  # 동
                        ec3 = m - 1 - (nr - startx)
                    elif k == 1:  # 서
                        ec3 = nr - startx
                    elif k == 2:  # 남
                        ec3 = nc - starty
                    elif k == 3:  # 북.
                        ec3 = m - 1 - (nc - starty)
                    break

# ---------------------- 시간 이상 2차원 배열 만들기 ----------------------
time_attack = [[1000 * 20 + 1] * n for i in range(n)]
time_info = [list(map(int, input().split())) for i in range(time_attack_num)]
for tr, tc, td, tv in time_info:
    v = tv
    time_attack[tr][tc] = 0

    for k in range(n):
        ntr = tr + row[td]
        ntc = tc + col[td]
        if not (0 <= ntr < n and 0 <= ntc < n) or grid[ntr][ntc]:
            break
        time_attack[ntr][ntc] = min(tv, time_attack[ntr][ntc])
        tv += v
        tr = ntr
        tc = ntc


# --------------------------------- 함수 ---------------------------------
def bfs3(sh, sr, sc, eh, er, ec):
    visited = [[[False] * n for i in range(n)] for i in range(5)]
    visited[sh][sr][sc] = True
    q = deque([(sh, sr, sc, 0)])

    while q:
        h, r, c, time = q.popleft()
        if (h, r, c) == (eh, er, ec):
            return time

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            nh = h
            # 실수하면 큰일난다.
            if h == 4:  # 윗면이면 어디로든지 갈 수 있음
                if nr < 0:  # 북
                    nh = 3
                    nr = 0
                    nc = m - 1 - nc
                elif nr >= m:  # 남
                    nh = 2
                    nr = 0
                    nc = nc
                elif nc < 0:  # 서
                    nh = 1
                    nc = nr
                    nr = 0
                elif nc >= m:  # 동
                    nh = 0
                    nc = m - 1 - nr
                    nr = 0
            elif h == 0:  # 동쪽면은 위,북,남 갈 수 있음
                if nr < 0:  # 위로
                    nh = 4
                    nr = m - 1 - nc
                    nc = m - 1
                elif nc >= m:  # 북쪽으로
                    nh = 3
                    nc = 0
                    nr = nr
                elif nc < 0:  # 남쪽으로
                    nh = 2
                    nc = m - 1
                    nr = nr
            elif h == 1:  # 서쪽면은 위,북,남 갈 수 있음
                if nr < 0:  # 위로
                    nh = 4
                    nr = m - 1 - nc
                    nc = 0
                elif nc >= m:  # 남쪽으로
                    nh = 2
                    nc = 0
                    nr = nr
                elif nc < 0:  # 북쪽으로
                    nh = 3
                    nc = m - 1
                    nr = nr
            elif h == 2:  # 남쪽면은 위,서,동 갈 수 있음
                if nr < 0:  # 위로
                    nh = 4
                    nr = m - 1
                    nc = nc
                elif nc < 0:  # 서쪽으로
                    nh = 1
                    nc = m - 1
                    nr = nr
                elif nc >= m:  # 동쪽으로
                    nh = 0
                    nc = 0
                    nr = nr

            elif h == 3:  # 북쪽면은 위,동,서 갈 수 있음
                if nr < 0:  # 위로
                    nh = 4
                    nr = 0
                    nc = m - 1 - nc
                elif nc < 0:  # 동쪽으로
                    nh = 0
                    nc = m - 1
                    nr = nr
                elif nc >= m:  # 서쪽으로
                    nh = 1
                    nc = 0
                    nr = nr

            if not (0 <= nr < m and 0 <= nc < m) or visited[nh][nr][nc] or cube[nh][nr][nc] == 1:
                continue
            visited[nh][nr][nc] = True
            q.append((nh, nr, nc, time + 1))
    return -1


def bfs2(sr, sc, er, ec):
    visited = [[False] * n for i in range(n)]
    visited[sr][sc] = True
    q = deque([(sr, sc, 0)])

    while q:
        r, c, time = q.popleft()
        if (r, c) == (er, ec):
            return time

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or grid[nr][nc] == 1 or grid[nr][nc] == 3:
                continue
            if ans + time + 1 >= time_attack[nr][nc]:
                continue
            visited[nr][nc] = True
            q.append((nr, nc, time + 1))
    return -1


# --------------------------------- 메인 ---------------------------------
ans = bfs3(sh3, sr3, sc3, eh3, er3, ec3)
if ans != -1:  # ans == -1이면 3차원 탈출도 못함
    ans += 1

    if time_attack[sr2][sc2] <= ans:
        ans = -1 # 내려왔는데 시간이상..


    if ans != -1:
        next_ans = bfs2(sr2, sc2, er2, ec2)
        if next_ans == -1:  # 2차원 탈출 못함
            ans = -1
        else:
            ans += next_ans
print(ans)
###########################################################3
# 2차풀이 시간이상현상 2차원으로
# --------------------------------- 입력, 좌표찾기 ---------------------------------

from collections import deque

n, m, time_attack_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
cube = []
for _ in range(5):
    tmp = [list(map(int, input().split())) for i in range(m)]
    cube.append(tmp)

row = [0, 0, 1, -1]
col = [1, -1, 0, 0]

sh3, sr3, sc3 = -1, -1, -1  # 3차원 시작점
eh3, er3, ec3 = -1, -1, -1  # 3차원 탈출구
sr2, sc2 = -1, -1,  # 2차원 시작점
er2, ec2 = -1, -1  # 2차원 탈출구


def find():  # 3 시작 위치 찾기
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 3:
                return i, j


startx, starty = find()

for i in range(n):  # 2차원 목적지 찾기
    for j in range(n):
        if grid[i][j] == 4:
            er2, ec2 = i, j

for h in range(5):  # 3차원 시작점 찾기
    for i in range(m):
        for j in range(m):
            if cube[h][i][j] == 2:
                sh3, sr3, sc3 = h, i, j

for i in range(n):  # 2차원 시작점, 3차원 목적지 찾기
    for j in range(n):
        if grid[i][j] == 3:
            for k in range(4):
                nr = i + row[k]
                nc = j + col[k]
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    sr2, sc2 = nr, nc  # 2차원 시작점
                    # 이제 3차원 목적지 찾기
                    eh3 = k  # k가 면 idx가 될거임.
                    er3 = m - 1  # r은 무조건 2임.
                    if k == 0:  # 동
                        ec3 = m - 1 - (nr - startx)
                    elif k == 1:  # 서
                        ec3 = nr - startx
                    elif k == 2:  # 남
                        ec3 = nc - starty
                    elif k == 3:  # 북.
                        ec3 = m - 1 - (nc - starty)
                    break

# ---------------------- 시간 이상 2차원 배열 만들기 ----------------------
time_attack = [[1000 * 20 + 1] * n for i in range(n)]
time_info = [list(map(int, input().split())) for i in range(time_attack_num)]
for tr, tc, td, tv in time_info:
    v = tv
    time_attack[tr][tc] = 0

    for k in range(n):
        ntr = tr + row[td]
        ntc = tc + col[td]
        if not (0 <= ntr < n and 0 <= ntc < n) or grid[ntr][ntc]:
            break
        time_attack[ntr][ntc] = min(tv, time_attack[ntr][ntc])
        tv += v
        tr = ntr
        tc = ntc


# --------------------------------- 함수 ---------------------------------
def bfs3(sh, sr, sc, eh, er, ec):
    visited = [[[False] * n for i in range(n)] for i in range(5)]
    visited[sh][sr][sc] = True
    q = deque([(sh, sr, sc, 0)])

    while q:
        h, r, c, time = q.popleft()
        if (h, r, c) == (eh, er, ec):
            return time

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            nh = h
            # 실수하면 큰일난다.
            if h == 4:  # 윗면이면 어디로든지 갈 수 있음
                if nr < 0:  # 북
                    nh = 3
                    nr = 0
                    nc = m - 1 - nc
                elif nr >= m:  # 남
                    nh = 2
                    nr = 0
                    nc = nc
                elif nc < 0:  # 서
                    nh = 1
                    nc = nr
                    nr = 0
                elif nc >= m:  # 동
                    nh = 0
                    nc = m - 1 - nr
                    nr = 0
            elif h == 0:  # 동쪽면은 위,북,남 갈 수 있음
                if nr < 0:  # 위로
                    nh = 4
                    nr = m - 1 - nc
                    nc = m - 1
                elif nc >= m:  # 북쪽으로
                    nh = 3
                    nc = 0
                    nr = nr
                elif nc < 0:  # 남쪽으로
                    nh = 2
                    nc = m - 1
                    nr = nr
            elif h == 1:  # 서쪽면은 위,북,남 갈 수 있음
                if nr < 0:  # 위로
                    nh = 4
                    nr = m - 1 - nc
                    nc = 0
                elif nc >= m:  # 남쪽으로
                    nh = 2
                    nc = 0
                    nr = nr
                elif nc < 0:  # 북쪽으로
                    nh = 3
                    nc = m - 1
                    nr = nr
            elif h == 2:  # 남쪽면은 위,서,동 갈 수 있음
                if nr < 0:  # 위로
                    nh = 4
                    nr = m - 1
                    nc = nc
                elif nc < 0:  # 서쪽으로
                    nh = 1
                    nc = m - 1
                    nr = nr
                elif nc >= m:  # 동쪽으로
                    nh = 0
                    nc = 0
                    nr = nr

            elif h == 3:  # 북쪽면은 위,동,서 갈 수 있음
                if nr < 0:  # 위로
                    nh = 4
                    nr = 0
                    nc = m - 1 - nc
                elif nc < 0:  # 동쪽으로
                    nh = 0
                    nc = m - 1
                    nr = nr
                elif nc >= m:  # 서쪽으로
                    nh = 1
                    nc = 0
                    nr = nr

            if not (0 <= nr < m and 0 <= nc < m) or visited[nh][nr][nc] or cube[nh][nr][nc] == 1:
                continue
            visited[nh][nr][nc] = True
            q.append((nh, nr, nc, time + 1))
    return -1


def bfs2(sr, sc, er, ec):
    visited = [[False] * n for i in range(n)]
    visited[sr][sc] = True
    q = deque([(sr, sc, 0)])

    while q:
        r, c, time = q.popleft()
        if (r, c) == (er, ec):
            return time

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or grid[nr][nc] == 1 or grid[nr][nc] == 3:
                continue
            if ans + time + 1 >= time_attack[nr][nc]:
                continue
            visited[nr][nc] = True
            q.append((nr, nc, time + 1))
    return -1


# --------------------------------- 메인 ---------------------------------
ans = bfs3(sh3, sr3, sc3, eh3, er3, ec3)
if ans != -1:  # ans == -1이면 3차원 탈출도 못함
    ans += 1

    if time_attack[sr2][sc2] <= ans:
        ans = -1 # 내려왔는데 시간이상..


    if ans != -1:
        next_ans = bfs2(sr2, sc2, er2, ec2)
        if next_ans == -1:  # 2차원 탈출 못함
            ans = -1
        else:
            ans += next_ans
print(ans)
