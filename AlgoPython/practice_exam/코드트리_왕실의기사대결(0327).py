'''
# 코드트리 왕실의 기사 대결
2025.04.06.일
두번째 풀이

# 문제 풀고 나서 기록
    제출횟수 1회
    문제 시작 15:17
    문제 종료 16:04

    총 풀이시간 47분
        17~28   : 문제이해 및 손코딩(11)
        28~33   : 위 기반 주석 및 입력 받기(5)
        33~42   : bfs 함수 설계 - 밀림 연쇄작용(9)
        28~52   : bfs 함수 확인(24)
                    - 기사 직사각형 크기는 동일하니께 ,w 는 증가시킬 필요가 없음 수정!
                    - 오타 발견 미친거아녀
                        idx, n, c, h, w = q.popleft()
                     -> idx, r, c, h, w = q.popleft() 수정
        52~58   : 피 깎는 로직(6)
                    for i in range(r, r + h):
                        for j in range(c, c + w):
                    한 칸 이동한 범위에 함정있는지 봐줘야함 수정!
                    
                    for i in range(nr, nr + h):
                        for j in range(nc, nc + w):
        58~04 : 검증(6)

  메모리 19 MB
  시간 94 ms
  
  회고
    1. bfs 검증시간이 더 기네.. 오타 조심하자

# 문제 풀면서의 기록
문제설명
    1. 기사이동
    2. 데미지
8 5 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
2 1 2 1 1
2 2 2 1 1
2 3 2 1 1
2 4 2 1 1
2 5 2 1 1

8 5 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 2 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
2 1 2 1 1
2 2 2 1 1
2 3 2 1 1
2 4 2 1 1
2 5 2 1 1
1 1
'''
from collections import deque

n, pn, on = map(int, input().split())
grid = [[2] * (n + 2)] + [[2] + list(map(int, input().split())) + [2] for i in range(n)] + [[2] * (n + 2)]
n += 2
player_grid = [[0] * n for i in range(n)]
player_lst = [0]
for p in range(pn):
    r, c, h, w, hp = map(int, input().split())
    player_lst.append((r, c, h, w, hp, 0))
    for i in range(r, r + h):
        for j in range(c, c + w):
            player_grid[i][j] = (p + 1)
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


def bfs(idx, nr, nc, nh, nw):
    visited = [False] * (pn + 1)
    visited[idx] = True
    q = deque([(idx, nr, nc, nh, nw)])
    tmp = []
    while q:
        idx, r, c, h, w = q.popleft()
        tmp.append(idx)
        for i in range(r, r + h):
            for j in range(c, c + w):
                if grid[i][j] == 2:
                    return []
                if player_grid[i][j] and not visited[player_grid[i][j]]:
                    visited[player_grid[i][j]] = True
                    pr, pc, ph, pw, php, pdamage = player_lst[player_grid[i][j]]
                    npr, npc = pr + row[d], pc + col[d]
                    q.append((player_grid[i][j], npr, npc, ph, pw))

    return tmp


for o in range(on):
    idx, d = map(int, input().split())
    if not player_lst[idx]:
        continue
    r, c, h, w, hp, damage = player_lst[idx]
    nr, nc = r + row[d], c + col[d]
    move_lst = bfs(idx, nr, nc, h, w)
    if not move_lst:  # 이동 불가
        continue
    for pidx in move_lst:
        r, c, h, w, hp, damage = player_lst[pidx]
        nr = r + row[d]
        nc = c + col[d]
        if pidx != idx:
            sick = 0
            for i in range(nr, nr + h):
                for j in range(nc, nc + w):
                    if grid[i][j] == 1:
                        sick += 1
            hp -= sick
            damage += sick
        if hp <= 0:
            player_lst[pidx] = 0  # 쥬금
        else:
            player_lst[pidx] = (nr, nc, h, w, hp, damage)
    player_grid = [[0] * n for i in range(n)]
    for pidx, player in enumerate(player_lst):
        if player == 0:
            continue
        r, c, h, w, hp, damage = player
        for i in range(r, r + h):
            for j in range(c, c + w):
                player_grid[i][j] = pidx


ans = 0

for pidx, player in enumerate(player_lst):
    if player == 0:
        continue
    r, c, h, w, hp, damage = player
    ans += damage
print(ans)

'''
# 체감난이도 골1~플5

# 문제 풀고 나서 기록
    제출 횟수 2회
    문제 시작 14:00
    1차  제출 15:42
    문제 종료 15:52

    총 풀이시간 112분
        00~25   : 문제 이해 및 손코딩(25) - 중간 화장실 3분
        25~30   : 위 기반 초기 주석 및 필요한 변수/함수 세분화(5)
        30~34   : 입력받기(4)
        34~35   : 탑 다운 설계(1)

        35~51   : move 함수 설계(16)
        51~56   : move 함수 확인(5)
                  1. 입력 받을 때 기사의 범위 r~x, c~y 넣어놓고
                     막상 벽 검사는 r~r+x, c~c+y 이렇게 했음
                     그래서 다 벽에 걸려버려서 범위 수정!
                  2. break 조건이 if move_possible 이 아니라
                     if not move_possible 이여야 함.... 수정!
                  3. 아니 벽 2라고 왜 벽을 1라고 썼을까^^ 수정!

        56~10   : minus_hp 함수 설계 하다 말고 패딩(14)
                  이제 여기서 격자 밖 나가는 애들 처리 해야지..
                  '근데 진짜 격자 밖 나가?' 싶어서 문제 다시 읽음
                  '격자 밖에 나가는 애들도 있다' 라는 말이 아무데도 안써있는거야....
                  근데 맨 윗 문단에 적혀있네요,.... 격자 밖은 벽으로 간주..
                  급하게 패딩 .. 패딩
                  근데 패딩하면 분명 범위가 달라지는 애들이 있을 거란 말이지? 코드 검토
                  내가 기사 좌표를 -1 해서 받았는데
                  패딩하면 +1 되므로 r-1 한거 없애줌!!!
        10~13   : 이제 진짜 minus_hp 함수 설계 ㅎ(3)
        13~35   : minus_hp 함수 확인(벽이 1 인지 함정이 2 인지 아직도 헷갈려하는 중;)(22)
                    1.
                    remove 해줄 때 뒤에서부터 안해도 될 것 같았는데 아니였음
                    뒤에서 부터 range 변경
                    2.
                    아.. 공격한애는 데미지 안먹는 구나 아차차..
                    공격한 애는 제외하고 데미지 먹게 변경
                    3.
                    grid = new_player_grid 이러고 있네
                    player_grid = new_player_grid 이거임 . 수정 완
                    4.
                    아 왕은 기사의 번호를 부르는 구나 .. 나는 인덱스로 기사를 넘버링 해줬음
                    그러면 당연히 안됨..
                    player_lst 를 딕셔너리로 변경
        35~38   : 답이 5가 나오네..(3)
                    아 ! 이동안한 애들도 피깎아주고 있네
                    pid가 move_lst 에 없으면 continue 하게 해줌
                    (여기서.... 1회틀 로직 잡아낼 수 있었을텐데 까비_
        38~42   : 검증 시작(4)
                    0. 문제 예시랑 동일한지
                    1. 사라진 기사 호출 테케 -> 오 키에러 떠서 수정완
                    2. 벽때문에 못밀어지는 테케
        42~52   : 틀려도 하필 38번 테케 .....(10)
                    로직이 완벽해보임 어디가 잘못됐는지 모르겠음
                    틀렸다면 기사 제거해주는 부분일텐데...
                    딕셔너리를 썼으니까 굳이 range로 안하고 move_lst에 들어있는 키들만 제거해줘도 되겠다. 해서 수정
        52      : 맞췄다!!!ㅠㅠㅠㅠㅠㅠ 근데 왜 맞았지?
        52~     : 왜 틀렸고, 맞았는지 분석!

  메모리 18 MB
  시간 74 ms

    회고
        1. 흐어 player_lst 를 처음부터 dict 로 했었어야 했는데 놓쳤다.
            왕이 n번 기사 움직여! 할 때 n번은.. 리스트의 인덱스가 될 수 없기 때문이다 ㅠㅠ
            아차차 그걸 놓쳐서 dict로 바꿨는데 그래서 데미지 먹는 함수에 영향을 끼쳤다..
            왜냐하면 데미지 먹는 함수는 lst 기반으로 짰기 때문....
            알아내서 정말 천만 다행...............
            로직만 신경쓰고 자료형 신경 못쓴게 아쉽......
            좋은 경험이다.!!!!!!!!!!!!!

        2. "격자 밖도 벽으로 간주" 이걸 늦게본게 진짜 바보 천치같음
            문제 풀면서 "오잉? 밖으로 나가는 애들은 없나?" 생각이 들었을때 다시 읽어봤어야 하는데ㅠㅠ 패딩을 나중에 했심...

        3. 문제 중간중간 벽이 1 인지 함정이 2인지 헷갈려서 이리저리했음
            어디 크게 써놓지 바보야

        4. minus_hp를 너무 대충 생각한듯
            이건 쉽지~ 라고 했는데 함수 짜는덴 5분 디거빙만 22분 했음
            반성하도록.

        5.  그래도 잘한 점은
            벽 만나는 걸 어떻게 처리하지? 를 고민 많이 하고 들어갔다
            dfs를 써야하나 생각도 했지만 그건 너무 어려울 것 같고....
            q를 쓴 건 잘 한 생각!! 굿굿굿

        6.
        for pid in range(len(player_lst) - 1, -1, -1):
        player_lst 는 딕셔너린데 예를들어 길이가 10이여도
        기사 넘버가 28인 애가 들어있을 수 있음!!
        그래서 움직일때 기사 넘버가 28인 애들은 pid 에 해당이 안돼서 그런겅임!!!!
        유레카 유레카!!
        key를 pop 해주기 때문에 reverse 도 안해줘도됨!!



# 문제 풀면서의 기록
어렵다.
문제 설명
    1. 기사 이동
        - d 방향으로 한 칸 이동
        - 다른 기사가 있으면 연쇄적으로 이동
        - 벽 있으면 불가
        - 격자 밖으로 쫓겨날 수도 있음
        - 체스판에서 사라진 기사도  호출 될 수 있음, 반응은 X
    2. 대결
        - 이동한 곳에 함정 수 만큼 대미지 먹음
        - 0되면 사라짐
        - 민 기사도 일단 이동 후에 대미지 받음 얘도 0되면 사라짐
구상
    1번이 어려운데 q를 써서 해보자.
    벽 만나면 False 줘서 이동 안하게 하겠다
    그리고 가면서 이동시켜야 하는 애들의 넘버를 [] 기록해두고
    걔네를 한번에 이동 시킨다.
    이동 시키고 나서 r,c 가 범위 벗어나면  remove 해준다 나간거니까

입력
    맵 크기 l, 기사수 n, 명령수 q
    맵 정보
    기사 정보
    명령 정보
출력
    생존한 기사들이 받은 대미지의 합? wow
필요한 변수
    player_lst = [(sr,sc,er,ec,power), ...]
    player_map 2차원 배열 -1로 초기화하고 넘버만 표시
    grid 2차원 배열 벽과 함정만
필요한 함수
    move() - 여기서 근데 좀 어려울 듯 이동 가능한지를 일단 알아놔야됨
    minus_hp() - 이동시킨거 기반 피깎기

궁굼한게 기사 이동시켰는데 지혼자 격자밖으로 나가는 경우도 있음? 아니면 한칸만이나??
아 체스밖도 벽으로 간주...?


4 3 4
0 0 1 0
0 0 1 0
1 1 0 1
0 0 2 0
1 2 2 1 5
2 1 2 1 1
3 2 1 2 3
1 2
2 1
3 3
2 0

사라진 기사 호출


4 3 1
0 0 0 0
0 0 0 0
0 0 0 0
2 2 2 2
1 1 1 2 5
2 1 1 2 5
3 1 1 2 5
1 2

안밀려요
'''

# -------------------------- 입력 --------------------------
from collections import deque

n, player_num, order_num = map(int, input().split())
grid = [[2] * (n + 2)] + [[2] + list(map(int, input().split())) + [2] for i in range(n)] + [[2] * (n + 2)]
n += 2

player_lst = {}
player_grid = [[-1] * n for i in range(n)]  # 나중에 꼭 -1로 바꾸기!!!!!!!!!!!!!!!!!
for p in range(player_num):
    r, c, x, y, power = map(int, input().split())
    player_lst[p] = [r, c, r + x, c + y, power, 0]  # 받은 데미지의합
    for i in range(r, r + x):
        for j in range(c, c + y):
            player_grid[i][j] = p

order_lst = []
for i in range(order_num):
    idx, d = map(int, input().split())
    order_lst.append((idx, d))

row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


# -------------------------- 함수 --------------------------
def move():  # 이동 가능한지만 본다.
    q = deque([(p_id - 1, player_lst[p_id - 1])])
    visited = [False] * player_num
    visited[p_id - 1] = True
    while q:
        pid, player = q.popleft()
        r, c, x, y, power, damage = player
        move_lst.append(pid)
        nr, nc, nx, ny = r + row[d], c + col[d], x + row[d], y + col[d]
        for i in range(nr, nx):
            for j in range(nc, ny):
                if player_grid[i][j] != -1:  # 다른 애도 이동 시켜줘야함..
                    if not visited[player_grid[i][j]]:
                        q.append((player_grid[i][j], player_lst[player_grid[i][j]]))
                        visited[player_grid[i][j]] = True
                if grid[i][j] == 2:  # 벽이면 안돼!!!!
                    return False
    return True


def minus_hp(origin_p_id):
    global player_grid
    # 일단 전부 이동부터 시켜주고요..
    for pid in move_lst:
        player_lst[pid][0] += row[d]
        player_lst[pid][1] += col[d]
        player_lst[pid][2] += row[d]
        player_lst[pid][3] += col[d]

    for pid in move_lst:
        # 공격한애는 데미지 안먹는다!
        if pid == origin_p_id:
            continue
        player = player_lst[pid]
        r, c, x, y, power, damage = player
        sick = 0  # 아야
        for i in range(r, x):
            for j in range(c, y):
                if grid[i][j] == 1:  # 데미지 감소!
                    sick += 1
        power -= sick
        damage += sick
        if power <= 0:
            player_lst.pop(pid)
        else:
            player_lst[pid][4] = power
            player_lst[pid][5] = damage

    # 그 다음에 맵에 반영!
    new_player_grid = [[-1] * n for i in range(n)]
    for pid, player in player_lst.items():
        r, c, x, y, power, damage = player
        for i in range(r, x):
            for j in range(c, y):
                new_player_grid[i][j] = pid

    player_grid = new_player_grid


# -------------------------- 메인 --------------------------
for p_id, d in order_lst:
    if (p_id - 1) not in player_lst:  # 체스판에 없어요..
        continue
    move_lst = []
    if move():
        minus_hp(p_id - 1)

ans = 0
for pid, player in player_lst.items():
    ans += player[5]
print(ans)
