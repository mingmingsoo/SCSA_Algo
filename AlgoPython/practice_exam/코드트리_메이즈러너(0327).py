'''
문제 설명
    1. 참가자 이동
    2. 미로 회전
입력
    맵 크기 n, 참가자 수 m, 게임시간 k
    맵 정보 (1~9 벽)
    참가자 좌표
    출구좌표
출력
    참가자 이동거리합, 출구좌표
필요한 함수
    move()
    rotation() - 브루트포스, 회전 필요
필요한 변수
    grid - 벽 좌표, 탈출구 -1 처리
    player_grid - 3차원, 플레이어 맵

5 3 20
0 0 0 0 1
9 2 2 0 0
0 1 0 1 0
0 0 0 1 0
0 0 0 0 0
1 3
3 1
3 5
3 3

5 2 2
0 0 0 0 0
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0
0 0 0 0 0
1 2
2 2
4 2
'''
n, pn, time = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
player_grid = [[[] for i in range(n)] for i in range(n)]
for p in range(pn):
    r, c = map(lambda x: int(x) - 1, input().split())
    player_grid[r][c].append(p + 1)
er, ec = map(lambda x: int(x) - 1, input().split())
grid[er][ec] = -1
total_move = 0

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]

exit_num = 0


def move():
    global total_move, player_grid, exit_num
    new_grid = [[[] for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if player_grid[i][j]:
                for p in player_grid[i][j]:
                    move = False
                    cur = abs(i - er) + abs(j - ec)
                    for k in range(4):
                        nr = i + row[k]
                        nc = j + col[k]
                        if not (0 <= nr < n and 0 <= nc < n) or grid[nr][nc] > 0:
                            continue
                        next = abs(nr - er) + abs(nc - ec)
                        if next < cur:
                            if (nr, nc) != (er, ec):
                                new_grid[nr][nc].append(p)
                            else:
                                exit_num += 1
                            move = True
                            total_move += 1
                            break
                    if not move:
                        new_grid[i][j].append(p)
    player_grid = new_grid
    # print("이동 후")
    # for _ in player_grid:
    #     print(_)


def rotation():
    global er,ec
    L, R, C = 0, 0, 0
    for l in range(2, n + 1):
        for r in range(0, n - l + 1):
            for c in range(0, n - l + 1):
                is_exit = is_people = False
                for i in range(r, r + l):
                    for j in range(c, c + l):
                        if player_grid[i][j]:
                            is_people = True
                        if grid[i][j] == -1:
                            is_exit = True
                if is_exit and is_people:
                    L, R, C = l, r, c
                    break
            if L:
                break
        if L:
            break

    # print("선택한 사각형:", L, R, C)
    small_grid = [_[C:C + L] for _ in grid[R:R + L]]
    small_player_grid = [[__[:] for __ in _[C:C + L]] for _ in player_grid[R:R + L]]

    small_ro_grid = [[0] * L for i in range(L)]
    small_ro_player_grid = [[[] for i in range(L)] for i in range(L)]

    for i in range(L):
        for j in range(L):
            small_ro_grid[i][j] = small_grid[L - j - 1][i]
            if small_ro_grid[i][j] > 0:
                small_ro_grid[i][j] -= 1
            small_ro_player_grid[i][j] = small_player_grid[L - j - 1][i][:]
    # print("----------")
    # for _ in small_ro_grid:
    #     print(_)
    #
    # print("----------")
    # for _ in small_ro_player_grid:
    #     print(_)

    for i in range(L):
        for j in range(L):
            grid[i + R][j + C] = small_ro_grid[i][j]
            if grid[i + R][j + C] == -1:
                er, ec = i + R, j + C
            player_grid[i + R][j + C] = small_ro_player_grid[i][j][:]

    # print("----회전후------")
    # for _ in grid:
    #     print(_)
    #
    # print("----------")
    # for _ in player_grid:
    #     print(_)

for t in range(time):
    # print("-------",t,"------------")
    move()

    if exit_num == pn:
        break
    rotation()

print(total_move)
print(er+1,ec+1)

'''
# 체감난이도 골 1 - 하라는게 너무 많음

# 문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 09:00
    문제 종료 10:09

    총 풀이시간 69 분
        00~10   : 문제 이해, 손코딩(10)
        10~19   : 위 기반 주석, 필요한 변수/함수 세분화(9)
        19~25   : 입력받기(6)
        25      : 탑다운 설계(1)
        25~32   : move 함수 작성(7)
        32~37   : move 함수 확인(5)
                    1.
                    이동을 하긴 하는데 11번 플레이어가 두 곳에 들어가있는 것 아님?
                    이동 시키고 break를 안해줘서 여러번 들어갔음 break 추가!
                    2.
                    한 턴에 바로 탈출하는 경우 테케를 넣었는데
                    오잉 탈출을 안하고 오히려 탈출구보다 먼 곳으로 가는 것임?
                    아 er,ec를 block는 입력받은 값에 -1 해줘서 넣었는데
                    er,ec 자체에는 안해줘서 그냥 입력받을 때 -1 해주는 걸로 수정
                    er, ec = map(lambda x: int(x) - 1, input().split())
                    3.
                    한 턴에 2명 탈출하는 경우 ans 가 2가 잘 나오고,
                    다 탈출처리 되어있는지 확인
        39~57   : rotation 함수 작성(18) <- 문제 중 제일 신경써야할 부분
        39~44   : 1. 회전시킬 사각형 찾기(5)
                    최소 크기의 사각형을 선택할 때 하나라도 만족하면 그만 탐색하기 위해 flag 위치 신경써서 했음
        44~57   : 2. 회전 시키기(13)
                    2차원 배열 block 회전 먼저! (grid는 3차원이니까 일단 나중에..)
                    찍어보니까 어이쿠 반시계 회전이네 시계로 수정
                    3차원 배열 복사.. 가물가물 해서 기본 프레임으로 짠 다음에 변형하는걸로!
                    오키오키 3차원 배열도 복사도 잘 되고 회전도 잘된다

                    작은 배열 회전시켰으니까 작은 배열을 원본 배열에 반영하기!
                    반영 시키면서 벽은 -1과 탈출구 위치 갱신 처리 해줌!

        57~59 : all_exit 함수(2)
        57~09 : 검증 시작(12)
                1.
                문제 설명 처럼 맵 변화, 사람 이동 잘 되는지 확인
                어후 8초까지 있어서 까딱 놓치면 어? 왜 여깄지? 했음

                2.
                의심 될만한 테케 넣어보기
                (1) 참가자 0,0 이고 출구가 n-1,n-1인 경우 인덱스 에러 안나는지
                (2) 최소 정사각형 잘 선택 하는지
                (3) 두 명의 사람이 같은 곳에 잘 있는지 <= 이게 젤 걱정이였음
                (4) 모두 탈출했을 때 break 잘 되는지

  메모리 17 MB
  시간 63 ms

    회고
        1. 사랑들을 1차원 리스트로 관리하려다가
            최소 사각형 구할 때,,, 이 좌표를 가지는 사람이 있냐? 조회 연산이 필요해서 안썼다.
            그리고 회전도 따로 해줘야해서 안했음. 3차원 배열로 하면 맵 회전시킬때 같이 시키면 되기 때문
            (기억 의존 안하려고 했는데.. 자바로 풀었을 때는 사람들을 1차원 리스트로 했었다
            만약 내가 진짜 시험장이라면 이렇게 했을까? 생각이 들었는데
            아니... 관성을 따랐을 것 같음 그래서 그냥 자바 풀이랑 다르게 했다.)

        2. 아 근데 3차원 배열 회전이 이론상 되겠지 했는데 약간의 불안함은 있었음
            또 3차원 배열 deepcopy 슬라이싱으로 하는거 바로는 안됐다.
            [[col[:] for col in row[:]] for row in grid]
            이런식으로 적고 변형했다.
            [[col[:] for col in row] for row in cube] 이렇게만 해줘도 되는구나 ㅋㅋㅋ

        3.  또! 입력받을 때 실수 나왔다
            block = [list(map(int, input().split()))]
            2차원 배열 받을 때  for i in range(n) 뒤에 또 안붙힘
            입력 에러나서 수정 ㅎ 뭐 익숙한 에러라 빨리 찾음
            -> 잘 하고 있다만 입력 받고 잘 입력 받았는지 찍어보기 꼭!

        4. 킹이이이이야 아니 3차원 배열일 필요가 없었음
            사람은 한 번이라도 합쳐지면 이동 루트가 똑같기 때문에 !!!!!!!!!대박
            교수님 천재세요..........................
            다시 풀어보기!

        5. 손코딩, 검증 완료! 이렇게만.. 꾸준히!!!

# 문제 풀면서의 기록
문제 설명
    N*N
    1. 참가자 이동(동시) - new_grid 필요 3차원 배열
        (sr,sc) - (er,ec) 맨하튼 최단거리 - bfs 가 아니다
         for k in range(4) 돌면서 현재 거리보다 가까우면 바로 break 하고 이동
        move = True면 ans 에 더해준다. -> len(grid[i][j]) 더해주면 됨.

        - 참가자는 grid 에 10부터 인덱싱을 남겨준다.

    2. 미로 회전
        한명 이상 참가자 & 출구를 포함하는 가장 작은 정사각형임
        크기는 2~N까지가 될 거다.
        벽이 있었으면 내구도가 1씩 깎인다
        여기서 5중 포문이 필요하긴 한데,,, 발견시 튀는거라 ㄱㅊ을 듯
    - 주의
        모든 참가자 탈출시 게임 끝 : 확인해주는 로직 필요
입력
    맵크기 n 사람 수 m 시간 k
    사람 좌표
    출구 좌표
    좌표 -1 씩 필요
출력
    이동 거리 합, 출구좌표는 -1로 하겠음

- 필요한 변수
    grid, new_grid = 3차원 배열
    move_possible = boolean 변수 (이동할 수 있냐? True 면 답에 더해줌)
    people_have, exit_have = boolean 변수 (회전시 이 두개 만족해야 그 사각형으로 선택해 줄 것임)
    people_exit = [False]* 사람 수 = 다 탈출 했는지
- 필요한 함수
    move() : 참가자 이동
    rotation() : 미로 회전
    all_exit() : 다 탈출했는지 확인

-ㅇㅋㅇㅋ 출구는 빈공간, 참가자 좌표랑 겹치지 않음

사람이 0,0 출구가 n-1,n-1 일떄 인덱스 에러 안나는지 확인 필요
사람이 한명이라도 있으면 사각형 생기는지 확인 필요


참가자 0,0 이고 출구가 n-1,n-1인 경우 인덱스 에러 안나는지
5 1 1
0 1 0 0 0
1 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1
5 5

두 명의 사람이 같은 곳에 잘 있는지
5 2 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
4 5
5 5
1 5

break 잘 되는지
5 3 100
0 0 0 0 1
9 2 2 0 0
0 1 0 1 0
0 0 0 1 0
0 0 0 0 0
1 3
3 1
3 5
3 3
'''
# ------------------- 입력 ----------------------------
n, people_num, time = map(int, input().split())
block = [list(map(int, input().split())) for i in range(n)]

grid = [[[] for i in range(n)] for i in range(n)]

p_idx = 10
for p in range(people_num):
    r, c = map(int, input().split())
    grid[r - 1][c - 1].append(p_idx)
    p_idx += 1

er, ec = map(lambda x: int(x) - 1, input().split())
block[er][ec] = -1

people_exit = [False] * (people_num)
ans = 0

row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]


# ------------------- 함수 ----------------------------
def move():
    global ans, grid
    new_grid = [[[] for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                move = False
                cur = abs(er - i) + abs(ec - j)
                for k in range(4):
                    nr = i + row[k]
                    nc = j + col[k]
                    if not (0 <= nr < n and 0 <= nc < n) or block[nr][nc] > 0:  # 벽만 못간다
                        continue
                    next = abs(er - nr) + abs(ec - nc)
                    if next < cur:
                        move = True
                        if (nr, nc) == (er, ec):  # 만약 출구면
                            for pidx in grid[i][j]:
                                people_exit[pidx - 10] = True
                            ans += len(grid[i][j])  # 값만 더해주고 안넣어준다
                        else:
                            new_grid[nr][nc].extend(grid[i][j])
                            ans += len(grid[i][j])
                        break
                if not move:  # 움직이지 못했으면 그냥 원래 그자리
                    new_grid[i][j].extend(grid[i][j])
    grid = new_grid


def rotation():
    global er, ec
    L, R, C = 0, 0, 0
    for length in range(2, n + 1):  # 사각형 크기
        is_length = False
        for r in range(0, n - length + 1):
            for c in range(0, n - length + 1):
                people_have, exit_have = False, False
                # 내가 선택한 사각형
                for i in range(r, r + length):
                    for j in range(c, c + length):
                        if block[i][j] == -1:
                            exit_have = True
                        if grid[i][j]:
                            people_have = True
                if people_have and exit_have:
                    is_length = True
                    L, R, C = length, r, c
                    break
            if is_length:
                break
        if is_length:
            break

    small_block = [_[C:C + L] for _ in block[R:R + L]]
    small_grid = [[__[:] for __ in _[C:C + L]] for _ in grid[R:R + L]]

    small_lo_block = [[0] * L for i in range(L)]
    small_lo_grid = [[[] for i in range(L)] for i in range(L)]

    for i in range(L):
        for j in range(L):
            small_lo_block[i][j] = small_block[L - j - 1][i]
            small_lo_grid[i][j] = small_grid[L - j - 1][i][:]

    for i in range(L):
        for j in range(L):
            if small_lo_block[i][j] > 0:
                small_lo_block[i][j] -= 1
            block[i + R][j + C] = small_lo_block[i][j]
            grid[i + R][j + C] = small_lo_grid[i][j][:]
            if block[i + R][j + C] == -1:
                er, ec = i + R, j + C


def all_exit():
    for pepple in people_exit:
        if not pepple:
            return False
    return True


# ------------------- 메인 ----------------------------
for t in range(time):

    move()
    print("-----움직여-------")
    for _ in grid:
        print(" ".join(f"{num:2}" for num in _))
    rotation()  # er,ec 갱신 필요
    print("-----회전해-------")
    for _ in grid:
        print(" ".join(f"{num:2}" for num in _))
    if all_exit():
        break
print(ans)
print(er + 1, ec + 1)
