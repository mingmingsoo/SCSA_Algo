'''아마 16:42 부터?
문제 설명
    1. 0은 어디에나 가능 -> bfs안에서 visited
    2. 색깔 있는 곳(빨 제외)에서만 bfs -> 총 2 개 이상
    3. 우선순위 주의
입력
    맵 크기 n, 색깔 몇개인지 m
    맵 정보
출력
    터지는 크기**2 합
'''
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
score = 0


def myprint():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 6:
                print(" ", end=" ")
            elif grid[i][j] == -1:
                print("B", end=" ")
            else:
                print(grid[i][j], end=" ")
        print()


def rotation():
    grid_origin = [_[:] for _ in grid]
    for i in range(n):
        for j in range(n):
            grid[i][j] = grid_origin[j][n - i - 1]


def gravity():
    for j in range(n):
        while True:
            down = False
            for i in range(n - 1, 0, -1):
                if grid[i][j] == 6 and 0 <= grid[i - 1][j] <= 5:
                    down = True
                    grid[i][j], grid[i - 1][j] = grid[i - 1][j], grid[i][j]
            if not down:
                break


def bfs(r, c):
    cnt = 0
    red = 0
    location = []
    visited[r][c] = True
    q = deque([(r, c)])
    red_visited = set()
    color = grid[r][c]
    while q:
        r, c = q.popleft()
        cnt += 1
        if grid[r][c] == 0: red += 1
        location.append((r, c))

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if not visited[nr][nc] and grid[nr][nc] == color:
                q.append((nr, nc))
                visited[nr][nc] = True
            if (nr, nc) not in red_visited and grid[nr][nc] == 0:
                q.append((nr, nc))
                red_visited.add((nr, nc))

    if cnt > 1:
        return cnt, red, location
    else:
        return -1, -1, -1


while True:

    bomb_lst = []
    visited = [[False] * n for i in range(n)]

    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]

    for i in range(n):
        for j in range(n):
            if 0 < grid[i][j] < 6 and not visited[i][j]:  # 검, 빨 제외
                total, red, location = bfs(i, j)
                if total != -1:
                    bomb_lst.append((-total, -red, -i, -j, location))

    if bomb_lst:
        bomb_lst.sort()
        cnt, lo = bomb_lst[0][0], bomb_lst[0][4]
        score += cnt ** 2
        # 6 이 빈공간
        for br, bc in lo:
            grid[br][bc] = 6
    else:
        break

    gravity()
    rotation()
    gravity()

print(score)


'''
# 21609 백준 상어중학교
# 체감난이도 골1(만약 0 방문처리 했을 때 답 틀리게 나오는 테케있었으면 골3~골4)

# 문제 풀고 나서 기록

    문제 시작 15:00
    1차 제출  15:56
    문제 종료 16:51
    총 풀이시간 111분
        00~03   : 문제 이해(3)
        03~11   : 초기 주석 및 문제 구상(8)
        11~20   : 탑다운 설계(9)
                  bfs, fall, gravity
        20~38   : bfs 설계 완료(18)
                  처음에는 우선순위를 if 로 비교하려고 했으나
                  우선순위 조건이 많기 때문에 배열에 담아서 sort 하는 걸로 수정
                  이때까지는 기준좌표 우선순위가 작은 순인줄 알고(큰 순임)
                  크기랑 무지개수에는 - 붙혔고 r,c는 그대로 넣고 sort 했음
        38~40   : delete 설계(2)
                  처음엔 F로 바꿨는데 그러면 if 연산에서 숫자 비교도 안되고 골치아파서 m이 5까지길래 9로 바꿈
        40~45   : fall 설계(5)
        45~51   : rotation 설계(6)
                  회전이 잘안돼서 보니까 n을 m으로 쳤음 수정 완료 휴~
        51~54   : 제출 전에 문제 조건 놓친거 없는지 확인(3)
                  허걱 그룹 선택하는 기준이 기준좌표가 큰 순임!!!
                   sort reverse로 수정 -> 이거 잘했다!! 칭찬해
        56      : 1차 제출 틀렸습니다
        56~33   : 무한 디버깅 시작...(36)
                  근데 진짜 틀린 부분이 없었음 너무나 완벽했음 ㅠㅠㅠㅠㅠㅠ
        33~51   : 내가 뭘 놓쳤는지 문제도 계속 읽고... 상기하고 테케 넣어보고...... 고민함(18)
                  초기 주석 보면 안하기로 설계했었는데!!!!!!! 대박 0인 애들 visited 처리하고 있었네? bfs 로직 수정 완료
                  이래서 습관이 무섭다니까..........ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ

    메모리 116136 KB
    시간 212 ms

    회고
        1. 내 로직이 완벽하면 뭔가를 놓쳤다는 것. 뭘 놓쳤는지 확인하기!!!!!!!!!!!
        2. 초기 주석에 [그러므로 visited는 일반블록에만 처리한다.] 이렇게 써놓고 망각한게 레전드
            이 경험 진짜 좋은경험...... 좀 더 빨리 초기주석을 한번 더 읽어봤으면 놓친 걸 알아냈을텐데 아쉽구만...
            그래도 발견해서 다행이다.ㅠㅠㅠㅠㅠㅠㅠㅠ
        3. 탑다운 설계도 잘했고, 처음에 구상을 잘해놔서 로직 구현엔 어렵지 않았다.
            앞으로도 이렇게만 차분히하자!!!!


# 문제 풀면서의 기록
문제설명
    1. 검은색(-1)/ 무지개(0)/ 일반 블록(1~M)이 있다
    2. 블록 그룹이 존재한다
        - 일반블록이 적어도 1개이고 그 일반블록은 색이 모두 같아야함
        - 검은블록 포함하면 안됨
        - 무지개는 얼마나 들어있든 상관 없음
        - 블록은 2보다 크거나 같음
        - 이 블록의 기준블록은 일반블록 중에서 행과 열이 가장 작은 것임
    3. 오토 플레이 기능
        크기가 가장 큰 블록을 찾음
        1.여러개면 무지개 블록의 수가 가장 많은 것
        2.그게 같다면 기준 블록의 행이 가장 큰것, 열이 가장 큰 것
        3. 블록 제거
    4. 중력/반시계/중력이 작용하는데
        -1 인 검은색 블록을 제외 한 모든 불록이 떨어진다.
구상
    - 오토플레이는 블록 그룹이 존재하는 동안 계속 반복됨;;
    1. 일단 가장 큰 블록 그룹을 찾아야한다.
        max_block = [], maxi = 0 로 두고
        각 점마다 bfs 돌려서 클 때마다 두개를 갱신해줘야함
        왜냐하면 0인애들은 일반블록이 모두 포함시킬 수 있기 때문 -> 이ㅓㄱ떄문이다
        그러므로 visited는 일반블록에만 처리한다.<-★★★★★★★★★★진짜 킹받네ㅠㅜㅜㅜ으휴 모질이
    2. 떨구는게 중요한데......
        떨어지는 애들을 F로 표시하자
        아래에서부터 내가 F이고 위의 숫자가 -1이 아닌 숫자면 떨어뜨려준다.
입력
    변 크기 N, 색상 갯수 M
출력
'''
from collections import deque


def bfs(r, c, num):
    q = deque([(r, c)])  # 0인애들 visited 처리 안한다.
    location, center, zero_visited = [], [], set()
    mujigae = 0
    while q:
        r, c = q.popleft()
        location.append((r, c))
        if grid[r][c] == 0:
            mujigae += 1
        else:
            center.append((r, c))
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc]:
                continue
            if grid[nr][nc] == num:
                visited[nr][nc] = True
                q.append((nr, nc))
            if grid[nr][nc] == 0 and (nr, nc) not in zero_visited:
                zero_visited.add((nr, nc))
                q.append((nr, nc))

    if len(location) <= 1:
        return -1, -1, -1, -1, []
    else:
        center.sort()
        return len(location), mujigae, center[0][0], center[0][1], location


def delete(location):
    for r, c in location:
        grid[r][c] = 9  # 9면 떨어진다.


def fall():
    for j in range(n):
        while True:
            down = 0
            for i in range(n - 1, 0, -1):
                if grid[i][j] == 9 and 0 <= grid[i - 1][j] < 6:
                    down += 1
                    grid[i][j], grid[i - 1][j] = grid[i - 1][j], grid[i][j]
            if down == 0:
                break


def myprint():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 9:
                print(" ", end=" ")
            elif grid[i][j] == -1:
                print("X", end=" ")
            else:
                print(grid[i][j], end=" ")
        print()


def rotation():
    copy_grid = [_[:] for _ in grid]
    for i in range(n):
        for j in range(n):
            grid[i][j] = copy_grid[j][n - i - 1]


score = 0
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

while True:
    visited = [[False] * n for i in range(n)]
    max_block = []
    for i in range(n):
        for j in range(n):
            if 0 < grid[i][j] < 6 and not visited[i][j]:
                visited[i][j] = True
                ele_maxi, ele_mujigae, ele_r, ele_c, ele_location = bfs(i, j, grid[i][j])
                if ele_maxi != -1:
                    max_block.append((ele_maxi, ele_mujigae, ele_r, ele_c, ele_location))
    if not max_block:  # 오토플레이 안되면 게임 끝
        break
    max_block.sort(reverse=True)
    maxi, muji, r, c, location = max_block[0]
    score += maxi * maxi
    delete(location)  # 이때 9로 표시
    fall()  # 떨굼
    rotation()  # 회전
    fall()  # 떨굼
print(score)
