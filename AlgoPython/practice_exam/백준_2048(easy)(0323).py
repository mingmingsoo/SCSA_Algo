'''

# 0323 2회차 풀이
# 코드트리 2048게임 (백준 주사위 굴리기)
# 체감난이도 골3~골4

# 문제 풀고 나서 기록

    제출횟수 1회
    문제 시작 16:26
    문제 종료 16:46
    총 풀이시간 20분
        26~28   : 문제 이해(2)
        28~30   : 초기주석 및 문제 구상(2)
        30~35   : 주석으로 단 1,2,3을 3,1,2 로 설계 / 일단 3만 설계!
                    3. 격자판 밖으로 이동하라는 명령은 무시
                    1. 정육면체를 굴리는데 격자판이 0이면 주사위 바닥면에 쓰여있는 수가 격자판에 복사
                    2. 격자판이 0이아니면 칸에 쓰여있는 수가 주사위 바닥에 복사되고 그 칸은 0이됨
        35~42   : 주사위 굴리는 roll 설계 - index로(7)
        42~43   : 나머지 1,2 설계(1)
        43~45   : 인덱스 에러나서 디버깅(2)
                    roll 함수에서 dice를
                    [dice[4] + dice[5] + dice[2] + dice[3] + dice[1] + dice[0]]
                    더해버렸네... + 에서 , 로 수정
                    -> [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]
        45~46   :   오잉 답이 안나오네?(1)
                    아 주사위 위치 바꿔주고 갱신해주는 코드가 없네!
                        r= nr, c = nc 추가!

    메모리 16 KB
    시간 60 ms

    회고
        1. 처음 주말 스터디에서 풀었을 땐 (주사위 바닥에 복사되고 그 칸은 0이됨) 이 조건을 놓쳐서 디버깅하는데 시간 오래걸렸었는데
            문제를 읽으면서 조건을 기록해둬서 이번엔 안놓치고 빨리 풀 수 있었다!
        2. 확실히 1회차 풀이보다 간단히 풀었네!!!

# 문제 풀면서의 기록
16:50 시작
17:10 종료

문제설명
    두가지 동작
    1. 중력
    2. 합침
        단 합쳐질때 2 2 2 2가 있으면
        (2 2) (2 2) 이렇게 한번씩만 합쳐져서
        4 4 가 된다.
    5번 상하좌우 이동하여 얻을 수 있는 가장 큰 블록의 수

구상
    1. duple_perm : 방향의 순서를 정해주는 중복 순열
            00000도 가능
    2. game : 방향 순서대로 게임 시작
        - 중력
        - 합쳐
        - 중력
입력
    초기 상태 2048
출력
    게임 끝난 후 2048의 최댓값
'''

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

sel = [0] * 5
ans = 0


def rotation(game_grid):
    grid = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            grid[i][j] = game_grid[n - j - 1][i]
    return grid


def gravity(game_grid):
    # 북쪽으로 땡긴당
    for j in range(n):
        while True:
            down = 0
            for i in range(n - 1):
                if game_grid[i][j] == 0 and game_grid[i + 1][j] != 0:
                    down += 1
                    game_grid[i][j], game_grid[i + 1][j] = game_grid[i + 1][j], game_grid[i][j]
            if not down:
                break


def merge(game_grid):
    # 북쪽으로 합친당
    for j in range(n):
        idx = 0
        while idx < n - 1:
            if game_grid[idx][j] and game_grid[idx][j] == game_grid[idx + 1][j]:
                game_grid[idx][j] *= 2
                game_grid[idx + 1][j] = 0
                idx += 1
            idx += 1


def duple_perm(idx):
    global ans, game_grid
    if idx == 5:
        # 여기서 게임진행
        game_grid = [_[:] for _ in grid]

        for d in sel:
            for ro in range(d):
                game_grid = rotation(game_grid)

            gravity(game_grid)
            merge(game_grid)
            gravity(game_grid)

        maxi = 0
        for i in range(n):
            for j in range(n):
                maxi = max(maxi, game_grid[i][j])
        ans = max(ans, maxi)

        return

    for i in range(4):
        sel[idx] = i
        duple_perm(idx + 1)


duple_perm(0)
print(ans)
