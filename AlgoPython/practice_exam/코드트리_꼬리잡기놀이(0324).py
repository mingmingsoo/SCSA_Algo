'''
문제 설명
    - 머리 따라 이동
        dict에 담기
        머리 pop 하고 꼬리 찾고 4 or 3
        그 다음에 다시 insert
        그거 기반 맵 반영
    - 공 굴려 위해서 넘버링 필요
        반전
입력
    맵 n 팀 m 라운드 수 k
1-3 일수가 있나..? 일단 없다고 가정.. -> 교수님한테 여쭤보기

5 1 1
1 2 2 2 2
3 0 0 0 2
2 0 0 0 2
2 0 0 0 2
2 2 2 2 2


'''
from collections import defaultdict, deque

n, tn, turn = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
# 넘버링
num_map = [[0] * n for i in range(n)]
num = 1
team_info = defaultdict(list)
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def bfs(r, c):
    team_info[num].append((r, c))  # 머리 담기
    q = deque([(r, c, 1)])  # 머리
    while q:
        r, c, position = q.popleft()

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or num_map[nr][nc] or not grid[nr][nc]:
                continue
            if position == 1:
                if grid[nr][nc] == 2:  # 2만 찾아!
                    team_info[num].append((nr, nc))
                    q.append((nr, nc, grid[nr][nc]))
                    num_map[nr][nc] = num
            else:
                if 2 <= grid[nr][nc] <= 3:
                    team_info[num].append((nr, nc))
                    q.append((nr, nc, grid[nr][nc]))
                    num_map[nr][nc] = num
                elif grid[nr][nc] == 4:
                    q.append((nr, nc, grid[nr][nc]))
                    num_map[nr][nc] = num


for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not num_map[i][j]:
            num_map[i][j] = num
            bfs(i, j)
            num += 1
score = 0
for t in range(turn):
    # print("-----이동 전-----",t,"초")
    # for _ in grid:
    #     print(_)
    # 1. 머리 따라서 이동
    for k, v in team_info.items():
        hr, hc = v[0]
        tr, tc = v.pop()  # 꼬리 빼
        grid[tr][tc] = 4

        # 머리 찾아
        for k in range(4):
            nr = hr + row[k]
            nc = hc + col[k]
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] in (3, 4):
                v.insert(0, (nr, nc))
                grid[nr][nc] = 1
                break
        # 기반 맵 반영

        for i in range(1, len(v) - 1):
            r, c = v[i]
            grid[r][c] = 2
        grid[v[len(v) - 1][0]][v[len(v) - 1][1]] = 3
    # print("-----이동 후-----",score,t,"초")
    # for _ in grid:
    #     print(_)
    if (t // n) % 4 == 0:
        mod = t % n
        # print(t, (t // n) % 4,  mod)
        find = False
        for j in range(n):
            if 1 <= grid[mod][j] <= 3:  # 공 발견!!
                team_num = num_map[mod][j]
                for idx, location in enumerate(team_info[team_num]):
                    r, c = location
                    if (r, c) == (mod, j):
                        score += (idx + 1) ** 2
                        team_info[team_num].reverse()
                        v = team_info[team_num]
                        grid[v[0][0]][v[0][1]] = 1
                        grid[v[len(v)-1][0]][v[len(v)-1][1]] = 3
                        for tidx in range(1, len(v)-1):
                            grid[v[tidx][0]][v[tidx][1]] = 2


                        find = True
                        break
            if find:
                break
    elif (t // n) % 4 == 1:
        mod = t % n
        # print(t, (t // n) % 4, mod)
        find = False
        for i in range(n - 1, -1, -1):
            if 1 <= grid[i][mod] <= 3:  # 공 발견!!
                team_num = num_map[i][mod]
                for idx, location in enumerate(team_info[team_num]):
                    r, c = location
                    if (r, c) == (i,mod):
                        score += (idx + 1) ** 2
                        team_info[team_num].reverse()
                        v = team_info[team_num]
                        grid[v[0][0]][v[0][1]] = 1
                        grid[v[len(v)-1][0]][v[len(v)-1][1]] = 3
                        for tidx in range(1, len(v)-1):
                            grid[v[tidx][0]][v[tidx][1]] = 2
                        find = True
                        break
            if find:
                break

    elif (t // n) % 4 == 2:
        mod = n - 1 - (t % n)
        # print(t, (t // n) % 4, mod)
        find = False
        for j in range(n - 1, -1, -1):
            if 1 <= grid[mod][j] <= 3:  # 공 발견!!
                team_num = num_map[mod][j]
                for idx, location in enumerate(team_info[team_num]):
                    r, c = location
                    if (r, c) == (mod, j):
                        score += (idx + 1) ** 2
                        team_info[team_num].reverse()
                        v = team_info[team_num]
                        grid[v[0][0]][v[0][1]] = 1
                        grid[v[len(v)-1][0]][v[len(v)-1][1]] = 3
                        for tidx in range(1, len(v)-1):
                            grid[v[tidx][0]][v[tidx][1]] = 2
                        find = True
                        break
            if find:
                break

    elif (t // n) % 4 == 3:
        mod = n - 1 - (t % n)
        # print(t, (t // n) % 4, mod)
        find = False
        for i in range(n):
            if 1 <= grid[i][mod] <= 3:  # 공 발견!!
                team_num = num_map[i][mod]
                for idx, location in enumerate(team_info[team_num]):
                    r, c = location
                    if (r, c) == (i, mod):
                        score += (idx + 1) ** 2
                        team_info[team_num].reverse()
                        v = team_info[team_num]
                        grid[v[0][0]][v[0][1]] = 1
                        grid[v[len(v)-1][0]][v[len(v)-1][1]] = 3
                        for tidx in range(1, len(v)-1):
                            grid[v[tidx][0]][v[tidx][1]] = 2
                        find = True
                        break
            if find:
                break

    # print("-----공 맞고 나서-----",t,"초")
    # for _ in grid:
    #     print(_)
print(score)


'''
# 체감난이도 골1~플5 온풍기 급.. 어려웠음

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
    17. 시험 전에 가운데부터 시작하는 달팽이 풀고가기
    18. new_grid 만들어서 넣어줄 때 이동할때만 넣어주지말고 이동하지 않을때도 넣어주는 거 확인해!!!!!!!!!!!!(술래잡기)
    19. 시험시간은 4시간이다. 체력 부족해서 검증 대충하지말자.................

# 문제 풀고 나서 기록
    제출 횟수 4회
    문제 시작 09:00
    문제 종료 11:10
    총 풀이시간 130분
        00~14   : 문제 이해, 초기 주석 및 문제 구상(14)
        14~43   : bfs 로직(29)
                    각 팀마다 1~4까지의 숫자와 좌표를 모두 담아줌
        43~50   : 이동 로직(17)
                    은 생각보다 쉬웠는데
                    2차원 배열에 좌표 갱신해주고,
                    머리 꼬리 넘버링 다시 해주는게 까다로웠음..
        50~25   : 공 던지는 로직 + 점수계산(35)
                    여기서 ... idx, jdx 계산을 똑바로 했어야했는데 못해서 틀릴 예정
        25~31   : 1차 제출 -> 틀렸습니다(6)
                    3번 예제
                    공 굴리는 위치 로직 수정
                    idx = order % 4가 아님
                    idx = order % n 임
        31~40   : 2차 제출 -> 틀렸습니다.(9)
                    4번 예제
                    아.. 4가 없는 팀도 존재함
                    bfs 로직 수정
        40~10   : 3차 제출 -> 틀렸습니다.(30)
                    틀린 테케가 10번이 넘길래 안봤음
                    문제 로직 뭐 놓쳤는지 분석
                    mok이 2, 3 일때는 아래(혹은 뒤)에서 부턴데 그걸 놓쳤었네!!!?!?!?!?!?
                    idx, jdx 수정!!!!
        10      : 4차 제출


    - 첫 풀이
      메모리 23 MB
      시간 201 ms
    - 최적화
      메모리 22 MB
      시간 150 ms

    회고
        1. 교수님 코드 이해해서 쉽게 풀어보기
        2. 내가 어렵게 푼 이유는..
            q에 4까지 모두 넣으려고 했기 때문인 것 같다
            q에 1~3만 넣어주면 관리하기 용이하다.
        3. 여러모로 아쉬운게 많은 문제
            풀이 시간이 길어지면서 검증을 할 수 있음에도 안하고 낸 내 자신이 밉다.
            앞으론 이러지말자. 시험시간은 4시간이다.

# 문제 풀면서의 기록
어려운뎀..
문제설명
    1. 각 팀이 방향에 따라 한칸씩 이동
    2. 공을 던짐
    3. 공맞은 팀 점수 추가
    4. 공맞은 팀은 방향 전환

입력
    맵 n, 팀 m, 라운드 k
    1 머리
    2 중간
    3 꼬리
    4 이동선

출력
    점수 총합

구상
    1. 회전시키는 게 어려운데....
        q에 어떻게 넣냐가 어려울 듯
'''

#####################################################################
# 코드 최적화
from collections import deque


def bfs(sr, sc, team_numbering):
    q = deque([(sr, sc)])
    tr, tc = -1, -1  # 꼬리 기록
    cnt = 0
    while q:
        r, c = q.popleft()
        cnt += 1
        tmp.append([grid[r][c], (r, c)])
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if 1 <= grid[nr][nc] <= 2 and not visited[nr][nc]:
                visited[nr][nc] = team_numbering
                q.append((nr, nc))
            if grid[nr][nc] == 3:
                tr, tc = nr, nc
    team_info.append(cnt + 1)
    return tr, tc


def bfs4(tr, tc, team_numbering):
    q = deque([(tr, tc)])
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if grid[nr][nc] == 4 and not visited[nr][nc]:
                visited[nr][nc] = team_numbering
                tmp.append([grid[nr][nc], (nr, nc)])
                q.append((nr, nc))


def scoring(i, j):
    global ans, find
    numbering = visited[i][j]
    how = team_info[numbering - 1]
    team = team_lst[numbering - 1]
    for w in range(how):  # 점수 찾기
        state, (r, c) = team[w]
        if (r, c) == (i, j) and 1 <= state <= 3:
            ans += (w + 1) * (w + 1)
            find = True
            break
    tmp = []  # 머리. 꼬리 회전
    for w in range(how - 1, -1, -1):  # 3,2,1 순으로 담기
        tmp.append(team[w])
    for w in range(len(team) - 1, how - 1, -1):  # 4도 거꾸로부터 담기
        tmp.append(team[w])

    tmp[0][0] = 1  # 머리!
    for w in range(1, 1 + how - 2):
        tmp[w][0] = 2  # 몽통!
    tmp[how - 1][0] = 3  # 꼬리!
    team_lst[numbering - 1] = tmp  # 반영


n, team_num, order_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
team_lst = []
visited = [[0] * n for i in range(n)]
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]  # 북 동 남 서
team_info = []  # 팀마다 몇명있는지
team_numbering = 1
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            tmp = []
            visited[i][j] = team_numbering
            tr, tc = bfs(i, j, team_numbering)  # 1,2  담음
            visited[tr][tc] = team_numbering  # 3 담음
            tmp.append([3, (tr, tc)])
            bfs4(tr, tc, team_numbering)  # 4 만 담음
            team_lst.append(tmp)
            team_numbering += 1

ans = 0

for order in range(order_num):

    # 1. 각 팀이 방향에 따라 한칸씩 이동
    for i in range(team_num):
        team = team_lst[i]
        team.insert(0, team.pop())

    # 1-1. 바뀐 위치에 따라 머리, 몸통, 꼬리 반영
    for i in range(team_num):
        how = team_info[i]
        team_lst[i][0][0] = 1
        for j in range(1, 1 + how - 2):
            team_lst[i][j][0] = 2
        team_lst[i][how - 1][0] = 3
        for j in range(how, len(team_lst[i])):
            team_lst[i][j][0] = 4

    # 1-2. 토대로 맵도 변경
    new_grid = [[0] * n for _ in range(n)]
    for team in team_lst:
        for state, (r, c) in team:
            new_grid[r][c] = state

    # 2. 공을 던짐
    # 3. 공맞은 팀 점수 추가
    mok = order // n
    find = False
    if mok % 4 == 0:  # 가로로 탐색 0 부터
        idx = order % n
        for j in range(n):
            if 1 <= new_grid[idx][j] <= 3:
                # 맞았다!
                scoring(idx, j)
            if find:
                break
    elif mok % 4 == 2:  # 가로로 탐색 뒤 부터
        idx = n - order % n - 1
        for j in range(n - 1, -1, -1):
            if 1 <= new_grid[idx][j] <= 3:
                # 맞았다!
                scoring(idx, j)
            if find:
                break
    elif mok % 4 == 3:  # 세로로 탐색 0 부터
        jdx = n - order % n - 1
        for i in range(n):
            if 1 <= new_grid[i][jdx] <= 3:
                # 맞았다!
                scoring(i, jdx)
            if find:
                break

    elif mok % 4 == 1:  # 세로로 탐색 n 부터
        jdx = order % n
        for i in range(n - 1, -1, -1):
            if 1 <= new_grid[i][jdx] <= 3:
                scoring(i, jdx)
            if find:
                break

    # 맞아서 위치 바뀌거 다시 반영!
    if find:
        new_grid = [[0] * n for _ in range(n)]
        for team in team_lst:
            for state, (r, c) in team:
                new_grid[r][c] = state

        grid = new_grid

print(ans)
############################################################
#  첫 풀이
from collections import deque

n, team_num, order_num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

team_lst = []
visited = [[0] * n for i in range(n)]
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]  # 북 동 남 서
team_info = []  # 팀마다 몇명있는지
ans = 0


def bfs(sr, sc, team_numbering):
    q = deque([(sr, sc)])
    tr, tc = -1, -1
    cnt = 0
    while q:
        r, c = q.popleft()
        cnt += 1
        tmp.append([grid[r][c], (r, c)])
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if 1 <= grid[nr][nc] <= 2 and not visited[nr][nc]:
                visited[nr][nc] = team_numbering
                q.append((nr, nc))
            if grid[nr][nc] == 3:
                tr, tc = nr, nc
    team_info.append(cnt + 1)
    return tr, tc


def bfs4(tr, tc, team_numbering):
    q = deque([(tr, tc)])
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if grid[nr][nc] == 4 and not visited[nr][nc]:
                visited[nr][nc] = team_numbering
                tmp.append([grid[nr][nc], (nr, nc)])
                q.append((nr, nc))


team_numbering = 1

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            tmp = []
            visited[i][j] = team_numbering
            tr, tc = bfs(i, j, team_numbering)  # 1,2만 담음
            visited[tr][tc] = team_numbering
            tmp.append([3, (tr, tc)])
            bfs4(tr, tc, team_numbering)  # 4 만 담음
            team_lst.append(tmp)
            team_numbering += 1

# for team in team_lst:
#     print(team)
team_numbering -= 1

for order in range(order_num):
    # pass
    # 1. 각 팀이 방향에 따라 한칸씩 이동
    # print("-----이동전-----")
    # for _ in grid:
    #     print(*_)
    for i in range(team_num):
        team = team_lst[i]
        team.insert(0, team.pop())

    for i in range(team_num):
        how = team_info[i]
        team_lst[i][0][0] = 1
        for j in range(1, 1 + how - 2):
            team_lst[i][j][0] = 2
        team_lst[i][how - 1][0] = 3
        for j in range(how, len(team_lst[i])):
            team_lst[i][j][0] = 4

    # print("------------")
    # for _ in team_lst:
    #     print(_)

    new_grid = [[0] * n for _ in range(n)]
    for team in team_lst:
        for state, (r, c) in team:
            new_grid[r][c] = state
    # print("-------이동후 ")
    # for _ in new_grid:
    #     print(*_)

    # 2. 공을 던짐
    # 3. 공맞은 팀 점수 추가
    mok = order // n
    if mok % 4 == 0:  # 가로로 탐색 0 부터
        idx = order % n
        # print("가로로 탐색 0부터 ", idx)
        for j in range(n):
            find = False
            if 1 <= new_grid[idx][j] <= 3:
                # 맞았다!
                numbering = visited[idx][j]
                how = team_info[numbering - 1]
                team = team_lst[numbering - 1]
                for i in range(how):
                    state, (r, c) = team[i]
                    if (r, c) == (idx, j) and 1 <= state <= 3:
                        ans += (i + 1) * (i + 1)
                        find = True
                        break
                tmp = []
                for i in range(how - 1, -1, -1):
                    tmp.append(team[i])
                for i in range(len(team) - 1, how - 1, -1):
                    tmp.append(team[i])

                tmp[0][0] = 1
                for j in range(1, 1 + how - 2):
                    tmp[j][0] = 2
                tmp[how - 1][0] = 3
                for j in range(how, len(tmp)):
                    tmp[j][0] = 4  # 이건 안해도 되겠지만 일단 두겟음

                team_lst[numbering - 1] = tmp
            if find:
                break
    if mok % 4 == 2:  # 가로로 탐색 뒤 부터
        idx = n - order % n - 1
        # print("가로로 탐색 n부터", idx)
        for j in range(n - 1, -1, -1):
            find = False
            if 1 <= new_grid[idx][j] <= 3:
                # 맞았다!
                numbering = visited[idx][j]
                how = team_info[numbering - 1]
                team = team_lst[numbering - 1]
                for i in range(how):
                    state, (r, c) = team[i]
                    if (r, c) == (idx, j) and 1 <= state <= 3:
                        ans += (i + 1) * (i + 1)
                        find = True
                        break
                tmp = []
                for i in range(how - 1, -1, -1):
                    tmp.append(team[i])
                for i in range(len(team) - 1, how - 1, -1):
                    tmp.append(team[i])

                tmp[0][0] = 1
                for j in range(1, 1 + how - 2):
                    tmp[j][0] = 2
                tmp[how - 1][0] = 3
                for j in range(how, len(tmp)):
                    tmp[j][0] = 4  # 이건 안해도 되겠지만 일단 두겟음

                team_lst[numbering - 1] = tmp
            if find:
                break

    if mok % 4 == 3:  # 세로로 탐색 0 부터
        jdx = n - order % n - 1
        # print("세로로 탐색 0부터", jdx)
        for i in range(n):
            find = False
            if 1 <= new_grid[i][jdx] <= 3:
                # 맞았다!
                numbering = visited[i][jdx]
                how = team_info[numbering - 1]
                team = team_lst[numbering - 1]
                for w in range(how):
                    state, (r, c) = team[w]
                    if (r, c) == (i, jdx) and 1 <= state <= 3:
                        ans += (w + 1) * (w + 1)
                        find = True
                        break
                tmp = []
                for w in range(how - 1, -1, -1):
                    tmp.append(team[w])
                for w in range(len(team) - 1, how - 1, -1):
                    tmp.append(team[w])

                tmp[0][0] = 1
                for w in range(1, 1 + how - 2):
                    tmp[w][0] = 2
                tmp[how - 1][0] = 3
                for w in range(how, len(tmp)):
                    tmp[w][0] = 4  # 이건 안해도 되겠지만 일단 두겟음

                team_lst[numbering - 1] = tmp
            if find:
                break

    if mok % 4 == 1:  # 세로로 탐색 n 부터
        jdx = order % n
        # print("세로로 탐색 n부터", jdx)
        for i in range(n - 1, -1, -1):
            find = False
            if 1 <= new_grid[i][jdx] <= 3:
                # 맞았다!
                numbering = visited[i][jdx]
                how = team_info[numbering - 1]
                team = team_lst[numbering - 1]
                for w in range(how):
                    state, (r, c) = team[w]
                    if (r, c) == (i, jdx) and 1 <= state <= 3:
                        ans += (w + 1) * (w + 1)
                        find = True
                        break
                tmp = []
                for w in range(how - 1, -1, -1):
                    tmp.append(team[w])
                for w in range(len(team) - 1, how - 1, -1):
                    tmp.append(team[w])

                tmp[0][0] = 1
                for w in range(1, 1 + how - 2):
                    tmp[w][0] = 2
                tmp[how - 1][0] = 3
                for w in range(how, len(tmp)):
                    tmp[w][0] = 4  # 이건 안해도 되겠지만 일단 두겟음

                team_lst[numbering - 1] = tmp
            if find:
                break

    new_grid = [[0] * n for _ in range(n)]
    for team in team_lst:
        for state, (r, c) in team:
            new_grid[r][c] = state
    # for _ in new_grid:
    #     print(*_)
    # print(ans)
    grid = new_grid
# 4. 공맞은 팀은 방향 전환
print(ans)
