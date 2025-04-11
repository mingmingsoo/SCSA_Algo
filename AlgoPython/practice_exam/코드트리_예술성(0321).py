'''
# 04.05.토 2회차 풀이
# 코드트리 예술성

# 문제 풀고 나서 기록

    제출 횟수 1회
    문제 시작 14:41
    문제 종료 15:15
    총 풀이시간 34분
        41~50   : 문제 이해 및 손코딩(9)
        50~54   : 맵 bfs 넘버링(4)
        54~58   : 변 갯수 구하기(4)
                    변 갯수 확인하다가 bfs에서 visited[][] = True 로 한거 발견하고
                    visited[][] = num으로 변경
        58~01   : 점수 계산 -> 구해놓은 dict들로(3)
        01~13   : 회전(12)
        13~15   : 검증(2)

    메모리 19 MB
    시간 107 ms

    회고
        1. 1차 풀이때는 변의 중복을 막고자 3차원 배열을 사용해서 벽을 만들었는데
            중복으로 변 구하고 //2 하면 된다는 사실을 알게돼서 그렇게 진행했다 !!

# 문제 풀면서의 기록
변의 갯수 구하기
'''
from collections import deque, defaultdict

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
score = 0


def bfs(r, c):
    mynum = grid[r][c]
    cnt = 0
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        cnt += 1
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or grid[nr][nc] != mynum:
                continue
            visited[nr][nc] = num
            q.append((nr, nc))

    num_info[num] = (mynum, cnt)


def rotation(grid):  # 반시계
    ro_grid = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            ro_grid[i][j] = grid[j][n - i - 1]
    return ro_grid


def srotation(s, r1, c1):
    ro_s = [[0] * (n // 2) for i in range(n // 2)]
    for i in range(n // 2):
        for j in range(n // 2):
            ro_s[i][j] = s[n // 2 - j - 1][i]

    for i in range(n // 2):
        for j in range(n // 2):
            ro_grid[i + r1][j + c1] = ro_s[i][j]


for t in range(4):
    num_info = {}
    face_dict = defaultdict(int)

    num = 1
    visited = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = num
                bfs(i, j)
                num += 1

    # 변 갯수 구하기
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nr = i + row[k]
                nc = j + col[k]
                if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] == visited[i][j]:
                    continue
                tmp = [visited[i][j], visited[nr][nc]]
                tmp.sort()
                face_dict[tuple(tmp)] += 1

    # 점수 계산
    for k, v in face_dict.items():
        num1, num2 = k
        face = v // 2
        score += (num_info[num1][1] + num_info[num2][1]) * num_info[num1][0] * num_info[num2][0] * face
    if t == 3:
        break

    # 회전
    # 1. 십자가 회전
    ro_grid = rotation(grid)
    # 2. 작은 회전
    s1 = [_[:n // 2] for _ in grid[:n // 2]]
    s2 = [_[n // 2 + 1:] for _ in grid[:n // 2]]
    s3 = [_[:n // 2] for _ in grid[n // 2 + 1:]]
    s4 = [_[n // 2 + 1:] for _ in grid[n // 2 + 1:]]

    srotation(s1, 0, 0)
    srotation(s2, 0, n // 2 + 1)
    srotation(s3, n // 2 + 1, 0)
    srotation(s4, n // 2 + 1, n // 2 + 1)

    grid = ro_grid
print(score)


'''
# 코드트리 예술성
# 체감난이도 골1~골2 (변 갯수가 어려웠음!)

# 문제 풀고 나서 기록

    문제 시작 15:00
    문제 종료 15:52
    총 풀이시간 52분
        00~08   : 문제 이해(8)
        08~16   : 초기 주석 및 문제 구상(8)
                   맞닿은 변 갯수 구하는게 어려울 거라 생각됐음
                   2차원 배열로 visited를 쓰면 2-3 은 막아지지만 2-4 맞닿았을 때 2가 visited 처리 돼서 못가지 말입니다..?
                   그래서 온풍기 안녕에서 벽 만든것 처럼 3차원 벽을 만들어야겠다! 라고 생각함
        16~23   : 맵 넘버링 로직- bfs(7)
        23~34   : 점수 계산을 위해 필요한 변수들을 구하는 로직(11)
                    1. combi를 써서 미리 조합 가능한 애들은 만들었음 -> 얘 때문에 시간이 뚱뚱한듯
                    2. 변의 갯수 세는 로직 - 3차원 visited 써서 구상한대로 진행!
                        ->  변 갯수 말고는 bfs에서 구해서 dict에 넣어줌
        34~36   :  점수 계산 로직(2)
                    위에 구해놓은 변수들로 연산만 해줌
        36~48   : 회전 로직(12)
                    1. 십자가 반시계 회전
                        어차피 나머지 애들은 작은 애들 회전하면서 덮힐 것이기 떄문에
                        2차원 배열 반시계 시켜버림
                    2. 작은애들 회전
                        난 역시 인덱스로 바로 회전시키는 것은 못한다......
                        1,2,3,4 분면 나눠서 회전시키고 반영시킴
                        1사분면만 잘 시켜놓으면 나머지는 쉬워서 후다닥 했음
        48~49   : 오잉 점수가 2회차까지만 더해지는 것임?
                    문제를 잘못읽은건데
                    초기점수 + 1회전 점수 + 2회전 점수 + 3회전 점수! 총 4번의 점수임!! 헤헷 3번인줄
                    그래서 for i in range(4)로 바꿔줌
        49~52   : 이상한 부분 없는지 체크(3)

  메모리 32 KB
  시간 289 ms


회고
    1. 탑다운 설계는 잘 못했다.
        변 갯수 세는게 내 로직대로 잘 되는지 확인한 다음 코드를 짜야겠다고 판단했기 때문!!
        된 다음에는 순차적으로 진행했다.

    2. 시간이 뚱뚱함
        아마  combi써서 그런 것 같은데.. 총 3회전이라 combi 써도 괜찮을 것이라 생각했다.
        친구들 코드 살펴보고 이해하기!

    3. 온풍기 풀면서 썼던 아이디어 활용한 건 잘했다.


# 문제 풀면서의 기록
문제설명
    1. 넘버링
    2. 맞닿은 변 갯수 구하기 (이게 좀 ..)
    3. 회전 (이건 뭐 열심히...)
구상
    맞닿은 변 갯수 구하는게 문제인데
    3턴만 있으니까
    총 그룹핑된 갯수의 2개씩의 조합을 딕셔너리로 구해놓고
    +=1 해주고
    두번 다시 안더해지게 visited 방향을 담아서 좌우/상하 다 트루쳐버린다
'''
from collections import deque


def small_rotate(r1, r2, c1, c2, grid_copy):
    small_grid = [_[c1:c2] for _ in grid_copy[r1:r2]]
    small_ro_grid = [_[:] for _ in small_grid]
    for i in range(sn):
        for j in range(sn):
            small_grid[i][j] = small_ro_grid[sn - j - 1][i]

    for i in range(sn):
        for j in range(sn):
            grid[i + r1][j + c1] = small_grid[i][j]


def rotation():
    grid_copy = [_[:] for _ in grid]  # 얘가 원본
    for i in range(n):
        for j in range(n):
            grid[i][j] = grid_copy[j][n - i - 1]

    # 작은 애들
    small_rotate(0, n // 2, 0, n // 2, grid_copy)
    small_rotate(0, n // 2, n // 2 + 1, n, grid_copy)
    small_rotate(n // 2 + 1, n, 0, n // 2, grid_copy)
    small_rotate(n // 2 + 1, n, n // 2 + 1, n, grid_copy)


def bfs(r, c, same_num, number):
    q = deque([(r, c)])
    cnt = 0
    while q:
        r, c = q.popleft()
        cnt += 1
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or numbering_map[nr][nc] or grid[nr][nc] != same_num:
                continue
            numbering_map[nr][nc] = number
            q.append((nr, nc))
    return cnt


def combi(sidx, idx):
    if sidx == 2:
        if numbering_match[sel[0]] != numbering_match[sel[1]]:
            score_dict[tuple(sel)] = 0
        return
    if idx == number + 1:
        return
    sel[sidx] = idx
    combi(sidx + 1, idx + 1)
    combi(sidx, idx + 1)


n = int(input())
sn = n // 2
grid = [list(map(int, input().split())) for i in range(n)]
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
ans = 0
for i in range(4):
    numbering_map = [[0] * n for i in range(n)]  # 이게 visited 처럼 쓰일 거임
    number = 1

    numbering_match = {}
    numbering_have = {}

    for i in range(n):
        for j in range(n):
            if not numbering_map[i][j]:
                numbering_map[i][j] = number
                cnt = bfs(i, j, grid[i][j], number)
                numbering_match[number] = grid[i][j]
                numbering_have[number] = cnt
                number += 1

    number -= 1

    # 점수 계산할 조합 만들기
    score_dict = {}
    sel = [0] * 2

    combi(0, 1)

    # 변의 갯수 샌다.
    visited = [[[False] * 4 for i in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            my_num = numbering_map[i][j]
            for k in range(4):
                nr = i + row[k]
                nc = j + col[k]
                if not (0 <= nr < n and 0 <= nc < n):
                    continue
                other_num = numbering_map[nr][nc]
                if not visited[i][j][k] and not visited[nr][nc][(k + 2) % 4] and other_num != my_num:
                    tmp = [my_num, other_num]
                    tmp.sort()
                    score_dict[tuple(tmp)] += 1
                    visited[i][j][k] = True
                    visited[nr][nc][(k + 2) % 4] = True

    for key, value in score_dict.items():
        if value:
            team1 = key[0]
            team2 = key[1]
            team1_have = numbering_have[team1]
            team2_have = numbering_have[team2]
            tem1_num = numbering_match[team1]
            tem2_num = numbering_match[team2]
            ans += (team1_have + team2_have) * tem1_num * tem2_num * value
    if i == 3:
        break  # 여까지 왔으면 마지막 회전 안해도 된다.
    rotation()
print(ans)
