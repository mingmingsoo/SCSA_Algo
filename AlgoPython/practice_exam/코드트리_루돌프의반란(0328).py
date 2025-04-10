from collections import deque

n, turn, sn, rp, sp = map(int, input().split())
r, c = map(lambda x: int(x) - 1, input().split())  # 루돌푸 위치
grid = [[0] * n for i in range(n)]
santa_lst = [0] * (sn + 1)
score = [0] * (sn + 1)
for _ in range(sn):
    idx, sr, sc = map(int, input().split())
    grid[sr - 1][sc - 1] = idx
    santa_lst[idx] = [sr - 1, sc - 1, 0]  # 위치, 기절
row = [-1, 0, 1, 0, 1, 1, -1, -1]
col = [0, 1, 0, -1, 1, -1, 1, -1]
change = [2, 3, 0, 1]


def is_end():
    for idx, santa in enumerate(santa_lst):
        if santa:
            return False
    return True


def cal(x, y, nx, ny):
    return (nx - x) ** 2 + (ny - y) ** 2


def jump(nr, nc, d):
    tmp = []
    q = deque([(nr, nc)])
    while q:
        sr, sc = q.popleft()
        tmp.append(grid[sr][sc])
        nsr = sr + row[d]
        nsc = sc + col[d]
        if 0 <= nsr < n and 0 <= nsc < n and grid[nsr][nsc]:
            q.append((nsr, nsc))

    return tmp


def merge(r, c, d, power, idx):  # 루돌프 위치는 바뀌면 안됨.
    # 일단 기절 맥이고 점수 매경
    score[idx] += power
    grid[r][c] = 0
    nr = r + row[d] * power
    nc = c + col[d] * power
    if not (0 <= nr < n and 0 <= nc < n):
        santa_lst[idx] = 0
    else:
        if not grid[nr][nc]:
            grid[nr][nc] = idx
            santa_lst[idx] = [nr, nc, t]
        else:
            jump_lst = jump(nr, nc, d)
            if jump_lst:
                jump_lst.reverse()
                for jdx in jump_lst:
                    jr, jc = santa_lst[jdx][0], santa_lst[jdx][1]
                    njr = jr + row[d]
                    njc = jc + col[d]
                    if 0 <= njr < n and 0 <= njc < n:
                        grid[njr][njc], grid[jr][jc] = grid[jr][jc], grid[njr][njc]
                        santa_lst[jdx][0] = njr
                        santa_lst[jdx][1] = njc
                    else:
                        santa_lst[jdx] = 0
                        grid[jr][jc] = 0
            grid[nr][nc] = idx
            santa_lst[idx] = [nr, nc, t]


def myprint():
    for i in range(n):
        for j in range(n):
            if (i,j) == (r,c):
                print("R", end=  " ")
            elif grid[i][j]:
                print(grid[i][j], end = " ")
            else:
                print(0, end = " ")
        print()

for t in range(1, turn + 1):
    # print("-------",t,"-------")
    # 1. 루돌프 이동
    lst = []
    for idx, santa in enumerate(santa_lst):
        if not santa:
            continue
        sr, sc, stun = santa
        dist = cal(r, c, sr, sc)
        lst.append((dist, (-sr, -sc), idx))
    lst.sort()
    _, location, sidx = lst[0]
    sr, sc = -location[0], -location[1]
    # 타겟은 정해졌고 타겟과 가장 가깝게
    lst = []
    for k in range(8):
        nr = r + row[k]
        nc = c + col[k]
        if 0 <= nr < n and 0 <= nc < n:
            dist = cal(nr, nc, sr, sc)
            lst.append((dist, (nr, nc), k))
    lst.sort()
    _, location, ru_d = lst[0]
    r, c = location  # 옮겻!!

    if grid[r][c]:
        merge(r, c, ru_d, rp, grid[r][c])
    # print("루돌프 이동 후")
    # myprint()
    # 2. 산타 이동
    for idx, santa in enumerate(santa_lst):
        if not santa:
            continue
        sr, sc, stun = santa
        if stun and stun >= t - 1:  # 기절한 애들
            continue
        lst = []
        cur = cal(sr,sc,r,c)
        for k in range(4):
            nr = sr + row[k]
            nc = sc + col[k]
            if 0 <= nr < n and 0 <= nc < n and not grid[nr][nc]:
                dist = cal(nr, nc, r, c)
                if cur > dist:
                    lst.append((dist, k, (nr, nc)))
        if lst:
            lst.sort()
            _, s_d, location = lst[0]
            nr, nc = location
            if (nr, nc) == (r, c):
                grid[sr][sc] = 0
                merge(r, c, change[s_d], sp, idx)
            else:
                # 그냥 이동
                santa_lst[idx] = [nr, nc, stun]
                grid[nr][nc], grid[sr][sc] = grid[sr][sc], grid[nr][nc]
        # print(idx,"번 산타 이동")
        # myprint()
    # 3. 살아있는 애들 +1 점
    all_die = True
    for idx, santa in enumerate(santa_lst):
        if santa:
            score[idx] += 1
            all_die = False
    if all_die:
        break
print(*score[1:])

'''
# 코드트리 루돌프의 반란
2025.04.06.일
두번째 풀이

# 문제 풀고 나서 기록
    제출횟수 1회
    문제 시작 20:09
    문제 종료 21:26

    총 풀이시간 77분
        09~28   : 문제이해 및 손코딩, 입력받기(19)
        28~39   : 루돌프 이동(11)
        39~45   : merge 상호작용 빼고 작성(6)
        45~58   : 산타 이동(13)
        58~11   : 상호작용 jump 작성(13)
        11~17   : 살아있는 산타 +1 점, 다 튕겨저 나갔으면 break 로직 작성(6)
        17~26   : 검증(9)

    메모리 19 MB
    시간 99 ms
    
    회고
    1. 두번째 풀이인데도 어렵다. 다시 풀어보기
    

# 문제 풀면서의 기록
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


'''
# 체감난이도 골1~플5

# 문제 풀고 나서 기록
    제출 횟수 3회
    문제 시작 14:00
    1차 제출  16:17
    2차 제출  16:21
    문제 종료 16:35

    총 풀이시간 155분
        00~18   : 문제 이해 및 손코딩(18)
        18~27   : 손코딩 기반 초기 주석 및 필요한 변수/함수 세분화(9)
        27~32   : 입력받기(5)
        32~38   : ru_move 설계(6)
        38~49   : ru_move 확인(11)
                    산타들과의 거리가 크게나와서 디버깅
                    (1)
                    r,c 을 루돌프 좌표로 했는데 입력받을 때도 산타 좌표롤 r,c 로 받아서
                    변수 중복돼서 루돌프 좌표가 수정된 거였음. 수정!
                    (2)
                        ================== before ==================
                        for k in range(8):
                            nr = deer_r + row[k]
                            nc = deer_c + col[k]
                            if not (0 <= nr < n and 0 <= nc < n):
                                continue
                            next = (nr - sr) ** 2 + (nc - sc) ** 2
                            if next < cur:
                                deer_r, deer_c, d = nr, nc, k
                        ============================================
                        이 부분에서 deer_r, deer_c 이 계속 갱신되면서
                        k 가 바뀔때마다 원래 루돌프 위치가 바껴서 거리가 계산이 잘 안됐음
                        그래서 원래의 사슴 위치를 기록해줌 (근데 또 문제 생겨서 수정할 예정)
                        ================== after ==================
                        ori_r, ori_c = deer_r, deer_c
                        for k in range(8):
                            nr = ori_r + row[k]
                            nc = ori_c + col[k]
                            if not (0 <= nr < n and 0 <= nc < n):
                                continue
                            next = (nr - sr) ** 2 + (nc - sc) ** 2
                            if next < cur:
                                deer_r, deer_c, d = nr, nc, k
                         ============================================
        49~58   : santa_move 설계(9)
                santa 이동거리는 맨해튼인 줄 알고 설계중...
                + 루돌프 충돌시 설계(상호작용이 아닐 때)
        58~13   : santa_move 확인(15)
                    1. sleep >= 0일 때만 기절 상태 검사하는걸로 수정
                        왜냐하면 -1 이라서 저 조건이 없으면 여기 continue에 다 걸려버림
                        아래처럼 수정
                        if sleep >= 0 and t - sleep <= 1:  # 기절이면 넘어가!
                            continue
                    2. 맨해튼 거리로 하면 문제 예시처럼 산타가 이동할 수 없어서
                        아 모든 이동거리가 제곱으로 하라는 거구나 하고 수정!
                        그냥 싹 지우고 다시 썼음.....ㅎ
                    3. 그래도 문제 설명처럼 산타가 이동을 안함
                        ================== before ==================
                        if next < cur:
                            sr, sc, sd = next, nsr, nsc, k
                        ============================================
                        아. ... 가장 가까운 거리로 갱신해줘야하는데 그걸 안했음 추가!
                        ru_move 도 같이 수정해줌!!
                        ================== after ==================
                        if next < cur:
                            cur, sr, sc, sd = next, nsr, nsc, k
                        ============================================
        13~49   : 충돌 발생 로직 작성(36)
                    루돌프에서 먼저 작성하면 산타 충돌도 똑같다고 생각함
        49~51   : end, scoring 설계(2)
        51~00   : 1번 테케는 나오고 2번 테케는 값이 조금 다름(9)
                    헐 대박...
                    산타가 순서대로 주는게 아니였음 ㅋㅋㅋㅋㅋㅋ
                    번호를 와리가리주네...?ㅋㅋ 입력만 조금 수정해줌
                    그래도 값이 조금 다름 ㅠㅠㅠ
                    2번 테케 산타가 많아서 복잡해서 작은 테케 만들어보기
        00~05   : 약속의 시간~.~(5)
                뭘 디버깅해야할지 생각했음
        05~08   : 2번 디버깅(3)
                    작은 테케 만들때 산타 힘은 크게, 루돌프 힘은 작게 줬는데
                    오잉? 점수가 안맞음!!
                    으 산타 점수 계산때 산타힘이 아니라 루돌프 힘 더해줬음 수정!
        08~17   : 검증(9)
                    1. 격자밖 나가는 산타 이동 테케 만들기
                    2. 연쇄적으로 쫓겨나는지 확인하는 테케 만들기
                    -> 무한루프도네? 아 nsr,nsc 담아야하는데 sr,sc 담아서 bfs 가 계속 돔 수정!
                    3. 옮겨야하는 애들 sort reverse 해줌
        17      : 1차 제출 -> 메모리 초과
        18~22   : 무한루프돈다. 10번테케여서 넣어봄(4)
                    bfs에서 sr, sc = santa_lst[idx][0], santa_lst[idx][0] 이러고 있음
                    sr, sc = santa_lst[idx][0], santa_lst[idx][1] 로 수정
                    -> 만든 테케가 대각선 이동이였어서 됐었나봄 ㅠㅠ

        22      : 2차 제출 -> 틀!
        22~35   : 12번 테케에서 틀려서 안보고.. 로직 점검
                    로직 확인하면서 산타의 방향들 저장 안해도돼서 없애버림
                    옮겨야하는 애들 sort reverse 해줌 하면서 루돌프쪽만 수정하고
                    산타쪽 수정 덜ㄹ해줌 ...;;; 수정
        35      : 3차 제출 -> 성공!


  메모리  19 MB
  시간 95 ms

    회고

        1. 메서드 하나하나 완벽하게 짜낸게 없어서 내 구현력이 낮다는 걸 느꼈음 ...
            문제는 이해하기 어렵지 않았으나... 내가 생각하는 걸 코드로 짜내는게 어려웠달까 ㅠㅠ
            부족하지만 성장해야지 뭐.. 힘내자

        2. 검증할 때 테케만 만들어보고 오타 없는지... 검사 안했음 ㅠㅠ
            이번엔 틀린 이유가 다 오타였음.................
            시험은 4시간이다 집중하자............

# 문제 풀면서의 기록
코드리팩토링
1회 틀: sr, sr 이러고 있음
2회 틀: 루돌프 충돌 수정해놓고 산타 충돌은 수정안함 미쳤어?

문제 설명
    1. 루돌프 이동 - 8방 우선순위 거리(^2) 주의, r 큰거 , c 큰거
    2. 산타 순차 이동 - 4방 우선순위 상우하좌
구상
    상호작용이 좀 어려운데
    기사단처럼 q로 써서 움직여야 하는애들 move_lst에 담고
    옮겨주면서 격자 밖인 애들은 없애줌 걍
    아 근데 산타이동 할때 순차라
    산타 1차원 리스트로 관리해주자.

입력
맵 크기 N, 턴 수 time, 산타 수 santa_num, 루돌푸 힘 ru_p,  산타 힘 s_p
루돌푸 위치
산타 위치

필요한 변수
    - 루돌프 좌표 r,c,d 맵에 따로 표시 안한다
    - 산타 맵 2차원 배열 grid 넘버링만 해준다
        산타 1차원 배열
        방향, 기절시간 담아준다
        방향과 기절시간 초기값은 -1
        근데 죽은애는 0으로 해주자.
    - score 산타 수 + 1만큼 0번쨰에 빈 0 넣어주기
필요한 함수
    ru_move() : 루돌프 이동
        if merge() : 충돌 낫냐?
            # 여기서 기절시간 기록
            santa_jump() : 났으면 와라락 이동
    santa_move() : 산타 순차 이동
        if 기절시간 <= time -1 : continue 요롷게  해서 넘어가.
        if merge() : 충돌 낫냐?
            # 여기서 기절시간 기록
            santa_jump() : 났으면 와라락 이동
    exit() : 전부 죽었나 검사
    scoring(): 살아있는 애들 점수 추가

잘 밀려서 쫓겨나는지
3 1 2 1 10
1 1
1 2 2
2 3 3

잘 밀려서 안 쫓겨나는지
4 1 2 1 10
1 1
1 2 2
2 3 3

와라락 밀리는지
5 1 4 1 10
1 1
1 2 2
2 3 3
3 4 4
4 5 5

'''
from collections import deque

n, time, santa_num, rup, sp = map(int, input().split())
deer_r, deer_c = map(lambda x: int(x) - 1, input().split())
grid = [[0] * n for i in range(n)]
santa_lst = [0] * (santa_num + 1)
score = [0] * (santa_num + 1)
for s in range(santa_num):
    sidx, sr, sc = map(int, input().split())
    grid[sr - 1][sc - 1] = sidx
    santa_lst[sidx] = [sr - 1, sc - 1, -1]
row = [-1, 0, 1, 0, 1, 1, -1, -1]
col = [0, 1, 0, -1, 1, -1, 1, -1]
dirs = {0: 2, 1: 3, 2: 0, 3: 1}  # 반대 방향


def ru_move():
    global deer_r, deer_c
    close_santa = []
    for santa in santa_lst:
        if santa == 0:  # 죽은 애 넘어가
            continue
        i, j = santa[0], santa[1]
        close_santa.append(((i - deer_r) ** 2 + (j - deer_c) ** 2, i, j))

    close_santa.sort(key=lambda x: (x[0], -x[1], -x[2]))
    dist, sr, sc = close_santa[0]

    cur = (deer_r - sr) ** 2 + (deer_c - sc) ** 2
    ori_r, ori_c = deer_r, deer_c

    for k in range(8):
        nr = ori_r + row[k]
        nc = ori_c + col[k]
        if not (0 <= nr < n and 0 <= nc < n):
            continue
        next = (nr - sr) ** 2 + (nc - sc) ** 2
        if next < cur:
            cur, deer_r, deer_c, d = next, nr, nc, k

    if grid[deer_r][deer_c]:  # 충돌 발생!!
        idx = grid[deer_r][deer_c]
        score[idx] += rup
        nsr = deer_r + row[d] * rup
        nsc = deer_c + col[d] * rup

        jump_santa(sr, sc, nsr, nsc, idx, d)


def merge(sr, sc, sd, move_lst):
    q = deque()
    if grid[sr][sc]:
        q.append(grid[sr][sc])

    while q:
        idx = q.popleft()
        move_lst.append(idx)
        sr, sc = santa_lst[idx][0], santa_lst[idx][1]
        nsr = sr + row[sd]
        nsc = sc + col[sd]
        if 0 <= nsr < n and 0 <= nsc < n and grid[nsr][nsc]:
            q.append(grid[nsr][nsc])


def jump_santa(sr, sc, nsr, nsc, idx, sd):
    if not (0 <= nsr < n and 0 <= nsc < n):
        santa_lst[idx] = 0  # 쥬금
        grid[sr][sc] = 0  # 쥬금
    else:
        move_lst = []
        merge(nsr, nsc, sd, move_lst)
        move_lst.sort(reverse=True)

        for jump_idx in move_lst:
            jr, jc, jsleep = santa_lst[jump_idx]
            njr = jr + row[sd]
            njc = jc + col[sd]
            if not (0 <= njr < n and 0 <= njc < n):
                santa_lst[jump_idx] = 0  # 쥬금
            else:
                grid[njr][njc] = jump_idx
                santa_lst[jump_idx][0] = njr
                santa_lst[jump_idx][1] = njc

        # 기절해!!
        santa_lst[idx][0] = nsr
        santa_lst[idx][1] = nsc
        santa_lst[idx][2] = t  # 기절!
        grid[sr][sc] = 0
        grid[nsr][nsc] = idx


def santa_move(t):
    for idx, santa in enumerate(santa_lst):
        if santa == 0:
            continue
        sr, sc, sleep = santa
        if sleep >= 0 and t - sleep <= 1:  # 기절이면 넘어가!
            continue

        cur = (sr - deer_r) ** 2 + (sc - deer_c) ** 2
        ori_sr, ori_sc = sr, sc
        for k in range(4):
            nsr = ori_sr + row[k]
            nsc = ori_sc + col[k]
            if not (0 <= nsr < n and 0 <= nsc < n) or grid[nsr][nsc]:
                continue
            next = (nsr - deer_r) ** 2 + (nsc - deer_c) ** 2
            if next < cur:
                cur, sr, sc, sd = next, nsr, nsc, k
        santa_lst[idx][0] = sr
        santa_lst[idx][1] = sc
        grid[ori_sr][ori_sc] = 0
        grid[sr][sc] = idx
        if (sr, sc) == (deer_r, deer_c):  # 충돌 발생!!
            score[idx] += sp
            nsr = sr + row[dirs[sd]] * sp
            nsc = sc + col[dirs[sd]] * sp

            jump_santa(sr, sc, nsr, nsc, idx, dirs[sd])


def end():
    for santa in santa_lst:
        if santa != 0:
            return False
    return True


def scoring():
    for idx, santa in enumerate(santa_lst):
        if santa != 0:
            score[idx] += 1


def myprint():
    for i in range(n):
        for j in range(n):
            if (i, j) == (deer_r, deer_c):
                print("R", end=" ")
            else:
                print(grid[i][j], end=" ")
        print()


for t in range(time):
    ru_move()
    santa_move(t)
    if end():
        break
    scoring()
print(*score[1:])
