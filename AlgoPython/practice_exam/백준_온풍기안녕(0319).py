'''
역시 어렵군
'''
from collections import deque

row = [-1, -1, 0, 1, 1, 1, 0, -1]
col = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, limit = map(int, input().split())
aircon = set()
grid = [list(map(int, input().split())) for i in range(n)]
valid_set = set()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 5:
            valid_set.add((i, j))
            grid[i][j] = 0
        elif 1 <= grid[i][j] <= 4:
            aircon.add((grid[i][j], i, j))
            grid[i][j] = 0

block = [[[False] * 4 for i in range(m)] for i in range(n)]
b = int(input())
for _ in range(b):
    r, c, s = map(int, input().split())
    r -= 1
    c -= 1
    if s == 0:
        block[r][c][0] = True
        block[r - 1][c][2] = True
    if s == 1:
        block[r][c][1] = True
        block[r][c + 1][3] = True

real_fill = [[0] * m for i in range(n)]
edge_set = set()
for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            edge_set.add((i, j))
dir_dict = {2: 6, 3: 0, 1: 2, 4: 4}

side_dict = {2: (0, 4, 6), 3: (6, 2, 0), 1: (0, 4, 2), 4: (6, 2, 4)}
for shape, sr, sc in aircon:
    fill = [[0] * m for i in range(n)]
    fill[sr + row[dir_dict[shape]]][sc + col[dir_dict[shape]]] = 5
    q = deque([(sr + row[dir_dict[shape]], sc + col[dir_dict[shape]], 5)])
    # 5는 무조건 시원해져
    while q:
        r, c, power = q.popleft()
        if power == 1:
            break
        # 바로 밑에
        k = dir_dict[shape]
        nr = r + row[k]
        nc = c + col[k]
        if 0 <= nr < n and 0 <= nc < m and not block[r][c][k // 2]:
            fill[nr][nc] = power - 1
            q.append((nr, nc, power - 1))

        # 옆에
        for k in side_dict[shape][:2]:
            nr1 = r + row[k]
            nc1 = c + col[k]

            nr2 = nr1 + row[side_dict[shape][2]]
            nc2 = nc1 + col[side_dict[shape][2]]
            if not (0 <= nr1 < n and 0 <= nc1 < m) or block[r][c][k // 2]:
                continue
            if not (0 <= nr2 < n and 0 <= nc2 < m) or block[nr1][nc1][side_dict[shape][2] // 2]:
                continue
            fill[nr2][nc2] = power - 1
            q.append((nr2, nc2, power - 1))

    for i in range(n):
        for j in range(m):
            if fill[i][j]:
                real_fill[i][j] += fill[i][j]

ans = 101


def valid():
    for vr, vc in valid_set:
        if grid[vr][vc] < limit:
            return False
    return True


def edge():
    for er, ec in edge_set:
        if grid[er][ec]:
            grid[er][ec] -= 1


def filling():
    for i in range(n):
        for j in range(m):
            if real_fill[i][j]:
                grid[i][j] += real_fill[i][j]


def spread():
    plus_grid = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                continue
            for k in (0, 2, 4, 6):
                nr = i + row[k]
                nc = j + col[k]
                if not (0 <= nr < n and 0 <= nc < m) or block[i][j][k // 2] or grid[nr][nc] >= grid[i][j]:
                    continue
                diff = (grid[i][j] - grid[nr][nc]) // 4
                plus_grid[nr][nc] += diff
                plus_grid[i][j] -= diff

    for i in range(n):
        for j in range(m):
            grid[i][j] += plus_grid[i][j]


for t in range(1, 101):
    filling()
    spread()
    edge()
    if valid():
        ans = t
        break

print(ans)

'''
# 백준 23289 온풍기 안녕!
# 체감난이도 골1 - 문제 풀면서 '골1정도 되는 것 같은데 나 왜이렇게 헤매지?ㅠㅠ' 생각했음...
                    풀고나니까 플5가 맞음.

# 김혜준 지켜야할 거 리스트업

    1. 문제 천천히.꼼꼼히 제발
    2. 2차원 배열 만들 때 for in range(n) 안붙힘
    3. 극간값 생각하기 예를 들어 100초까지면 99초까지봤음
    4. 작성시 한줄한줄 꼼꼼히 와라라락 쓰면 안됨. = 제발 차분히
    5. 보기랑 테케랑 다를 수 있으니 명심 파이어스톰에서 회전됐는데 보기랑 테케 달라서 계속 틀린줄 암
    6. 시뮬레이션에서 테케가 몇개 틀리면, 혹시 동작 순서가 이상한 건 아닌지 확인 (주사위 굴리기나 선물이 넘쳐흘러처럼)
    7. 인구이동 자료구조 만드는 거는 참고해도 될 듯 최적화 관련해서
    8. 프린트 안지우고 제출한거 2트임 진짜 왜구래ㅠ 확인하고 내야지
    9. 내가 관리해야할 대상이 여러개면 하나만 보지말고 대상 모두 전반적으로 print 해서 상태 확인하기(아기 상어 eat 초기화 안함 이슈)
    10. 파핑파핑이나 다리만들기 bfs에서 미리 visited 초기화 해줘야함. r,c  하고 다음에 visited 처리하면 안됨.. nr,nc 에서 꼭 처리해줘야함
            -> 그래야 중복으로 안들어감
    11. 규칙찾기 진짜 못하는듯.. 그래도 찾아라 규칙 못찾으면 몸이 힘들다
    12. 시뮬레이션이라고 너무 동작 순서별로 기능 나누지 말고!!
            일단 나눈 다음에 혹시 동작들을 합쳐도 되는지 확인하기!!!(나무재테크처럼)
    13. 조건문 쓸꺼면 잘 확인하고 쓰기(원판돌리기)
    14. 문제를 잘읽자........윷놀이 사기단을 잊지마...........
    15. 테케 안나오면 오타 없는지도 꼭 확인해주기! (마법사 상어와 복제) r2,c2를 r3,c2로 썼음
    16. 조회연산 많으면 set쓰자 (온풍기 안녕)

# 문제 풀고 나서 기록

    문제 시작 14:00
    문제 종료 16:27
    총 풀이시간 147분
        00~16   : 문제 이해(16) - 화장실 4분
        16~21   : 초기주석 및 문제 구상(5)
        21~30   : 입력 및 탑다운 설계(9)
        30~26   : 온풍기 퍼져나가는 로직 설계(56)
                    일단 오른쪽부터 설계했다가....
                    방향마다 벽 기준이 달라서 하드코딩했다.
                    문제 예제처럼 잘퍼지는지 확인 완료
        26~56   : 조절 로직, 가생이로직, 검증로직 설계(30)
                    이것도 좀 애먹었는데 한번에 처리하려니까 답도 안나오고 어려워서
                    plus_grid, minus_grid 만들어서 했음.
                    가생이 빼는 로직 작성(2)
                    검증 로직도 쉬워서 일단 작성(2)

                    조절 로직 완료되기 전에 가생이. 검증로직 짰는데
                    이유는 조절 로직이 잘되는지 확인하려면 1번테케 출력물하고 비교해야돼서
                    먼저 만들어줬다.

        56~58   : 오픈 테케 답 나오고 2차원 배열 형태도 같음(2)
        58~25   : 1차 제출 - 시간초과, 시간초과나는 이유 분석(27)
                    틀렸습니다도 아니고 시간초과라니...........
                    (1) 혹시 while문을 계속 도는 로직이 있는지... 확인
                        -> 전혀 없음
                    (2) 테케 만들어서 최댓값 넣어봐도 답이 바로 나옴.....
                    (3) 벽 최대갯수가 50*50이라 벽 많을때가 조회가 많아서 문제인가? 해서 set으로 변환
        25~27   : 2차 제출 - 틀렸습니다
                  3차 제출 - 시간초과
                    시간초과 -> 틀렸습니다
                    시간초과는 안났다는건데 리스트랑 set이 그렇게 차이 안날 것 같다고 생각해서
                    다시 첫번째 제출한거 내봤음 (혹시 서버가 느려져서 시간초과 뜬거 아닐까? 하는ㄴ 마음에 ..ㅎㅎ)
                    -> 응 아니고 시간초과가 맞아

                    틀렸다는 건 로직이 잘못된건데... 내가  초기 주석에 100초는 답이 될 수 없고 100초여도 101초 출력하게 짰는데
                    이게 문제인 것 같아서 range 범위를 101까지 늘려줌
                    -> 맞았습니다!


    - 딕셔너리 안쓰고 방향별 if쓰면
      메모리 125832 KB
      시간 732 ms

    - 딕셔너리 쓰면
      메모리 120288 KB
      시간 488 ms


    회고
        1. 시간초과 나서 당황했지만 생각해보면 set이 맞는데.. 그래도 지료구조 바꿀 생각한건 잘했다.
        2. 구상하면서 '99까지 출력될 수 있다고 가정함 -> 더 고민해봐야할듯.' 기록했는데
            답이 100이여도 101로 출력하라는건가? 싶었다.
            기록을 해놓은 덕분에 틀린 이후에 range 수정해서 빨리 맞출 수 있었다.
            앞으로도 헷갈리는 건 잘 기록 해놓자.
        3. 백준 특성 덕분에 [시간초과 -> 틀렸습니다]로 바껴서 뭘 틀렸는지 빠르게 알아낼 수 있었음.
            시험땐 안이러니까 헷갈리는거 기록 잘해놔야함.

# 문제 풀면서의 기록

이야 너무 어려운데...........
문제 설명
    1-1. 집에 있는 모든 온풍기 바람 나옴
    1-2. 그리고 합쳐짐
        이거 두개를 하기 위해선 new_grid만들고 bfs로 퍼진 다음 new_grid에 +=1 해야할듯

    2. 온도 조절 됨
        주변에 나보다 낮은 애들 갯수 카운트해서 나는 그것만큼 빼주고
        나머지들은 더해주고 연쇄적으로 일어나기에 이것도 new_grid 필요
    3. 가생이 빼주기
    4. 초콜렛 먹기
    5. 검사.

구상
    1. 일단 검사해야하는 5는 0으로 바꿔주고 따로 담아줌 valid에서 쓰겠다.
    2. 벽이 어렵다. 일단 저장해놓고 bfs 돌릴 때 검사.
출력
    초콜렛 개수인데 100을 넘어가면? 100도 안된다는거지? 100부터 101이라는거지?????
    99까지 출력될 수 있다고 가정함 -> 더 고민해봐야할듯.
'''
from collections import deque


def valid(grid):
    for r, c in valid_location:
        if grid[r][c] < limit:
            return False
    return True


n, m, limit = map(int, input().split())  # limit 이상
grid = [list(map(int, input().split())) for i in range(n)]
valid_location = set()
robot_list = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 5:
            valid_location.add((i, j))
            grid[i][j] = 0
        elif 0 < grid[i][j] < 5:
            robot_list.append((i, j, grid[i][j] - 1))
            grid[i][j] = 0

block_num = int(input())
block_list = set()
row = [0, 0, -1, 1]
col = [1, -1, 0, 0]
for b in range(block_num):
    r, c, d = map(int, input().split())
    if d == 0:
        block_list.add((r - 1, c - 1, r - 2, c - 1, 2))
        block_list.add((r - 2, c - 1, r - 1, c - 1, 3))
    else:
        block_list.add((r - 1, c - 1, r - 1, c, 0))
        block_list.add((r - 1, c, r - 1, c - 1, 1))
end = False
ans = 101

# for choco in range(1, 100):  # 이러면 커져도 101까지만 나온다.
for choco in range(1, 101):
    # 1-1. 집에 있는 모든 온풍기 바람 나옴
    for r, c, d in robot_list:
        new_grid = [[0] * m for i in range(n)]

        # 일단 퍼져나가
        # 오른쪽 기준으로..

        sr, sc = r + row[d], c + col[d]
        new_grid[sr][sc] = 5  # 5인 곳 표시
        q = deque([(sr, sc, 4)])
        while q:
            r, c, power = q.popleft()
            if power == 0:
                break

            # 5 옆에
            nr = r + row[d]
            nc = c + col[d]
            if (r, c, nr, nc, d) not in block_list and 0 <= nr < n and 0 <= nc < m:
                new_grid[nr][nc] = power
                q.append((nr, nc, power - 1))

            if d == 3:  # 온풍기 방향이 하
                nr1 = r + row[1]  # 왼쪽을 가기위해서 가야하는 왼쪽
                nc1 = c + col[1]

                nr2 = nr + row[1]  # 가려는 왼쪽
                nc2 = nc + col[1]

                if 0 <= nr2 < n and 0 <= nc2 < m and (r, c, nr1, nc1, 1) not in block_list and \
                        (nr1, nc1, nr2, nc2, 3) not in block_list:
                    new_grid[nr2][nc2] = power
                    q.append((nr2, nc2, power - 1))

                nr1 = r + row[0]  # 오른쪽을 가기위해서 가야하는 왼쪽
                nc1 = c + col[0]

                nr2 = nr + row[0]  # 가려는 오른쪽
                nc2 = nc + col[0]
                if 0 <= nr2 < n and 0 <= nc2 < m and (r, c, nr1, nc1, 0) not in block_list and \
                        (nr1, nc1, nr2, nc2, 3) not in block_list:
                    new_grid[nr2][nc2] = power
                    q.append((nr2, nc2, power - 1))

            elif d == 2:  # 온풍기 방향이 상
                nr1 = r + row[1]  # 왼쪽을 가기위해서 가야하는 왼쪽
                nc1 = c + col[1]

                nr2 = nr + row[1]  # 가려는 왼쪽
                nc2 = nc + col[1]

                if 0 <= nr2 < n and 0 <= nc2 < m and (r, c, nr1, nc1, 1) not in block_list and \
                        (nr1, nc1, nr2, nc2, 2) not in block_list:
                    new_grid[nr2][nc2] = power
                    q.append((nr2, nc2, power - 1))

                nr1 = r + row[0]  # 오른쪽을 가기위해서 가야하는 왼쪽
                nc1 = c + col[0]

                nr2 = nr + row[0]  # 가려는 오른쪽
                nc2 = nc + col[0]
                if 0 <= nr2 < n and 0 <= nc2 < m and (r, c, nr1, nc1, 0) not in block_list and \
                        (nr1, nc1, nr2, nc2, 2) not in block_list:
                    new_grid[nr2][nc2] = power
                    q.append((nr2, nc2, power - 1))

            elif d == 0:  # 온풍기 방향이 오른쪽
                nr1 = r + row[2]  # 위쪽을 가기위해서 가야하는 위쪽
                nc1 = c + col[2]

                nr2 = nr + row[2]  # 가려는 위
                nc2 = nc + col[2]

                if 0 <= nr2 < n and 0 <= nc2 < m and (r, c, nr1, nc1, 2) not in block_list and \
                        (nr1, nc1, nr2, nc2, 0) not in block_list:
                    new_grid[nr2][nc2] = power
                    q.append((nr2, nc2, power - 1))

                nr1 = r + row[3]  # 아래쪽을 가기위해서 가야하는 아래쪽
                nc1 = c + col[3]

                nr2 = nr + row[3]  # 가려는 아래
                nc2 = nc + col[3]

                if 0 <= nr2 < n and 0 <= nc2 < m and (r, c, nr1, nc1, 3) not in block_list and \
                        (nr1, nc1, nr2, nc2, 0) not in block_list:
                    new_grid[nr2][nc2] = power
                    q.append((nr2, nc2, power - 1))

            elif d == 1:  # 온풍기 방향이 왼쪽
                nr1 = r + row[2]  # 위쪽을 가기위해서 가야하는 위쪽
                nc1 = c + col[2]

                nr2 = nr + row[2]  # 가려는 위
                nc2 = nc + col[2]

                if 0 <= nr2 < n and 0 <= nc2 < m and (r, c, nr1, nc1, 2) not in block_list and \
                        (nr1, nc1, nr2, nc2, 1) not in block_list:
                    new_grid[nr2][nc2] = power
                    q.append((nr2, nc2, power - 1))

                nr1 = r + row[3]  # 아래쪽을 가기위해서 가야하는 아래쪽
                nc1 = c + col[3]

                nr2 = nr + row[3]  # 가려는 아래
                nc2 = nc + col[3]

                if 0 <= nr2 < n and 0 <= nc2 < m and (r, c, nr1, nc1, 3) not in block_list and \
                        (nr1, nc1, nr2, nc2, 1) not in block_list:
                    new_grid[nr2][nc2] = power
                    q.append((nr2, nc2, power - 1))

        for i in range(n):
            for j in range(m):
                grid[i][j] += new_grid[i][j]

    # 1-2. 그리고 합쳐짐
    #         이거 두개를 하기 위해선 new_grid만들고 bfs로 퍼진 다음 new_grid에 +=1 해야할듯

    #     2. 온도 조절 됨
    #         주변에 나보다 낮은 애들 갯수 카운트해서 나는 그것만큼 빼주고
    #         나머지들은 더해주고 연쇄적으로 일어나기에 이것도 new_grid 필요
    plus_grid = [[0] * m for i in range(n)]
    minus_grid = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                total_minus = 0
                for k in range(4):
                    nr = i + row[k]
                    nc = j + col[k]
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] < grid[i][j] and \
                            (i, j, nr, nc, k) not in block_list:
                        minus = grid[i][j] - grid[nr][nc]
                        plus_grid[nr][nc] += minus // 4
                        total_minus += minus // 4
                minus_grid[i][j] = total_minus

    for i in range(n):
        for j in range(m):
            grid[i][j] += plus_grid[i][j] - minus_grid[i][j]

    #     3. 가생이 빼주기

    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                if grid[i][j] > 0:
                    grid[i][j] -= 1

    #     4. 초콜렛 먹기
    #     5. 검사.
    if valid(grid):
        ans = choco
        break

print(ans)
###########################################################
# 두번쨰 풀이 코드 리팩토링
from collections import deque


def warm():
    for r, c, d in robot_list:
        new_grid = [[0] * m for i in range(n)]

        # 일단 퍼져나가
        sr, sc = r + row[d], c + col[d]
        new_grid[sr][sc] = 5  # 5인 곳 표시
        q = deque([(sr, sc, 4)])
        while q:
            r, c, power = q.popleft()
            if power == 0:
                break

            # 5 옆에
            nr = r + row[d]
            nc = c + col[d]
            if (r, c, nr, nc, d) not in block_list and 0 <= nr < n and 0 <= nc < m:
                new_grid[nr][nc] = power
                q.append((nr, nc, power - 1))

            nr1 = r + row[dir_dict[d][0]]
            nc1 = c + col[dir_dict[d][0]]

            nr2 = nr + row[dir_dict[d][0]]
            nc2 = nc + col[dir_dict[d][0]]

            if 0 <= nr2 < n and 0 <= nc2 < m and (r, c, nr1, nc1, dir_dict[d][0]) not in block_list and \
                    (nr1, nc1, nr2, nc2, dir_dict[d][1]) not in block_list:
                new_grid[nr2][nc2] = power
                q.append((nr2, nc2, power - 1))

            nr1 = r + row[dir_dict[d][2]]
            nc1 = c + col[dir_dict[d][2]]

            nr2 = nr + row[dir_dict[d][2]]
            nc2 = nc + col[dir_dict[d][2]]
            if 0 <= nr2 < n and 0 <= nc2 < m and (r, c, nr1, nc1, dir_dict[d][2]) not in block_list and \
                    (nr1, nc1, nr2, nc2, dir_dict[d][1]) not in block_list:
                new_grid[nr2][nc2] = power
                q.append((nr2, nc2, power - 1))

        for i in range(n):
            for j in range(m):
                grid[i][j] += new_grid[i][j]


def control():
    plus_grid = [[0] * m for i in range(n)]
    minus_grid = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                total_minus = 0
                for k in range(4):
                    nr = i + row[k]
                    nc = j + col[k]
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] < grid[i][j] and \
                            (i, j, nr, nc, k) not in block_list:
                        minus = grid[i][j] - grid[nr][nc]
                        plus_grid[nr][nc] += minus // 4
                        total_minus += minus // 4
                minus_grid[i][j] = total_minus

    for i in range(n):
        for j in range(m):
            grid[i][j] += plus_grid[i][j] - minus_grid[i][j]


def edge():
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                if grid[i][j] > 0:
                    grid[i][j] -= 1


def valid(grid):
    for r, c in valid_location:
        if grid[r][c] < limit:
            return False
    return True


n, m, limit = map(int, input().split())  # limit 이상
grid = [list(map(int, input().split())) for i in range(n)]
valid_location = set()
robot_list = set()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 5:
            valid_location.add((i, j))
            grid[i][j] = 0
        elif 0 < grid[i][j] < 5:
            robot_list.add((i, j, grid[i][j] - 1))
            grid[i][j] = 0

block_num = int(input())
block_list = set()
row = [0, 0, -1, 1]
col = [1, -1, 0, 0]
for b in range(block_num):
    r, c, d = map(int, input().split())
    if d == 0:
        block_list.add((r - 1, c - 1, r - 2, c - 1, 2))
        block_list.add((r - 2, c - 1, r - 1, c - 1, 3))
    else:
        block_list.add((r - 1, c - 1, r - 1, c, 0))
        block_list.add((r - 1, c, r - 1, c - 1, 1))
dir_dict = {0: [2, 0, 3], 1: [2, 1, 3], 2: [1, 2, 0], 3: [1, 3, 0]}
end = False
ans = 101

for choco in range(1, 101):
    warm()
    control()
    edge()
    if valid(grid):
        ans = choco
        break
print(ans)
