'''
# 코드트리 팩맨
2025.04.04.금
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 11:51
    문제 종료 12:34

    총 풀이시간 43분
        51~00 : 문제 이해 및 초기주석(9)
        00~02 : 방향 만들기(2)
        02~25 : 로직 작성(23)
        25~34 : 검증(9)
                한마리도 못먹을 때는 상상상으로 가는거 아닌가? 해서
                조건문으로 이동위치 따져줬던 걸 lst 담아서 sort 하는 걸로 변경



  메모리 16 MB
  시간 50 ms


최악컨디션에서 함 해부자~
문제 설명
    1. 몬스터 복제
    2. 몬스터 이동 new_grid 필요
        시체 검사 필요
    3. 팩맨 이동
        maxi = 0, nr = r ,nc = c , eating = set()
        for d1,d2,d3 in dir_lst:
            visited = set()
            if nr = ..
            if len(visited) > maxi:
                ...
        r = nr , c = nc , eating
    4. 시체 남기기 die_grid 필요
    4. die_grid 1씩 빼주기 양수인 애들만
    5. 위에 원본 extend

입력
    몬스터 마리 수 m, 진행 턴 수 t
    팩맨 위치 r,c
    몬스터 정보
주의
    팩맨 방향 우선순위 상좌하우
    set 순서 유지 되지?
    근데 팩맨이 먹을 수 있는게 하나도 없으면 이동해????????????????????????
    ㅇㅇ 그럴 듯
1 1
3 1
1 1 5
'''
#################################################################### 방향 만들기
dir_lst = set()
sel = [0] * 3


def make_dir(idx):
    if idx == 3:
        dir_lst.add(tuple(sel))
        return
    for i in range(4):
        sel[idx] = i
        make_dir(idx + 1)

make_dir(0)

#################################################################### 입력
n = 4
m, time = map(int, input().split())
grid = [[[] for i in range(n)] for i in range(n)]
die_grid = [[0] * n for i in range(n)]
for _ in range(m):
    r, c, d = map(lambda x: int(x) - 1, input().split())
    grid[r][c].append(d)
pr, pc = map(lambda x: int(x) - 1, input().split())

m_row = [0, -1, -1, -1, 0, 1, 1, 1]
m_col = [-1, -1, 0, 1, 1, 1, 0, -1]
p_row = [-1, 0, 1, 0]
p_col = [0, -1, 0, 1]

#################################################################### 메인
for t in range(time):
    # 2. 몬스터 이동 new_grid 필요, 시체 검사 필요
    new_grid = [[[] for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                for d in grid[i][j]:
                    move = False
                    for k in range(8):
                        nr = i + m_row[d]
                        nc = j + m_col[d]
                        if not (0 <= nr < n and 0 <= nc < n) or (nr, nc) == (pr, pc) or die_grid[nr][nc]:
                            d = (d - 1) % 8
                        else:
                            move = True
                            break
                    if move:
                        nr = i + m_row[d]
                        nc = j + m_col[d]
                        new_grid[nr][nc].append(d)
                    else:
                        new_grid[i][j].append(d)
    # 3. 팩맨 이동
    location_lst = []
    for dirs in dir_lst:
        r, c = pr, pc
        eat = 0
        possible = True
        visited = set()
        for d in dirs:
            nr = r + p_row[d]
            nc = c + p_col[d]
            if not (0 <= nr < n and 0 <= nc < n):
                possible = False
                break
            if new_grid[nr][nc] and (nr, nc) not in visited:
                visited.add((nr, nc))
                eat += len(new_grid[nr][nc])
            r = nr
            c = nc
        if possible:
            location_lst.append((-eat, dirs, visited, r, c))
    location_lst.sort()
    eat_num, dirs, eating, npr, npc = location_lst[0]
    pr, pc = npr, npc  # 팩맨 이동
    for r, c in eating:
        new_grid[r][c] = []  # 먹혔다.
        die_grid[r][c] = 3  # 죽었다

    # 4. die_grid 1씩 빼주기 양수인 애들만
    for i in range(n):
        for j in range(n):
            if die_grid[i][j]:
                die_grid[i][j] -= 1

    # 5. 위에 원본 extend
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                new_grid[i][j].extend(grid[i][j])
    grid = new_grid

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            ans += len(grid[i][j])
print(ans)

'''
# 백준 23290 마법사 상어와 복제
# 체감난이도 골1 - 신경써야할 부분이 너~~~~~~~~~~~무 많음

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

# 문제 풀고 나서 기록

    문제 시작 09:00
    문제 종료 10:34
    총 풀이시간 94분
        00~07   : 문제 이해(7)
        07~10   : 초기 주석 및 문제 구상(3)
        10~13   : 초기 주석대로 탑다운 설계(3)
        13~22   : 물고기 이동 로직 설계(9)
        22~25   : 상어 방향 담는 duple_perm 함수 설계(3)
        25~29   : 상어 이동 out_of_range 함수 설계(4)
        29~33   : 우선순위에 따른 상어 이동 로직 설계(4)
        33~39   : 1차 디버깅(6)(처음 상어는 0,0,0 인데 3,0,2의 방향을 가져서 디버깅)

                    1. 먹은 물고기 갯수 계산할 때 이동 후 물고기로 계산 될 수 있도록
                        len(grid[r][c]) -> len(new_grid[r][c]) 로 수정

                    2. 한번 먹은 물고기는 다시 먹을 수 없는데 그 조건을 생각 못해서
                        visited 추가해줌

        39~44   : 냄새 로직 설계(5) (죽은 애들 smell_grid 에 2표시, 그리고 -1 씩 감소)
        44~45   : 물고기 복제 로직 설계(1)
        45~58   : 2차 디버깅(13)(몇몇 테케가 답 안나오는 거 확인(당연하지 고칠게 많단다^^))

                    1. origin_grid 라고 3차원 배열 복사해놓은거 필요가 없어서 지워줌(1)
                        왜냐하면 new_grid를 사용하기에 원본 배열을 사용하지 않기 때문임

                    2. 냄새 풍기는거 죽은 애들 2로 표시해줬는데(13)
                        -1 해주는 과정에서 (2 -> 1) 로 변하기 때문에 3으로 바꿔줌

        58~04   : 3차 디버깅(6)(그래도 답이 안나와요)

                    물고기 이동할 때 이동하지 못하면 원래 그 위치, 그 방향 그대로 넣어줘야하는데
                    이동시에만 넣어줬어서 움직이지 못했으면 원래 그 위치 추가! 해줌 -> 이런건 기본 아니냐...
                    if not move: new_grid[i][j].append(fish)

        04~33   : 4차 디버깅(29)(그래도 답이 안나옴)

                    -> 숫자 큰 테케는 디버깅이 힘들고 6번 테케로 디버깅
                    별의 별 print를 다 찍어봄 그렇지만 너의 로직이 맞음
                    근데 대박 상어가 (우,우,우) 로 갈때 가운데 우는 안잡아 먹는 것 아니겠어요?

                    heapq.heappush(possible, (-eat, s_dir, (r1, c1, r3, c2, r3, c3)))
                    -> heapq.heappush(possible, (-eat, s_dir, (r1, c1, r2, c2, r3, c3))) 로 수정...

    메모리 160068 KB
    시간 272 ms

    회고
        1. 으아아 오타 오타 오타!!!!!!!!
            오타로 디버깅 처음 해보는데.. 테케 답이 안나올 땐 오타 없는지 확인하는 습관도 가지기!!!!!!!
        2. 테케가 굉~~장히 친절해서 오타도 찾았고 원큐에 성공한 문제다..................
            테케 의존 줄여야하는데~ 코드를 잘짜자....................please.......
        3. 로직 덩어리로 숭덩숭덩 짜지말고 로직 하나하나 꼼꼼히 짠 다음에 다음 로직으로 넘어가자!!!!!!
        2. 헷갈렸던 점: 상어가 못먹어도 go 인가? yes!!  못먹으면 (상,상,상)으로 간다(범위 안벗어나면)

# 문제 풀면서의 기록
문제 설명
    1. 초기 물고기 상태 남겨놓음
    2. 물고기 이동
    3. 상어 이동
    4. 2턴 전 물고기 냄새 사라짐
    5. 물고기 복제

구상
    1. origin 배열을 만든다
    2.
    3. 먼저 상어가 이동 가능한 방향들을 list에 담는다.
        그 모든 조합 중 가능한 조합 + 담겨있는 물고기 갯수(얘가 더 우선순위)를 담고
        젤 앞에있는 애를 고른다.
        그리고 죽은 애들은 냄새 표시
    4. 냄새 관리

입력
    물고기 수, 턴 수
    물고기 정보
출력
    남아있는 물고기 수
'''


def duple_perm(idx):
    if idx == 3:
        shark_dir_list.append(tuple(sel))
        return

    for i in range(4):
        sel[idx] = i
        duple_perm(idx + 1)


def out_of_range(sr, sc, s_dir):
    r, c = sr, sc
    for d in s_dir:
        r = r + s_row[d]
        c = c + s_col[d]
        if not (0 <= r < n and 0 <= c < n):
            return True
    return False


n = 4
fish_num, turn_num = map(int, input().split())
grid = [[[] for i in range(n)] for i in range(n)]
for f in range(fish_num):
    r, c, d = map(lambda x: int(x) - 1, input().split())
    grid[r][c].append(d)
sr, sc = map(lambda x: int(x) - 1, input().split())  # 상어 위치
smell_grid = [[0] * n for i in range(n)]  # 어차피 물고기는 냄새있는 곳으로 못가서 냄새가 겹칠 일은 없다. 그래서 2차원 배열
row = [0, -1, -1, -1, 0, 1, 1, 1]
col = [-1, -1, 0, 1, 1, 1, 0, -1]
s_row = [-1, 0, 1, 0]
s_col = [0, -1, 0, 1]

shark_dir_list = []
sel = [0] * 3
duple_perm(0)

for turn in range(turn_num):
    # 1. 초기 물고기 상태 남겨놓음
    # 2. 물고기 이동
    new_grid = [[[] for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                for fish in grid[i][j]:
                    d = fish
                    move = False
                    for k in range(8):
                        nr = i + row[d]
                        nc = j + col[d]
                        if (nr, nc) == (sr, sc) or not (0 <= nr < n and 0 <= nc < n) or smell_grid[nr][nc]:
                            d = (d - 1 + 8) % 8
                        else:
                            new_grid[nr][nc].append(d)
                            move = True
                            break
                    if not move:
                        new_grid[i][j].append(fish)

    possible = []
    for s_dir in shark_dir_list:
        eat_set = set()
        if out_of_range(sr, sc, s_dir):  # 범위 벗어나면 아웃
            continue
        d1, d2, d3 = s_dir
        r1, c1 = sr + s_row[d1], sc + s_col[d1]
        r2, c2 = r1 + s_row[d2], c1 + s_col[d2]
        r3, c3 = r2 + s_row[d3], c2 + s_col[d3]
        eat = len(new_grid[r1][c1])
        eat_set.add((r1, c1))
        if (r2, c2) not in eat_set:
            eat += len(new_grid[r2][c2])
            eat_set.add((r2, c2))
        if (r3, c3) not in eat_set:
            eat += len(new_grid[r3][c3])
        possible.append((-eat, s_dir, [(r1, c1), (r2, c2), (r3, c3)]))
    possible.sort()
    eat, dirs, location = possible[0]

    sr, sc = location[2][0], location[2][1]  # 상어 옮겨
    for r, c in location:
        if new_grid[r][c]:
            smell_grid[r][c] = 3
            new_grid[r][c] = []

    # 4. 2턴 전 물고기 냄새 사라짐
    for i in range(n):
        for j in range(n):
            if smell_grid[i][j] > 0:
                smell_grid[i][j] -= 1

    #     5. 물고기 복제
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                new_grid[i][j].extend(grid[i][j])

    grid = new_grid

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(grid[i][j])
print(ans)
