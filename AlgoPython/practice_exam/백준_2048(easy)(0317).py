'''
# 0323 2회차 풀이(3회차 안해도 될듯)
# 코드트리 2048 게임 (백준 2048(easy))
# 체감난이도 골2

# 문제 풀고 나서 기록

    제출 횟수 1회
    문제 시작 16:50
    문제 종료 17:11
    총 풀이시간 21분
        50~51   : 문제 이해(1)
        51~53   : 초기 주석 및 문제 구상(2)
        53~55   : duple_perm 설계(2)
        55~00   : rotation 설계(5)
        00~02   : gravity 설계(2)
        02~05   : merge 설계(3)
        05~09   : 오픈테케 답이 안나오네! 디버깅
                    duple_perm 함수 안에서 생성한 game_grid는 전역변수로 관리 안되는데
                    이걸 놓쳤음 (오류가 안나서 될 줄..)
                    회전한 배열을 return 하는 걸로 수정
        09~11   : 다른 함수들도 잘 되는지 디버거로 확인!(2)

    메모리 294 MB
    시간 23 ms

    회고
        1. rotation에서 메모리 안먹을라고 이게 되나? 싶어서 duple_perm 함수 안에서 생성한 game_grid를 수정하는 코드를 짰는데
            역시나 안됐다!
            허튼짓 하지말고 함수 안에서 grid 생성하고 return 하도록!!!
        2. 1회차 코드리뷰때 봤던 다른 친구들 풀이처럼
            합쳐지면서 바로바로 댕기는 코드로 다시 짜봤는데 시간 차이는 별로 없음..!


# 문제 풀면서의 기록
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

시간복잡도
    경우의 수 4*5 = 1024
    시뮬레이션 20*20*3 = 1200
    -> 1,228,800
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
    grid_copy = [_[:] for _ in game_grid]
    for i in range(n):
        for j in range(n):
            game_grid[i][j] = grid_copy[n - j - 1][i]


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
    global ans
    if idx == 5:
        # 여기서 게임진행
        game_grid = [_[:] for _ in grid]

        for d in sel:
            for ro in range(d):
                rotation(game_grid)

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

'''
# 12100 백준 2048 (Easy)
# 체감난이도 골3 (중력 관련해서 풀어봤으면 골3, 처음이라면 골2)
# 근데 어디선가 풀어봤던 문제인 것 같은데 ㅠㅠㅠ SWEA에 있나??? 처음 풀어본 느낌은 아니였다.
    -> 아 SWEA에 비슷한 문제가 있네요 역시...

# 문제 풀고 나서 기록

    문제 시작 09:00
    문제 종료 09:32
    총 풀이시간 32분
        00~04   : 문제 이해(4)
        04~05   : 초기 주석 및 문제 구상(1)
        05~08   : 1차 설계(3)
                    처음엔 btk 이라고 생각을 안하고
                    for i in range(5):
                        for d in range(4):
                            ...
                    브루트포스 처럼 설계 했는데
                    움직임에 따라 배열 변화가 누적되는 것이기 때문에 이렇게 하면 안됨!!
                    -> 5번 방향의 순서를 구한다음에 시뮬레이션 돌리는거로 변경
        08~11   : 중복순열(?) == 가능한 모든 방향 조합 함수 완료(3)
        11~19   : gravity 함수 완료(8)
                    print로 방향별로 잘 떨어지는 것 확인
        19~24   : merge 함수 완료(5)
                    gravity 에서 약간의 로직만 추가해주면 됨
                    그리고 merge 다음에 gravity 한번 더 추가!
        24~32   : 코드 작성 완료, 테케 답 나오는 거 확인, 검증 시작 (8)
                    - 문제 설명에 있는 예제처럼 방향대로 잘 떨어지고 합쳐지는지 확인
                    - 범위와 i,j 틀린 거 없는지 확인

    메모리 113304 KB
    시간 404 ms

    회고
        1. 스쳤던 생각들
            (ㄱ) 4방향에 따라 하드코딩 하지말고 회전시킨다음 공통적으로 땅겨도 되겠다 했지만
                아 회전을 어떻게 시킬지가 더 머리아파서 그냥 하드코딩으로 당겨줬다.
            (ㄴ) 함수화 가능하겠는데..? 했지만 가로, 세로가 i/j 가 달라서 그것 또한 어려울 것 같아서 않았다.
            -> 역시 (ㄱ), (ㄴ)은 가능했다 교수님 코드 참조하기!!!

        2. 이런 문제는 한 방향의 로직을 완벽하게 짜면
            나머지 방향은 범위와 r,c만 바꾸면 된다.
            근데 중요한 건 스타드 방향을 완벽히 짜야되는 점 ..... 명심..명심..
        3. 검증을 8분정도 했다. 잘했다!! 앞으로도 침착하게 꼼꼼히!!!!

# 문제 풀면서의 기록
문제 설명
    1. 4방향으로 중력
    2. 그리고 방향을 기준으로 합쳐
print(4**5)
헷갈리는 점이 5번움직이고 최댓값 계산인지 ..
근데 당연히 많이 움직일 수록 최댓값이 나오겠져
'''

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]
ans = 0

sel = [0] * 5


def gravity(d, grid):
    if d == 0:  # 북쪽
        for j in range(n):
            while True:
                down = 0
                for i in range(0, n - 1, 1):
                    if grid[i][j] == 0 and grid[i + 1][j] != 0:
                        grid[i][j], grid[i + 1][j] = grid[i + 1][j], grid[i][j]
                        down += 1
                if down == 0:
                    break
    elif d == 1:  # 남쪽
        for j in range(n):
            while True:
                down = 0
                for i in range(n - 1, 0, -1):
                    if grid[i][j] == 0 and grid[i - 1][j] != 0:
                        grid[i][j], grid[i - 1][j] = grid[i - 1][j], grid[i][j]
                        down += 1
                if down == 0:
                    break
    elif d == 2:  # 왼쪽으로 당겨
        for i in range(n):
            while True:
                down = 0
                for j in range(0, n - 1, 1):
                    if grid[i][j] == 0 and grid[i][j + 1] != 0:
                        grid[i][j], grid[i][j + 1] = grid[i][j + 1], grid[i][j]
                        down += 1
                if down == 0:
                    break
    elif d == 3:  # 오른쪽으로 당겨
        for i in range(n):
            while True:
                down = 0
                for j in range(n - 1, 0, -1):
                    if grid[i][j] == 0 and grid[i][j - 1] != 0:
                        grid[i][j], grid[i][j - 1] = grid[i][j - 1], grid[i][j]
                        down += 1
                if down == 0:
                    break


def merge(d, grid):
    if d == 0:
        for j in range(n):
            i = 0
            while i < n - 1:
                if grid[i][j] == grid[i + 1][j]:
                    grid[i][j] = grid[i][j] * 2
                    grid[i + 1][j] = 0
                    i += 1
                i += 1
    elif d == 1:
        for j in range(n):
            i = n - 1
            while i > 0:
                if grid[i][j] == grid[i - 1][j]:
                    grid[i][j] = grid[i][j] * 2
                    grid[i - 1][j] = 0
                    i -= 1
                i -= 1
    elif d == 2:
        for i in range(n):
            j = 0
            while j < n - 1:
                if grid[i][j] == grid[i][j + 1]:
                    grid[i][j] = grid[i][j] * 2
                    grid[i][j + 1] = 0
                    j += 1
                j += 1
    elif d == 3:
        for i in range(n):
            j = n - 1
            while j > 0:
                if grid[i][j] == grid[i][j - 1]:
                    grid[i][j] = grid[i][j] * 2
                    grid[i][j - 1] = 0
                    j -= 1
                j -= 1


def perm(idx):
    global ans, grid
    if idx == 5:
        grid_origin = [_[:] for _ in grid]
        for d in sel:
            gravity(d, grid)
            merge(d, grid)
            gravity(d, grid)

        for i in range(n):
            for j in range(n):
                ans = max(ans, grid[i][j])
        grid = [_[:] for _ in grid_origin]
        return
    for i in range(4):
        sel[idx] = i
        perm(idx + 1)


perm(0)
print(ans)
