'''
# 코드트리 싸움땅
2025.04.05.토
두번째 풀이

# 문제 풀고 나서 기록
    제출횟수 2회
    문제 시작 19:20
    1차 제출  20:01
    문제 종료 20:49

    총 풀이시간 89분
        20~30   : 문제이해 및 손코딩, 주석(7)
        30~41   : 플레이어 이동 로직 - 싸움 안할 때
        41~55   : 플레이어 이동 로직 - 싸움 할 때
        55~01   : 2번 테케 안나와서 디버깅
                    if other_gun > gun:
                        if gun > 0:
                            gun_grid[nr][nc].append(gun)
                        gun_grid[nr][nc].remove(other_gun)
                        gun = other_gun
                        player_grid[nr][nc] = p
                        player_lst[p] = [nr, nc, d, s, gun]

                    이렇게 되어있는데, 이러면 내 총이 더 클 때는 플레이어가 이동을 안함!
                    -> 들여쓰기 수정

                    if other_gun > gun:
                        if gun > 0:
                            gun_grid[nr][nc].append(gun)
                        gun_grid[nr][nc].remove(other_gun)
                        gun = other_gun
                    player_grid[nr][nc] = p
                    player_lst[p] = [nr, nc, d, s, gun]
        01~49   : 틀렸습니다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 디버깅.............(48)
                    플레이어가 벽만나서 방향 바꾸고, 싸움을 하게 됐을 때
                    player_lst[p][2] = d
                    바뀐 방향을 갱신안해줘서 틀렸음....................


  메모리 18 MB
  시간 91 ms

  회고
    1. 이렇게 틀려본거 정말 좋은 기회라고 생각합니다...
        방향을 갱신 안해줘서 틀리다니!!!!!!!!!!!!!!!!!!!!!!!!!!! 리스트업 ...
        !! 방향 바꾸고 리스트에 갱신 확실히 하기 !!


# 문제 풀면서의 기록
문제 설명
    1. 플레이어 순차 이동
    2. 플레이어 없으면 총먹어
                있으면 싸움

입력
    맵n, 플레이어 수 m, 턴 수 turn
    총 정보(맵)
    플레이어 정보 r,c,d,s
필요한 변수
player_lst = [위치,방향,능력치,총]
player_grid = [넘버만]
gun_grid = 3차원
'''

n, pm, turn = map(int, input().split())
tmp = [list(map(int, input().split())) for i in range(n)]
gun_grid = [[[] for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if tmp[i][j]:
            gun_grid[i][j].append(tmp[i][j])
player_lst = [0]
player_grid = [[0] * n for i in range(n)]
for _ in range(pm):
    r, c, d, s = map(int, input().split())
    player_lst.append([r - 1, c - 1, d, s, 0])
    player_grid[r - 1][c - 1] = _ + 1

score = [0] * (pm + 1)
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


def move(win_idx, lose_idx, x, y):
    # 진 플레이어 이동
    _, _, d, s, gun = player_lst[lose_idx]
    if gun:
        gun_grid[x][y].append(gun)
        gun = 0
    for k in range(4):
        nr = x + row[d]
        nc = y + col[d]
        if 0 <= nr < n and 0 <= nc < n and player_grid[nr][nc] == 0:
            break
        else:
            d = (d + 1) % 4
    if gun_grid[nr][nc]:
        gun = max(gun_grid[nr][nc])
        gun_grid[nr][nc].remove(gun)
    player_lst[lose_idx] = [nr, nc, d, s, gun]
    player_grid[nr][nc] = lose_idx

    # 이긴 플레이어 이동
    _, _, d, s, gun = player_lst[win_idx]
    if gun_grid[x][y]:
        other_gun = max(gun_grid[x][y])
        if other_gun > gun:
            gun_grid[x][y].remove(other_gun)
            if gun:
                gun_grid[x][y].append(gun)
            gun = other_gun
    player_lst[win_idx] = [x, y, d, s, gun]
    player_grid[x][y] = win_idx


for t in range(turn):
    for p in range(1, pm + 1):
        r, c, d, s, gun = player_lst[p]
        nr = r + row[d]
        nc = c + col[d]
        if not (0 <= nr < n and 0 <= nc < n):
            d = (d + 2) % 4
        nr = r + row[d]
        nc = c + col[d]
        player_grid[r][c] = 0
        player_lst[p][2] = d # 이거 안해줘서 1회틀
        if not player_grid[nr][nc]:  # 빈 곳
            other_gun = 0
            if gun_grid[nr][nc]:
                other_gun = max(other_gun, max(gun_grid[nr][nc]))
            if other_gun > gun:
                if gun > 0:
                    gun_grid[nr][nc].append(gun)
                gun_grid[nr][nc].remove(other_gun)
                gun = other_gun
            player_grid[nr][nc] = p
            player_lst[p] = [nr, nc, d, s, gun]
        else:
            px = player_grid[nr][nc]
            rx, cx, dx, sx, gunx = player_lst[px]  # 상대 정보
            win_idx = lose_idx = 0
            my_power = gun + s
            other_power = gunx + sx
            if my_power > other_power:
                win_idx, lose_idx = p, px
            elif my_power == other_power:
                if s > sx:
                    win_idx, lose_idx = p, px
                else:
                    win_idx, lose_idx = px, p
            else:
                win_idx, lose_idx = px, p
            score[win_idx] += abs(my_power - other_power)
            move(win_idx, lose_idx, nr, nc)

print(*score[1:])


'''
# 코드트리 싸움땅
# 체감난이도 골1 (위치 갱신이 어려움)

# 문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 09:00
    문제 종료 10:33
    총 풀이시간 93분
        00~15   : 문제 이해, 초기 주석 및 문제 구상(15)
                    문제 조건 안놓치려고 타이핑 하면서 이해!
        15~24   : 입력받기,  필요한 변수 설정
                    player_lst, player_grid, grid 3개 관리하려다가
                    그냥 player_grid, grid 2개로 관리하고
                    플레이어 넘버를 2중 포문 돌면서 찾으면 움직이게 설계했다 (새로운 게임 처럼)
        [move 함수 설계]
        24~30   : 싸움 안할때 로직 작성
                    총 잘 먹는지 확인하려고 인풋 넣어봤는데 오류떠서 디버깅
                    1.
                    [unpack non-iterable"]
                    if player_grid 에서
                    if player_grid[i][j]로 수정
                    2.
                    [">" not supperted between instances of list and int]
                    other_gun = grid[nr][nc] 에서
                    other_gun = max(grid[nr][nc]) 로 수정
                    -> 코드를 와라락 써서 생기는 실수들 ...^_^
        [battle 함수 설계]
        30~45   : 싸움 할때 로직 작성(15)
                    먼저 현재 순번 플레이어가 이겼다고 가정하고 대략적인 코드 작성
        45~51   : 위에 가안으로 작성해둔 코드를 기반으로(6)
                    win_score, win_num, win_d, win_power, win_gun, lose_num, lose_d, lose_power, lose_gun, nr, nc
                    를 battle 함수의 매개변수로 넘김
        51      : 1번 테케 넣어봄
                    0,0,0,0 출력! (당연한 결과)
        51~53   : 화장실(2)
        53~55   : 디버거로 애들 잘 움직이나 확인(2)
                    1.
                    d-1로 넣은거 d 로 수정! d는 0,1,2,3 으로 들어오기 때문
                    2.
                    1번 플레이어만 움직이고 끝나서 불필요한 flag 제거
        55~33   : 1번 테케는 나오고(38)
                    2번 테케에서 arg in ans empty sequence 오류
                    grid[nr][nc] 가 비어있을 때 max를 찾으려고 해서 났음!
                    if grid[nr][nc]:
                        other_gun = max(grid[nr][nc]) <- 조건 추가
                    2번 테케 답이 안나옴 디버깅 시작
                    문제 설명대로 잘 움직이고 싸우나 확인했음
                    플레이어는 무조건 움직이므로
                    battle(~~)
                    player_grid[i][j] = 0  이렇게 되어있던 코드를 순서를 바꿔줌!
 - 2차원 배열로 이중 포문 돌면서 순번 찾으면
      메모리 22 KB
      시간 156 ms
   1차원 배열로 관리해주면
      메모리 18 KB
      시간 99 ms
회고
    1. '새로운 게임처럼 플레이어들(말들)을 1차원 배열로 따로 관리해줘도 되겠다!'
        생각이 들었지만... 시간도 널널하고 그렇게 하지 않는 편이라 따로 만들진 않았다.
        (2회차에는 그렇게 했다. 1차원 배열로 관리하면 코드가 깔끔해진다.)
    2. 이런 문제 나오면 1차원 배열로 관리하자.... 디버깅 하기 힘들다
    3. 위치 갱신할 때는 before , after 확실히 하자!!!!!!!!!!!!!


# 문제 풀면서의 기록
실제 시험이라고 생각하자
문제설명
    잘 이해 안돼서 타이핑 해보자
    1. 첫번째 플레이어부터 "순차적으로" 본인이 향하고 있는 방향대로 한 칸 이동
        만약 격자 밖인 경우 반대 방향으로 한 칸 이동
    2. 이동한 방향에 플레이어가 없는 경우
        - 해당 칸에 총이 있는지 확인
        - 플레이어가 총이 없고 칸에 총이 있는 경우 총 획득
        - 플레이어가 총이 있고 칸에 총이 있는 경우
            더 쎈 총을 획득하고 나머지 총은 내려놓음
        이동한 방향에 플레이어가 있는 경우
        - 초기능력치_총 공격력 합으로 싸움
             같으면 초기 능력치가 높은 프레이어가 승리
            -> 이긴 플레이어는 플레이어 초기 능력치 + 총 공격력 합의 차이만큼 포인트 획득
        -> 진 플레이어는 본인 총 내려놓고 1칸 이동
            -> 만약 다른 플레이어나 격자가 밖이면 오른쪽으로 90도 회전해서 빈칸이 보이는 순간 이동
                해당 칸에 총이 있으면 가장 공격력 높은 총 획득, 나머지는 내려놓음
        -> 이긴 플레이어는 승리한 칸에 있는 총들과 원래 총 비교해서 가장 높은 총 획득
            나머지는 내려놓음

입력
    맵 n, 플레이어ㅅ m, k 라운드 수
    맵 정보(총 정보)
    플레이어 정보

구상
    플레이어를 어떻게 관리할건지...
    플레이어 배열 : [위치,방향,초기능력치, 총공격력]
    총 배열 : 3차원 배열

필요한 메서드
    move()
        battle()

'''


def myprint():
    print("-------------------------")
    for i in range(n):
        for j in range(n):
            if player_grid[i][j]:
                print(player_grid[i][j][0], end=" ")
            else:
                print(".", end=" ")
        print()


def battle(win_score, win_num, win_d, win_power, win_gun, lose_num, lose_d, lose_power, lose_gun, nr, nc):
    ans[win_num] += win_score

    # 진 플레이어는 본인이 가지고 있는 총을 해당 격자에 내려놓음
    if lose_gun:
        grid[nr][nc].append(lose_gun)
        lose_gun = 0
    for w in range(4):
        if not (0 <= nr + row[lose_d] < n and 0 <= nc + col[lose_d] < n) or \
                player_grid[nr + row[lose_d]][nc + col[lose_d]]:
            lose_d = (lose_d + 1) % 4
        else:
            break
    nor = nr + row[lose_d]
    noc = nc + col[lose_d]
    if grid[nor][noc]:
        lose_gun = max(grid[nor][noc])
        grid[nor][noc].remove(lose_gun)
    player_grid[nor][noc] = (lose_num, lose_d, lose_power, lose_gun)

    # 이긴 플레이어는...
    if grid[nr][nc]:
        other_gun = max(grid[nr][nc])
        if other_gun > win_gun:
            grid[nr][nc].remove(other_gun)
            grid[nr][nc].append(win_gun)  # 내 총 내려놓음
            win_gun = other_gun
    player_grid[nr][nc] = (win_num, win_d, win_power, win_gun)  # 나는 그 총 먹음


def move():
    for num in range(player_num):
        find = False
        for i in range(n):
            for j in range(n):
                if player_grid[i][j]:
                    pnum, d, power, gun = player_grid[i][j]
                    if pnum == num:
                        find = True
                        if not (0 <= i + row[d] < n and 0 <= j + col[d] < n):
                            d = (d + 2) % 4
                        nr = i + row[d]
                        nc = j + col[d]
                        if not player_grid[nr][nc]:  # 다른 플에이어가 없으면
                            # 해당 칸에 총이 있는지 확인
                            if grid[nr][nc]:
                                other_gun = max(grid[nr][nc])
                                if other_gun > gun:
                                    grid[nr][nc].remove(other_gun)
                                    if gun != 0:
                                        grid[nr][nc].append(gun)  # 내 총 내려놓음
                                    gun = other_gun
                            player_grid[nr][nc] = (pnum, d, power, gun)  # 나는 그 총 먹음
                            player_grid[i][j] = 0  # 나는 떠났음

                        else:  # 다른 플레이어 있으면 싸운다.
                            my_power = power + gun
                            o_pnum, o_d, o_power, o_gun = player_grid[nr][nc]
                            other_power = o_power + o_gun
                            if my_power > other_power:  # 내가 이김!
                                win_num, win_d, win_power, win_gun = pnum, d, power, gun
                                lose_num, lose_d, lose_power, lose_gun = o_pnum, o_d, o_power, o_gun
                            elif my_power == other_power:
                                if power > o_power:
                                    win_num, win_d, win_power, win_gun = pnum, d, power, gun
                                    lose_num, lose_d, lose_power, lose_gun = o_pnum, o_d, o_power, o_gun
                                else:
                                    win_num, win_d, win_power, win_gun = o_pnum, o_d, o_power, o_gun
                                    lose_num, lose_d, lose_power, lose_gun = pnum, d, power, gun
                            elif my_power < other_power:
                                win_num, win_d, win_power, win_gun = o_pnum, o_d, o_power, o_gun
                                lose_num, lose_d, lose_power, lose_gun = pnum, d, power, gun
                            win_score = abs(my_power - other_power)
                            player_grid[i][j] = 0  # 나는 떠났음
                            battle(win_score, win_num, win_d, win_power, win_gun, lose_num, lose_d, lose_power,
                                   lose_gun, nr, nc)
                        break
            if find:
                break


n, player_num, time = map(int, input().split())
tmp = [list(map(int, input().split())) for i in range(n)]

grid = [[[] for i in range(n)] for i in range(n)]
player_grid = [[0] * n for i in range(n)]
for p in range(player_num):
    r, c, d, power = map(int, input().split())
    player_grid[r - 1][c - 1] = (p, d, power, 0)
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if tmp[i][j]:
            grid[i][j].append(tmp[i][j])

ans = [0] * player_num

for t in range(time):
    move()
print(*ans)

'''
플레이어 정보 1차원 배열로도 관리
'''


def battle(win, lose):
    # 진 사람 로직
    lr, lc, ld, lp, lg = player_info[lose]
    if lg:
        grid[lr][lc].append(lg)
        lg = 0
    for k in range(4):
        if not (0 <= lr + row[ld] < n and 0 <= lc + col[ld] < n) or player_grid[lr + row[ld]][lc + col[ld]] != -1:
            ld = (ld + 1) % 4
        else:
            break
    nlr = lr + row[ld]
    nlc = lc + col[ld]
    if grid[nlr][nlc]:
        other_gun = max(grid[nlr][nlc])
        lg = other_gun
        grid[nlr][nlc].remove(lg)
    player_info[lose] = (nlr, nlc, ld, lp, lg)
    player_grid[nlr][nlc] = lose

    # 이긴 사람 로직
    wr, wc, wd, wp, wg = player_info[win]
    if grid[wr][wc]:
        other_gun = max(grid[wr][wc])
        if other_gun > wg:
            grid[wr][wc].append(wg)
            wg = other_gun
            grid[wr][wc].remove(wg)
    player_info[win] = (wr, wc, wd, wp, wg)
    player_grid[wr][wc] = win


def move():
    for idx, player in enumerate(player_info):
        r, c, d, power, gun = player
        if not (0 <= r + row[d] < n and 0 <= c + col[d] < n):
            d = (d + 2) % 4
        nr = r + row[d]
        nc = c + col[d]
        if player_grid[nr][nc] == -1:  # 싸움 안함!
            if grid[nr][nc]:
                other_gun = max(grid[nr][nc])
                if gun < other_gun:
                    grid[nr][nc].remove(other_gun)
                    grid[nr][nc].append(gun)
                    gun = other_gun
            player_grid[nr][nc] = idx
            player_grid[r][c] = -1
            player_info[idx] = (nr, nc, d, power, gun)
        else:  # 싸움 함!
            player_info[idx] = (nr, nc, d, power, gun)
            o_idx = player_grid[nr][nc]
            o_r, o_c, o_d, o_power, o_gun = player_info[o_idx]  # 누구랑 싸울건데
            my_score = power + gun
            o_score = o_power + o_gun
            if my_score > o_score:
                win = idx
                lose = o_idx
            elif my_score == o_score:
                if power > o_power:
                    win = idx
                    lose = o_idx
                else:
                    win = o_idx
                    lose = idx
            else:
                win = o_idx
                lose = idx
            player_grid[r][c] = -1  # 일단 빈공간은 맞음
            ans[win] += abs(my_score - o_score)
            battle(win, lose)


n, player_num, time = map(int, input().split())
tmp = [list(map(int, input().split())) for i in range(n)]

grid = [[[] for i in range(n)] for i in range(n)]
player_grid = [[-1] * n for i in range(n)]
player_info = []
for p in range(player_num):
    r, c, d, power = map(int, input().split())
    player_grid[r - 1][c - 1] = p
    player_info.append((r - 1, c - 1, d, power, 0))
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if tmp[i][j]:
            grid[i][j].append(tmp[i][j])

ans = [0] * player_num

for t in range(time):
    move()
print(*ans)


################################################################
# 두번째 풀이 : 플레이어 정보 1차원 배열로도 관리 -> 코드가 짧아짐


def battle(win, lose):
    # 진 사람 로직
    lr, lc, ld, lp, lg = player_info[lose]
    if lg:
        grid[lr][lc].append(lg)
        lg = 0
    for k in range(4):
        if not (0 <= lr + row[ld] < n and 0 <= lc + col[ld] < n) or player_grid[lr + row[ld]][lc + col[ld]] != -1:
            ld = (ld + 1) % 4
        else:
            break
    nlr = lr + row[ld]
    nlc = lc + col[ld]
    if grid[nlr][nlc]:
        other_gun = max(grid[nlr][nlc])
        lg = other_gun
        grid[nlr][nlc].remove(lg)
    player_info[lose] = (nlr, nlc, ld, lp, lg)
    player_grid[nlr][nlc] = lose

    # 이긴 사람 로직
    wr, wc, wd, wp, wg = player_info[win]
    if grid[wr][wc]:
        other_gun = max(grid[wr][wc])
        if other_gun > wg:
            grid[wr][wc].append(wg)
            wg = other_gun
            grid[wr][wc].remove(wg)
    player_info[win] = (wr, wc, wd, wp, wg)
    player_grid[wr][wc] = win


def move():
    for idx, player in enumerate(player_info):
        r, c, d, power, gun = player
        if not (0 <= r + row[d] < n and 0 <= c + col[d] < n):
            d = (d + 2) % 4
        nr = r + row[d]
        nc = c + col[d]
        if player_grid[nr][nc] == -1:  # 싸움 안함!
            if grid[nr][nc]:
                other_gun = max(grid[nr][nc])
                if gun < other_gun:
                    grid[nr][nc].remove(other_gun)
                    grid[nr][nc].append(gun)
                    gun = other_gun
            player_grid[nr][nc] = idx
            player_grid[r][c] = -1
            player_info[idx] = (nr, nc, d, power, gun)
        else:  # 싸움 함!
            player_info[idx] = (nr, nc, d, power, gun)
            o_idx = player_grid[nr][nc]
            o_r, o_c, o_d, o_power, o_gun = player_info[o_idx]  # 누구랑 싸울건데
            my_score = power + gun
            o_score = o_power + o_gun
            if my_score > o_score:
                win = idx
                lose = o_idx
            elif my_score == o_score:
                if power > o_power:
                    win = idx
                    lose = o_idx
                else:
                    win = o_idx
                    lose = idx
            else:
                win = o_idx
                lose = idx
            player_grid[r][c] = -1  # 일단 빈공간은 맞음
            ans[win] += abs(my_score - o_score)
            battle(win, lose)


n, player_num, time = map(int, input().split())
tmp = [list(map(int, input().split())) for i in range(n)]

grid = [[[] for i in range(n)] for i in range(n)]
player_grid = [[-1] * n for i in range(n)]
player_info = []
for p in range(player_num):
    r, c, d, power = map(int, input().split())
    player_grid[r - 1][c - 1] = p
    player_info.append((r - 1, c - 1, d, power, 0))
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if tmp[i][j]:
            grid[i][j].append(tmp[i][j])

ans = [0] * player_num

for t in range(time):
    move()
print(*ans)
