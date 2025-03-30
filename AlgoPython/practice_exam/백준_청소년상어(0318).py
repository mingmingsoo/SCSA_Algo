'''
# 백준 19236 청소년상어
# 체감난이도 객관적으로 골1인데 하 백트래킹 너무 어렵다 내 기준 플5

# 문제 풀고 나서 기록

    문제 시작 14:00
    문제 종료 15:27
    총 풀이시간 87분
        00~07   : 문제 이해(7)
        07~10   : 초기 주석 및 문제 구상(3)
        10~16   : ~입력 받기(6)
                    (1) 3차원 배열 썼다가 [[[]]], btk 면 맵 원상복구 해줘야하는데 복사에 문제생길 것 같아서 tuple로 바꿨다[[()]]
                    (2) btk 주석 먼저 달기 -> 잘한듯?
                        [# 물고기 이동]
                        [# 상어 이동]
                        [# 근데 이동할 곳 없으면 return]
        16~31   : 물고기 이동 로직(15)
                    물고기 따로 관리해줘도 되지만... 굳이? 싶어서 swap하는 걸로 짰다.
                    새로운 게임2에서 flag 위치로 머리 아팠던 기억에 flag 위치 먼저 넣어주고 갔다.
                    테케처럼 물고기 이동 잘 하는지 확인
        31~36   : 상어 이동 로직 작성(5)
        36~37   : 무한루프 돌아서 디버깅(1)
                    -> 상어 이동 로직 수정
        37~49   : 아까처럼은 아니지만 어디선가 무한루프 돌아서 디버깅(12)
                    (1) 종료조건 return 추가
                    (2) 물고기가 빈 곳으로 이동하고 전에 있던 곳 비워줘야하는데 안비워줌!
                        grid[ofr][ofc] = ()  코드 추가
        49~53   : 무한 루프가 안멈춰요 .. 디버깅 시작(4)
                    상어가 3,3 에서 무한루프 돌아서 확인! 쩜푸하는 로직이 없음!!
                    상어가 빈곳에 가면 그 위치가 갱신되게 로직 추가!
                    elif 0 <= nr < n and 0 <= nc < n and not grid[nr][nc]:
                    ori_r = nr
                    ori_c = nc
        53~57   : 1번 테케 답이 73 이 나오는 대참사 (답 33임)(4)
                    맵을 원상복구 시키는 로직 수정
                    grid[nr][nc] = ()
                    btk(nr, nc, nd, eat + num)
                    grid[nr][nc] = (num,nd)
                    이렇게만 했는데 이러면 이동 반영이 안돼서 맵 배열 복사
                    -> 근데 그 복사를 물고기 이동전에 했지뭐야?
        57~27   : 2번 테케 답이 다름(20)
                    무한 디버깅 시작
                    이동도 잘하고!! 상어도 갈 곳 잘 담음!!!! 그럼 뭐가문젠데!!!
                    이동 하고나서 맵 배열을 복사해줘야하는데 이동 전에 맵 배열을 복사했었음!!!!! you 바보??!?
                    -> 배열 복사 위치 수정
                    -> 드디어 답이 나오네요


    메모리 110964 KB
    시간 112 ms

    회고
        1. [아 이게 btk인지... btk 로 풀겠다 일단.] 라고 썼는데
            이렇게 고민한 이유는 '무조건 큰 물고기 먹어야 이득아닌가?' 했지만
            상어가 무슨 물고기를 먹냐에 따라 물고기 이동이 달라지기에 btk여야한다고 생각했다. 그게 맞음!

        2. [상어가 쩜푸가되나?] 라고 썼는데 만약 [상어 - 빈공간 - 물고기] 일때 상어가 쩜푸해서 물고기까지 갈 수 있는지 헷갈렸다
             "한 번에 여러 개의 칸을 이동할 수 있다." 라고 써있어서  일단 쩜푸가 된다고 가정하고 풀었다. -> 이게 맞음!

        3. 백트래킹 너무 어렵고..
            grid[nr][nc] = ()
            btk(nr, nc, nd, eat + num)
            grid[nr][nc] = (num,nd)
            이렇게 하면 왜 안되는지 아직 모르겠음.ㅠㅠㅠ 알아내기

            -> 알아냈습니다!!!!
             btk 타고가면 상어가 어떻게 가냐에 따라 물고기 이동이 달라지는데
             grid[nr][nc] = (num,nd) 이렇게만 해주면,
             물고기들 위치가 원상복구가 안되고 상어가 잡아먹은 물고기만 채워주는 거여서 안된다!

        4. 오랜만에 디버깅 열심히 했네.......... 디버깅 하면 체력소모가 심하고 기빨린다..........
            디버깅 안하려면 로직을 꼼꼼히 짜야한다..... 명심하도록


# 문제 풀면서의 기록
아 이게 btk인지...
btk 로 풀겠다 일단.

문제 설명
    0. 상어 등장
    [반복]
    1. 물고기 이동
    2. 상어 이동

입력
    상어 번호와 방향
출력
    상어가 먹을 수 있는 물고기 번호의 최댓값

구상
    입력을 일단,, 받고
    상어 0,0,-1 에서 0,0의 방향과 초기 eat 가지고
    btk시작하는데(상어r, 상어c, eat)
    종료조건은 상어가 갈 수 있는 곳이 없으면 return

상어가 쩜푸가되나?
'''


##############################################################
# 첫번째 풀이
n = 4
grid = [[[0] for i in range(4)] for i in range(4)]

for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(0, 8, 2):
        grid[i][j // 2] = (tmp[j], tmp[j + 1] - 1)  # 상어 번호, 방향

sr, sc = 0, 0
sd, eat = grid[0][0][1], grid[0][0][0]
grid[0][0] = ()
row = [-1, -1, 0, 1, 1, 1, 0, -1]
col = [0, -1, -1, -1, 0, 1, 1, 1]
ans = 0


def btk(r, c, d, eat):
    global ans, grid
    # 물고기 이동
    for num in range(1, 17):
        find = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] and grid[i][j][0] == num:
                    find = True
                    ofr, ofc, ofd = i, j, grid[i][j][1]
                    fr, fc, fd = ofr, ofc, ofd
                    move = False
                    for k in range(8):
                        nfr = fr + row[fd]
                        nfc = fc + col[fd]
                        if not (0 <= nfr < n and 0 <= nfc < n) or (nfr, nfc) == (r, c):
                            fd = (fd + 1) % 8
                        else:
                            fr = nfr
                            fc = nfc
                            move = True
                            break
                    if move:
                        if grid[fr][fc]:
                            grid[ofr][ofc] = (grid[fr][fc][0], grid[fr][fc][1])
                            grid[fr][fc] = (num, fd)
                        else:
                            grid[fr][fc] = (num, fd)
                            grid[ofr][ofc] = ()
                    break
            if find:
                break
    grid_origin = [_[:] for _ in grid]

    # 상어 이동
    # 근데 이동할 곳 없으면 return
    shark_go = []
    ori_r, ori_c = r, c
    while True:
        nr = ori_r + row[d]
        nc = ori_c + col[d]
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc]:
            shark_go.append((nr, nc, grid[nr][nc][0], grid[nr][nc][1]))
            ori_r = nr
            ori_c = nc
        elif 0 <= nr < n and 0 <= nc < n and not grid[nr][nc]:
            ori_r = nr
            ori_c = nc
        if not (0 <= nr < n and 0 <= nc < n):
            break
    if not shark_go:
        ans = max(ans, eat)
        return
    else:
        for nr, nc, num, nd in shark_go:
            grid[nr][nc] = ()
            btk(nr, nc, nd, eat + num)
            grid = [_[:] for _ in grid_origin]


btk(sr, sc, sd, eat)
print(ans)

##############################################################
# 두번째 풀이 코드 리팩토링(함수화)

def myprint():
    print("----------------------")
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                print(grid[i][j][0], end="")
                print("↑↖←↙↓↘→↗"[grid[i][j][1]], end=" ")
            else:
                print("XX", end=" ")
        print()


def move(r, c):  # 물고기 이동
    for num in range(1, 17):
        find = False
        for i in range(n):
            for j in range(n):
                if grid[i][j] and grid[i][j][0] == num:
                    find = True
                    ofr, ofc, ofd = i, j, grid[i][j][1]  # 원래 위치
                    fr, fc, fd = ofr, ofc, ofd  # 바뀔 위치
                    move = False
                    for k in range(8):
                        nfr, nfc = fr + row[fd], fc + col[fd]
                        if not (0 <= nfr < n and 0 <= nfc < n) or (nfr, nfc) == (r, c):
                            fd = (fd + 1) % 8  # 못가는 곳이면 방향 전환
                        else:  # 갈 수 있는 곳이면 위치 갱신
                            fr = nfr
                            fc = nfc
                            move = True
                            break
                    if move:  # 갈 수 있으면 간다.
                        if grid[fr][fc]:  # 물고기 있는 곳이면 swap
                            grid[ofr][ofc] = (grid[fr][fc][0], grid[fr][fc][1])  # 원래 위치에 가는 곳의 물고기를..
                            grid[fr][fc] = (num, fd)  # 갈 곳에 가는 애를..
                        else:  # 빈 공간으로 가면 나만 넣어줌
                            grid[fr][fc] = (num, fd)
                            grid[ofr][ofc] = ()
                    break  # 다음 번호 물고기 탐색을 위해 break 1
            if find:  # 다음 번호 물고기 탐색을 위해 break 2
                break


def shark_navi(r, c, d):  # 어디 갈 수 있는지 넣어줄 거임
    shark_go = []
    ori_r, ori_c = r, c
    while True:
        nr = ori_r + row[d]
        nc = ori_c + col[d]
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc]:  # 물고기 있는 곳 넣어줌
            shark_go.append((nr, nc, grid[nr][nc][0], grid[nr][nc][1]))
            ori_r = nr
            ori_c = nc
        elif 0 <= nr < n and 0 <= nc < n and not grid[nr][nc]:  # 물고기 없는 곳이면 일단 위치만 갱신
            ori_r = nr
            ori_c = nc
        else:  # 범위 벗어났으면 while 탈출
            break
    return shark_go


def btk(r, c, d, eat):
    global ans, grid
    move(r, c)
    grid_origin = [_[:] for _ in grid]  # btk 원상복귀를 위해 카피본 만들기

    shark_go = shark_navi(r, c, d)
    if not shark_go:  # 상어 집가.
        ans = max(ans, eat)
        return
    else:  # 상어 물고기 먹어
        for nr, nc, num, nd in shark_go:
            grid[nr][nc] = ()
            btk(nr, nc, nd, eat + num)
            grid = [_[:] for _ in grid_origin]  # 원상복구


n = 4
grid = [[[0] for _ in range(4)] for _ in range(4)]

for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(0, 8, 2):
        grid[i][j // 2] = (tmp[j], tmp[j + 1] - 1)  # 상어 번호, 방향

sr, sc, sd, eat = 0, 0, grid[0][0][1], grid[0][0][0]  # 상어 초기 위치, 방향, 처음 먹은 양
grid[0][0] = ()  # 처음 물고기 먹혔다.
row = [-1, -1, 0, 1, 1, 1, 0, -1]
col = [0, -1, -1, -1, 0, 1, 1, 1]
ans = 0
btk(sr, sc, sd, eat)
print(ans)