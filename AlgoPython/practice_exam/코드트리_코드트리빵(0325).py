'''
# 04.06.일 2회차 풀이
# 코드트리 코드트리빵

# 문제 풀고 나서 기록

    제출 횟수 1회
    문제 시작 12:29
    문제 종료 15:15
    총 풀이시간 34분
        29~38   : 문제 이해 및 손코딩(9)
        38~41   : 위 기반 주석, 입력받기(3)
        41~48   : 탑다운 설계(7)
        48~51   : 편의점 이동 로직(3)
        51~55   : 베이스캠프 이동 로직(4)
        55~02   : 검증(7)

    메모리 16 MB
    시간 56 ms

    회고
        1. 자꾸 enumerate를 안쓰네.... 리스트업에 추가

# 문제 풀면서의 기록
문제 설명
    1. 편의점 이동
    2. 편의점 도착
    3. 베켐 이동
필요한 함수
    con_go
    base_go
필요한 변수
    block
    block_tmp
    player_lst
    grid - 베이스 캠프를 나타냄
'''
from collections import deque

n, pn = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
player_end = [tuple(map(lambda x: int(x) - 1, input().split())) for i in range(pn)]

player_lst = [(-1, -1) for i in range(pn)]
block = [[0] * n for i in range(n)]

time = 0

row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]


def con_go(idx, r, c):
    er, ec = player_end[idx]
    visited = [[False] * n for i in range(n)]
    visited[r][c] = True
    q = deque([(r, c, [])])
    while q:
        r, c, path = q.popleft()
        if (r, c) == (er, ec):
            return path[0][0], path[0][1]

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or block[nr][nc]:
                continue
            visited[nr][nc] = True
            q.append((nr, nc, path + [(nr, nc)]))


def base_go(idx):
    # 편의점에서 가까운 베켐 찾기
    base = []
    er, ec = player_end[idx]
    visited = [[False] * n for i in range(n)]
    visited[er][ec] = True
    q = deque([(er, ec)])
    while q:
        for qs in range(len(q)):
            r, c = q.popleft()
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or block[nr][nc]:
                    continue
                visited[nr][nc] = True
                q.append((nr, nc))
                if grid[nr][nc] == 1:
                    base.append((nr, nc))
        if base:
            base.sort()
            return base[0][0], base[0][1]


def is_end():
    for idx, location in enumerate(player_lst):
        if location != player_end[idx]:
            return False
    return True


while True:
    block_tmp = []
    # 1. 편의점 이동
    # print("==",time,"==")
    # print("before", player_lst)
    for idx, location in enumerate(player_lst):
        if location == player_end[idx]:  # 이미 도착
            continue
        if location == (-1, -1):  # 베켐도 못감
            continue
        r, c = location
        nr, nc = con_go(idx, r, c)
        player_lst[idx] = (nr, nc)
        if (nr, nc) == player_end[idx]:
            block_tmp.append((nr, nc))

    for block_r, block_c in block_tmp:
        block[block_r][block_c] = 1
    # 2. 베켐 이동
    for idx, location in enumerate(player_lst):
        if idx <= time and location == (-1, -1):
            br, bc = base_go(idx)
            player_lst[idx] = (br, bc)
            block_tmp.append((br, bc))
    for block_r, block_c in block_tmp:
        block[block_r][block_c] = 1
    # print("after", player_lst)
    time += 1
    if is_end():
        break

print(time)

'''
# 체감난이도 골3 인데 아 진짜 문제 설명이 너무 불친절함. 그래서 골1


# 문제 풀고 나서 기록
    제출 횟수 3회
    문제 시작 14:00
    1차 제출  14:57 (99번 틀림)
    2차 제출  15:04 (런타임 에러)
    문제 종료 16:25

    총 풀이시간 145분
        00~17   : 문제 이해, 초기 주석 및 ☆손코딩☆(17)
        17~26   : 탑다운 설계(9)
        26~40   : 편의점 - 베이스캠프 bfs 로직(14)
                    스타트 택시 문제였나? 그때 처럼 편의점에서 모든 베이스캠프의 거리를 담았다가
                    q_size만 돌게해서 같은 distance에서 발견하면 끝나는 로직으로 시간 단축하게 했음!(땡스포 완진)
        40~47   : 손님 - 편의점 bfs 로직(7)
                    최단 거리 이므로 한 루트만 발생하면 break 하게 했음
                    그리고 손님은 한 칸 이동이므로 그 루트들 중 맨 첫번째로만 이동함
        47~57   : 코드 작성 완료 디버거로 잘 되나 확인(10)
                    이미 도착한 애들은 안 살펴봐도 되기에 시간을 단축하고자
                    # 0. 이미 도착한 애들은 건너뛰어!
                    if player == player_end[idx]:
                        continue 추가!
                (+) 시간이 다른 문제들보다 빡빡해서 최대값 테케 만들어서 넣어보기
        57~04   : 1차 제출 -> 틀렸습니다(7)
                    근데 99번 테케여서 안봤음
                    아니 99번에서 틀리는건 뭐냐고요...ㅋㅋㅋㅋㅌㅋㅀ훙푸항
                    문제 다시 읽기
                    "아~~ 한 턴이 끝나야 벽처리를 해주는거네"
                    벽을 그때그때 처리했는데 턴 끝나고 벽처리 하는 걸로 수정
        04~25   : 2차 제출 -> 런타임 에러(81)
                    이번엔 5번 테케였음
                    런타임 에러라니 띠용?
                    분석 시작...........
                    한시간 넘게 5번테케 답이 왜 7인지 그려봤음
                    도저히 답이 7이 나올 수가 없는데....................................
                    관련해서는 회고에 써놨음
        25      : 맞췄다!!!!!!!ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
                    어느때보다 즐거웠던듯 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ

  메모리 16 MB
  시간 49 ms

    회고
        1. ................................
            진짜 내가 멍청인건지 문제를 원망해야하는건지
            "격자에 있는 모든 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없어짐"
            여기서 베이스캠프로 가는 애들은 저 지나갈 수 없는 칸을 못가는거에 해당한다는 게 진짜 열불나네
            말을 똑바로해야지!!! ㅠㅠ 베이스캠프로 가면 격자 in 아니냐고...
            하 물론 출발지는 ,,, 격자밖이지만요 ,,,,,
            4 5
            1 0 1 1
            1 0 1 1
            0 0 0 1
            1 0 1 1
            4 2
            3 1
            3 3
            3 2
            1 2

            이 테케 답은 7인데 도도도도도저히 7이 나올 수가 없는데!!!!!!!!!!!!!!!!!!
            7이 나오는 방법은 4번째 손님이 베켐을 갈 때 3번 편의점을 못가야만 7이 나오는데
            time이 4일 때 [3번 손님 편의점 도착 & 4번 손님 베켐 도착]
            이게 동시에 일어나는데!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            어케 4번 베켐이 3번 손님편의점을 지나갈 수가 있냐고요~~~~~~~
            ... 여하튼..... ... 뭐 제 잘못이죠...
            격자 밖에서 오는건 맞잖아요....

        2. 나연이 따라 손코딩 하고 들어갔는데
            코드 실수 없이 빠르게 작성할 수 있었음!!
            물론 문제 이해를 잘못해서 디버깅하는데 한 세월 썼지만
            손코딩 진짜 좋은듯?!?!
            대충이라도 적자!!!!!

        3. 그래도
            while q:
                q_size = len(q)
                for qs in range(q_size):
            요렇게 q_size만큼 돌아서 베이스캠프 발견하면 끝나게한거는 잘했다.
            발전했다 ㅇㅈ

# 문제 풀면서의 기록
문제 설명
    m명의 사람이 정확히 m분에 각자의 베이스 캠프에서 출발해 편의점으로 이동 시작
    사람들은 출발시간이 되기 전까지 격자 밖에 있고, 모두 다른 편의점을 목표로 함
    1분 동안 진행되는 행동
    1. 격자에 있는 사람들은 가려는 편의점을 향해 1칸씩 움직임
        우선순위 ^ < > v
    2. 편의점에 도착하면 그 편의점이 벽이됨 -> 이래서 bfs가 필요할 듯
    3. 현재 시간이 t분이고 t<=m 을 만족하면 t번 사람은 편의점 가까이에 있는 베이스캠프에 들어감
        여러가지면 행이 작고 열이 작은
        베이스캠프에 사람 있으면 그 칸 못지나감
헷갈리는 거
    2. 격자에 있는~ 유의합니다. 이해 안됨 -> 이거때문에 틀림 ! 그래도 기록은 잘 해뒀다..
    베켐에서 나오면 지나갈 수 있는지? -> 아닌 듯 그냥 벽처리
    사람들은 겹쳐도 된다.
구상
    1. 격자밖인지 검사
        -> 격자밖이 아니면 bfs 돌려서 이동
    2. 편의점이면 편의점 벽처리
    3. 베켐갈 수 있으면 베켐가 -> 이것도 bfs 필요!!
    4. 플레이어 == 편의점이면 break

15 30
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
3 1
3 2
3 3
3 4
3 5
3 6
3 7
3 8
3 9
3 10
3 11
3 12
3 13
3 14
3 15
4 1
4 2
4 3
4 4
4 5
4 6
4 7
4 8
4 9
4 10
4 11
4 12
4 13
4 14
4 15


아 바로 block 하면 안되고
격자에 있는 모든 사람들이 이동 한 뒤에임!!!!!!!!!

'''
from collections import deque


def base_go(idx):
    cr, cc = player_end[idx]  # 편의점 위치
    # 편의점 위치에서 베켐중 가까운 거리를 찾는다.
    possible = []
    q = deque([(cr, cc, 0)])
    visited = [[False] * n for i in range(n)]
    visited[cr][cc] = True

    while q:
        q_size = len(q)
        for qs in range(q_size):
            r, c, dist = q.popleft()
            if grid[r][c] == 1:
                possible.append((dist, r, c))
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or block[nr][nc]:
                    continue
                visited[nr][nc] = True
                q.append((nr, nc, dist + 1))
        if possible:
            possible.sort()
            dist, r, c = possible[0]
            return r, c


def con_go(idx):
    r, c = player_lst[idx]  # 현재 플레이어 위치
    er, ec = player_end[idx]  # 편의점 위치
    q = deque([(r, c, 0, [])])  # 위치 거리, 경로
    visited = [[False] * n for i in range(n)]
    visited[r][c] = True
    possible = []
    while q:
        r, c, dist, path = q.popleft()
        if (r, c) == (er, ec):
            possible = path
            break
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or block[nr][nc]:
                continue
            visited[nr][nc] = True
            q.append((nr, nc, dist + 1, path[:] + [(nr, nc)]))
    return possible[0][0], possible[0][1]


n, player_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
block = [[0] * n for i in range(n)]

player_lst = []
for p in range(player_num):
    player_lst.append((-1, -1))

player_end = []  # 목적지
for p in range(player_num):
    r, c = map(int, input().split())
    player_end.append((r - 1, c - 1))

time = 0

row = [-1, 0, 0, 1]  # 이렇게 해도 우선순위가 되나?ㅜㅜ ㅇㅇ 된다
col = [0, -1, 1, 0]

while True:
    block_lst = []
    for idx, player in enumerate(player_lst):

        # 0. 이미 도착한 애들은 건너뛰어!
        if player == player_end[idx]:
            continue

        # 1. 가까운 편의점으로 이동
        if player != (-1, -1):
            nr, nc = con_go(idx)
            player_lst[idx] = (nr, nc)

        # 2. 편의점 도착했으면 벽처리
        er, ec = player_end[idx]
        if player_lst[idx] == (er, ec):
            block_lst.append((er, ec))

        # 3. 베켐 갈 수 있으면 베켐 가
        if time >= idx:
            if player == (-1, -1):  # 근데 베켐애들은 격자밖에서 이동하는거라 벽처리 해줘야함
                while block_lst:
                    r, c = block_lst.pop()
                    block[r][c] = 1
                base_r, base_c = base_go(idx)
                player_lst[idx] = (base_r, base_c)
                block_lst.append((base_r, base_c))
        else:
            break
    while block_lst:  # 만약 베켐 갈 수 있는 애들이 없었으면 벽처리가 안돼서 턴 끝나고 한번 더
        r, c = block_lst.pop()
        block[r][c] = 1
    time += 1
    if player_lst == player_end:
        break
print(time)
