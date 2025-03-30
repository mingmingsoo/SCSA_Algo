'''
시간복잡도
몬스터 수 n**2(시간)
bfs n**2
n**4 = 160000
'''

from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            r, c, eat, level = i, j, 0, 2
            grid[r][c] = 0

time = 0
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def bfs(r, c):
    visited = [[False] * n for i in range(n)]
    visited[r][c] = True
    q = deque([(r, c, 0)])
    while q:
        for qs in range(len(q)):
            r, c, dist = q.popleft()
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or grid[nr][nc] > level:
                    continue
                if 0< grid[nr][nc] < level:
                    monsters.append((dist + 1, nr, nc))
                visited[nr][nc] = True
                q.append((nr, nc, dist + 1))
        if monsters:
            return


while True:

    monsters = []
    bfs(r, c)
    if not monsters:
        break
    monsters.sort()
    dist, mr, mc = monsters[0]
    time+=dist
    grid[mr][mc] = 0
    r, c = mr, mc
    eat += 1
    if eat == level:
        level += 1
        eat = 0

print(time)


'''
# 문제 풀고 나서 기록

# 김혜준 지켜야할 거 리스트업

    1. 문제 천천히.꼼꼼히 제발
    2. 2차원 배열 만들 때 for in range(n) 안붙힘
    3. 극간값 생각하기 예를 들어 100초까지면 99초까지봤음
    4. 작성시 한줄한줄 꼼꼼히 와라라락 쓰면 안됨. = 제발 차분히
    5. 보기랑 테케랑 다를 수 있으니 명심(파이어스톰에서 회전됐는데 보기랑 테케 달라서 계속 틀린줄 암)
    6. 시뮬레이션에서 테케가 몇개만 틀리면, 혹시 동작 순서가 이상한 건 아닌지 확인 (주사위 굴리기나 선물이 넘쳐흘러처럼)
    7. 자료구조를 여러번 만들면 인구이동 상기하기
    8. 프린트 안지우고 제출한거 2트임 진짜 왜구래ㅠ 확인하고 내야지
    9. 내가 관리해야할 대상이 여러개면 하나만 보지말고 대상 모두 전반적으로 print 해서 상태 확인하기

    ❌제출횟수 3회❌
    1회 틀린이유: eat 초기화를 안해줌
    2회 틀린이유: eat 초기화 안해준거 발견해서
                신나서 print 안지우고 제출 환멸남
                머가 그렇게 신났니😡

    문제 시작 09:05
    문제 종료 09:33
    총 풀이시간 28분
        05~08   : 문제 이해(3)
        08~10   : 문제 구상 및 초기 주석(2)
        10~20   : 1차 설계 완료(10)
                    레벨 높은애들은  피해서 가야되는게 망각하고 맨해튼 거리로 짰음
                    당근 이렇게 짜면 1번 테케 답이 안나옴
        20~23   : 2차 설계 완료(3)
                    후보 정하는 로직 bfs로 수정
        23~25   : 로직 이상한 부분 없는지 확인(2)
        26      : 틀렸습니다!
        26~32   : 디버깅(6)
                1. 문제에서 놓친거 없는지 확인
                2. 내 테케 넣어보기
                3. target의 정보 출력해봄
                    -> 당연히 맞게 나옴
                    -> 너는  eat 초기화를 안해서 그런거니까.
                    -> 전투로봇이 잘못됐을 것이라는 생각을 못했음
                    -> 전투로봇 찍어볼걸
                4. 코드 한줄한줄 뜯어봄
                5. eat 초기화 안한거 발견
        32      : 프린트 안지우고 제출 -> 틀!
        33      : 진짜제출

    메모리 114924 KB
    시간 164 ms

    회고
    1. 아 eat 초기화 안한거 발견할 때까진 흐름 좋았는데
        print 안지우고 제출한거 정말 밍망하고 챙피합니다.

    2. 코드 짜면서 로직 잘 돌아가는지 잘 확인하는 편이라 생각했는데
        target만 확인하고 전투로봇 확인 안한건 좀 아쉽네요...
        다음엔 비슷한 문제가 있으면 생각 날 것 같아서
        관리해야할 대상이 여러개면 대상 모두 확인하도록!! 하겠습니다!!!!!!!!
        
    3. 클래스? 생각 했지만 heapq에 몬스터 넣어야하는데 우선순위 어떻게 설정해야할 지 잘 모르겠어서 패스했음
        지금 기억을 더듬어보니까 gt, lt 이런거 있었던 것 같은데 다시 짜보기



# 문제 풀면서의 기록
문제설명
    초기 전투로봇 레벨2
    1초에 상하좌우 한칸식 이동
    자기보다 레벨 높은애들은 지나갈 수 없음
    자기보다 레벨 낮은애들 없앨 수 있음
    자기랑 레벨 같으면 지나갈 수 는 있음
    가는 우선순위
    1. 거리가 가장 가까운
    2. 가장 위쪽, 왼쪽
    없으면 끝
    전투로봇은 본인 레벨만큼 먹으면 레벨 상승함

입력
    9: 전투로봇
    1~6 : 몬스터
구상
    bfs도는데 힙큐 사용.

'''
import heapq
from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]

r, c, level, eat = -1, -1, 2, 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            grid[i][j] = 0
            r, c = i, j

time = 0
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
while True:
    # 자기보다 레벨 높은애들은 지나갈 수 없음
    # 자기보다 레벨 낮은애들 없앨 수 있음
    # 자기랑 레벨 같으면 지나갈 수 는 있음
    target_q = []

    # 아 거리 계산하는게 쉽지 않네...

    q = deque([(r, c, 0)])
    visited = [[False] * n for i in range(n)]
    visited[r][c] = True
    while q:
        r, c, dist = q.popleft()

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc]:
                continue
            if grid[nr][nc] == 0 or grid[nr][nc] == level:
                visited[nr][nc] = True
                q.append((nr, nc, dist + 1))
            elif grid[nr][nc] < level:
                visited[nr][nc] = True
                heapq.heappush(target_q, (dist + 1, nr, nc))
    if not target_q:
        break
    # print(target_q)
    dist, target_r, target_c = heapq.heappop(target_q)
    # print((target_r,target_c),dist)
    grid[target_r][target_c] = 0  # 먹는다
    eat += 1
    r = target_r
    c = target_c
    time += dist
    if eat == level:
        level += 1
        eat = 0  # eat 초기화를 안해줘서 1회 틀림

print(time)
