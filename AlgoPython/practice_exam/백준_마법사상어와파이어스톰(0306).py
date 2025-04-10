from collections import deque

p, on = map(int, input().split())
n = 2 ** p
grid = [list(map(int, input().split())) for i in range(n)]

order_lst = list(map(int, input().split()))


def rotation(sr, sc):
    small_grid = [_[sc:sc + m] for _ in grid[sr:sr + m]]
    # 얘를 4등분해
    small_grid1 = [_[:m // 2] for _ in small_grid[: m // 2]]
    small_grid2 = [_[m // 2:m] for _ in small_grid[:m // 2]]
    small_grid3 = [_[:m // 2] for _ in small_grid[m // 2:m]]
    small_grid4 = [_[m // 2:m] for _ in small_grid[m // 2:m]]

    for i in range(m // 2):
        for j in range(m // 2):
            grid[i + sr][j + sc] = small_grid3[i][j]
    for i in range(m // 2):
        for j in range(m // 2):
            grid[i + sr][j + sc + m // 2] = small_grid1[i][j]
    for i in range(m // 2):
        for j in range(m // 2):
            grid[i + sr + m // 2][j + sc] = small_grid4[i][j]
    for i in range(m // 2):
        for j in range(m // 2):
            grid[i + sr + m // 2][j + sc + m // 2] = small_grid2[i][j]


row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

for l in order_lst:
    m = 2 ** l
    # 잘라
    if l != 0:
        for i in range(0, n, m):
            for j in range(0, n, m):
                rotation(i, j)

    delete = set()
    for i in range(n):
        for j in range(n):
            ice = 0
            for k in range(4):
                nr = i + row[k]
                nc = j + col[k]
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc]:
                    ice += 1

            if ice < 3:
                delete.add((i, j))
    for r, c in delete:
        if grid[r][c]:
            grid[r][c] -= 1

# 최대 군집 갯수
maxi = 0
visited = [[False] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] and not visited[i][j]:
            visited[i][j] = True
            cnt = 0
            q = deque([(i, j)])
            while q:
                r, c = q.popleft()
                cnt += 1
                for k in range(4):
                    nr = r + row[k]
                    nc = c + col[k]
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
            maxi = max(maxi, cnt)

print(sum(map(sum, grid)))
print(maxi)


'''
# 코드트리 회전하는 빙하
2025.04.02 수
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 2회
    문제 시작 19:38
    1차 제출  20:40
    문제 종료 20:41

    총 풀이시간 63분
        38~42 : 문제 이해
        42~51 : 회전 로직
        51~56 : 얼음 녹이는 로직 -> 여기서 어 1번 테케 답이 저렇게 나올 수 가 없눈데? 생각..
                일단 그래도 bfs 로직 짜자 하고 작성
        56~00 : 얼음 군집 bfs 로직 작성
        00~41 : 1번 테케가 왜 다른지 문제 읽기..
                내가 생각한 회전이랑 문제 회전이 다른 거 였음!!!! 회전 로직 수정하기
        41~42 : 아차차 1번 테케 나와서 바로 제출했는데 l == 0 일땐 continue 해줘야함 ^^ 수정..

  메모리 25 MB
  시간 819 ms

  회고
    1. 백준 문제랑 달라서...... 너무나 당황함
        1번 테케 답이 저렇게 나올 수 가 없는데ㅠㅠㅠㅠㅋㅋㅋ 한참 헤메다가 문제 다른 거 알고
        회전 로직 고쳐서 수정했다.
        문제를 잘 읽자!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        이 문제는 4등분해서 사분면 회전이다.


'''

from collections import deque

poww, _ = map(int, input().split())
n = 2 ** (poww)

grid = [list(map(int, input().split())) for i in range(n)]
level_lst = list(map(int, input().split()))


def rotation(si, sj, level, half):  # half칸 씩 회전..?
    small_grid = [_[sj:sj + level] for _ in grid[si:si + level]]

    small_grid1 = [_[:half] for _ in small_grid[:half]]
    small_grid2 = [_[half:level] for _ in small_grid[:half]]
    small_grid3 = [_[:half] for _ in small_grid[half:level]]
    small_grid4 = [_[half:level] for _ in small_grid[half:level]]

    # 이걸 회전
    small_grid_lo = [[0] * level for i in range(level)]
    for i in range(half):
        for j in range(half):
            small_grid_lo[i][j] = small_grid3[i][j]
    for i in range(half):
        for j in range(half, level, 1):
            small_grid_lo[i][j] = small_grid1[i][j - half]

    for i in range(half, level, 1):
        for j in range(half):
            small_grid_lo[i][j] = small_grid4[i - half][j]

    for i in range(half, level, 1):
        for j in range(half, level, 1):
            small_grid_lo[i][j] = small_grid2[i - half][j - half]

    for i in range(level):
        for j in range(level):
            grid[i + si][j + sj] = small_grid_lo[i][j]


row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
for l in level_lst:
    if l != 0:

        level = 2 ** l
        for i in range(0, n, level):
            for j in range(0, n, level):
                rotation(i, j, level, level // 2)

    melting = [[0] * n for i in range(n)]
    # 얼음 녹이기
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                cnt = 0
                for k in range(4):
                    nr = i + row[k]
                    nc = j + col[k]
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc]:
                        cnt += 1
                if cnt <= 2:
                    melting[i][j] = 1  # 녹을 예정..

    for i in range(n):
        for j in range(n):
            if melting[i][j] and grid[i][j]:
                grid[i][j] -= 1

ans = 0
visited = [[False] * n for i in range(n)]


def bfs(r, c):
    cnt = 0
    q = deque([(r, c)])
    while q:
        r, c = q.pop()
        cnt += 1
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or not grid[nr][nc]:
                continue
            visited[nr][nc] = True
            q.append((nr, nc))
    return cnt


for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j]:
            visited[i][j] = True
            ans = max(ans, bfs(i, j))

print(sum(map(sum, grid)))
print(ans)

'''
# 세번째 풀이
    range함수
    천재들의 코드 참조 (summ = sum(map(sum, grid)))

# 두번째 풀이
    회전 간단히.
    함수화 명료하게.

# 백준 20058 마법사 상어와 파이어스톰

# 김혜준 지켜야할 거 리스트업

    1. 문제 천천히.꼼꼼히 제발
    2. 2차원 배열 만들 때 for in range(n) 안붙힘
    3. 극간값 생각하기 예를 들어 100초까지면 99초까지봤음
    4. 작성시 한줄한줄 꼼꼼히 와라라락 쓰면 안됨.
    5. 보기랑 테케랑 다를 수 있으니 명심 
    문제 시작 09:00
    문제 종료 10:03
    총 풀이시간 63분
        0~16분   : 문제 이해(16)
                    회전시키는거야 이해못할게 없는데
                    얼음이 줄어드는 조건이 이해가 안돼서 16분동안 생각했다.
                    도저히 모르겠어서 첫번째 테케의 전체 sum 을 구했고
                    출력값과 4 차이나는 것을 알 수 있었다.
                    모두 1이상의 값인데 어디선가 -1 씩 4번 빠진거라 모서리라고 판단했고
                    그 판단 이후 다시 읽어보니까 이해가 됐다...........

                    어렸을 때 책 좀 많이 읽을걸..ㅎ파이어스톰에서 회전됐는데 보기랑 테케 달라서 계속 틀린줄 암

# 문제 풀고 나서 기록


        16~29분  : 회전 로직1(13)
                    보기랑 테케 다른거 인지하지 못하고
                    왜 안되지?! 왜 안되지?! 하고 있음.;;;;;;;;

        29~47분  : 회전 로직2(18)
                    small_grid 사용해서 회전로직 완료.
                    진작에 이렇게 할걸 한번에 회전시키고 싶어서 고생했습니다.
                    1~64 값을 가지는 문제의 보기 같은 테케 만들기
                    잘 돼서 회전 로직 완료

        47~51분  : 얼음 녹이는 로직 설계(4)
        51~55분  : sum과 군집 갯수 구하는 로직 설계(4)
                    음수값 나와서 1이상인 애들만 녹게 로직 수정

        56~63분  : 몇개 테케가 답이 다른게 나와서 디버깅
                1.  군집 최대 갯수가 내 눈으로도 60개인데
                    61개라고 나와서 보니까
                    군집 갯수 샐때 0일 때도 군집 시작하게 해서 수정.
                2.  얼음 녹일 때 녹으면 안되는 곳도 녹길래 보니까
                    new_grid 의 count를 세줘야하는데 grid로 되어있어서 수정

    메모리 123072 KB
    시간 460 ms

    회고
        1. 문제 이해가 안가서 눈물 흘릴 뻔....
            그래도 sum 갯수 구해서 이해해서 다행이다ㅠㅠㅠ 삼성 화법을 익히자
        2. 문제 보기랑 테케가 다른데 테케를 넣어보면서 왜 보기처럼 회전 안되지?!?! 한건 레전드 바보짓
            이 사실을 인지하자....
            이 사실을 인지하자....
            이 사실을 인지하자....
            이 사실을 인지하자....
            다음엔 이런 실수 안할거야...........

            그리고 회전 한번에 하려고 하지말고
            small_grid 만들어서하기..........
            왜 한번에 하려고 욕심냇니
        3. 회전 로직 끝나고 맘이 급해져서 얼음 줄이는 함수랑 군집 구하는 함수
            와라라라라락 작성해버림
            그래서 조건을 많이 놓쳤다.
            (ㄱ)얼음은 min 0까지.
            (ㄴ)군집은 0은 안됨.
             불과 하루 전에 [작성시 한줄한줄 꼼꼼히, 와라라락 쓰면 안됨.] 라고 썼는데 말이다.
        4. 내가 해야될 것
            차분함을 연습하기, 노력하기 명심.................


문제 설명
    이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은
    얼음의 양이 1 줄어든다.
    (r, c)와 인접한 칸은 (r-1, c), (r+1, c), (r, c-1), (r, c+1)이다.

    이 말이 잘 이해가 안간다. 아직도 이해 안가네.. # 회전 시켜봐야 알듯
    추측하기론 3개이상의 얼음을 bfs다 묶고 그 visited 가 아닌 애들을 빼주는 것 같다
    아
    각 count 가 내 주변이 사방이 2개이하면 줄어든다고 ㅇㅋ


'''
###############################################################
# 정리한 세번째 풀이

from collections import deque


def oob(r, c):
    return 0 <= r < N and 0 <= c < N


def rotation(size):  # 회전하는 함수
    # 내가 필요한 것 시작점들과 가로의 길이

    for sr in range(0, N, size):
        for sc in range(0, N, size):
            for i in range(0, size):
                for j in range(0, size):
                    new_grid[i + sr][j + sc] = grid[size - j - 1 + sr][i + sc]


def remove():  # 주변 갯수 세서 줄여주는 함수
    remove_grid = [[False] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            ele_round = 0
            for k in range(4):
                nr = i + row[k]
                nc = j + col[k]
                if not oob(nr, nc) or new_grid[nr][nc] <= 0:
                    continue
                ele_round += 1
            if ele_round <= 2:
                remove_grid[i][j] = True

    for i in range(N):
        for j in range(N):
            if remove_grid[i][j]:
                if new_grid[i][j] > 0:
                    new_grid[i][j] -= 1


def bfs(r, c):  # 군집 갯수 구하는 함수
    global cluster
    visited[r][c] = True
    q = deque([(r, c)])
    ele = 0

    while q:
        r, c = q.popleft()
        ele += 1
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not oob(nr, nc) or visited[nr][nc] or grid[nr][nc] <= 0:
                continue
            q.append((nr, nc))
            visited[nr][nc] = True

    cluster = max(cluster, ele)


n, m = map(int, input().split())
N = 2 ** n
grid = [list(map(int, input().split())) for i in range(N)]
L_list = map(int, input().split())
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

# 메인로직
for L in L_list:
    new_grid = [[0] * N for i in range(N)]
    rotation(2 ** L)  # 회전해
    remove()  # 얼음 줄어들어
    grid = new_grid

# 출력값들 구하기
# 1. 합
summ = sum(map(sum, grid))
# 2. 클러스터 최대 크기
cluster = 0
visited = [[False] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j] and grid[i][j] > 0:
            bfs(i, j)
print(summ)
print(cluster)

##############################################################
# 정리안된 첫번째 풀이...
from collections import deque

n, m = map(int, input().split())
N = 2 ** n
grid = [list(map(int, input().split())) for i in range(N)]
L_list = map(int, input().split())


# for row in grid:
#     print(row)


def rotation(size):
    for sr, sc in start_list:
        small_grid = [[0] * size for i in range(size)]
        for i in range(0, size):
            for j in range(0, size):
                small_grid[i][j] = grid[size - j - 1 + sr][i + sc]
        for i in range(0, size):
            for j in range(0, size):
                new_grid[i + sr][j + sc] = small_grid[i][j]
        # for i in range(sr, sr+size): # 같음. 상대위치를 절대 위치로 변환
        #     for j in range(sc, sc+size):
        #         new_grid[i][j] = small_grid[i-sr][j-sc]


row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
for L in L_list:
    new_grid = [[0] * N for i in range(N)]
    # 내가 필요한 것
    # 시작점들과 가로의 길이
    start_list = []
    for i in range(0, N, 2 ** L):
        for j in range(0, N, 2 ** L):
            start_list.append((i, j))

    rotation(2 ** L)

    remove_grid = [[False] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            ele_round = 0
            for k in range(4):
                nr = i + row[k]
                nc = j + col[k]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if new_grid[nr][nc] > 0:
                    ele_round += 1
            if ele_round <= 2:
                remove_grid[i][j] = True

    for i in range(N):
        for j in range(N):
            if remove_grid[i][j]:
                new_grid[i][j] -= 1
                if new_grid[i][j] < 0:
                    new_grid[i][j] = 0

    grid = new_grid

summ = 0
for _ in grid:
    summ += sum(_)
print(summ)

cluster = 0


def bfs(r, c):
    global cluster
    visited[r][c] = True
    q = deque([(r, c)])
    ele = 0

    while q:
        r, c = q.popleft()
        ele += 1
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
                continue
            if grid[nr][nc] > 0:
                q.append((nr, nc))
                visited[nr][nc] = True

    cluster = max(cluster, ele)


visited = [[False] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j] and grid[i][j] > 0:
            bfs(i, j)
print(cluster)
