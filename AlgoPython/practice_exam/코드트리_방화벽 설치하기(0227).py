'''
# 코드트리 방화벽 설치하기 (백준 14502 연구소)

2025.03.28.금
두번째 풀이(이지만 예전에 풀어봤어서 3번째 풀이)
문제 풀고 나서 기록

    제출횟수 1회
    문제 시작 20:42
    문제 종료 20:51
    총 풀이시간 9분
        42~43   : 문제 이해 및문제 구상 및 초기 주석(1)
        43~46   : combi 설계(3)
        46~51   : bfs 설계(5)


    메모리 25 MB
    시간 314 ms

문제 풀면서의 기록
문제 설명
    기존에 설치되어 있는 방화벽 제외 3개 추가해서 설치한다.
    불이 퍼지는 영역이 최대일 때 그 크기는?
입력
    불2 벽1 빈칸0 <- 이걸 combi
구상
    combi
'''
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
arr = []
two = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            arr.append((i, j))
        elif grid[i][j] == 2:
            two.append((i, j))
sel = [0] * 3

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]
ans = 0


def combi(sidx, idx):
    global ans
    if sidx == 3:
        grid_simul = [_[:] for _ in grid]
        q = deque(two)
        for r, c in sel:
            grid_simul[r][c] = 1
        while q:
            r, c = q.popleft()
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if 0 <= nr < n and 0 <= nc < m and grid_simul[nr][nc] == 0:
                    grid_simul[nr][nc] = 2
                    q.append((nr, nc))
        sm = 0
        for i in range(n):
            for j in range(m):
                if grid_simul[i][j] == 0:
                    sm += 1
        ans = max(ans, sm)
        return

    if idx == len(arr):
        return

    sel[sidx] = arr[idx]
    combi(sidx + 1, idx + 1)
    combi(sidx, idx + 1)


combi(0, 0)
print(ans)


'''
# 코드트리 방화벽 설치하기 (백준 14502 연구소)

# 두번째 풀이
    count 함수 적용, input, 등

문제 풀고 나서 기록

    문제 시작 13:40
    문제 종료 14:00
    총 풀이시간 20분
        0~2분    : 문제 이해(2)
        2~4분    : 문제 구상 및 초기 주석(2)
        4~8분    : 탑다운 설계(4) # combi 메서드 안에 bfs 가 있어서 combi 작성 완료까지 하고 탑다운
        8~12분   : count, bfs 함수 작성 완료(4)
        12~18분  : 로직은 맞는데 답이 크게 나와서 당황. 디버깅 시작(6)
                    -> 처음 콤비에서는 디버깅으로 잘 되는걸 확인했음
                    -> 보니까 두번째 콤비부터 bfs가 안됨
                    -> 확인해보니 q에 아무것도 안담겨 있음
                    -> q가 얕은복사 되서 그랬음 -> 깊은 복사로 바꿈.
                    -> 디버깅 하면서 vistied의 필요를 못느껴서 지움 (11차원 토마토 문제 생각이났음)
        18~20분 : 오타없는지, 디버깅용 print 없는지, 범위 확인(2)
        제출

    메모리 116328 KB
    시간 316 ms

    회고======================================================================================================================
    q = origin_q 하면서 약간 의심스러웠는데 역시나 복사가 잘 안됐음
    그래도 나름 오류를 빨리 잡은 것 같음
    deque를 복사해본건 처음.. 덱은 슬라이싱 복사가 안되는걸 배움. copy 쓰거나 deque(origin_q) 담아버리기

    원본 배열을 바꿀 경우
    1. 원본배열복사본으로 로직을 처리한다
    2. 원본을 바꾼다음에 다시 원본배열로 바꾼다
    두가지가 있으면 2가 편하다. -> 전역변수만 해버리면 되고, 1번은 함수안의 함수면 함수에 달고다녀줘야함.ㅠ bfs(grid_copy) 요런식으로
    ★괜히 1로했다가 디버깅을 q에 초점을 못맞췄음 2번 한가지로 통일하기.★

    count를 쓸거면서 count 이름의 함수를 만든건 잘못했음
    =========================================================================================================================

문제설명
    방화벽을 3개까지 추가로 설치할 수 있을 때
    불이 안번지는 최대 갯수는?
입력
    맵크기
    2 불 1 벽 0 퍼질 수 있음
구상
    3개 선택은 조합으로 하고
    모든 경우의 수에서 bfs로 돌리기
필요한 메서드
    combi : 방 3개 조합
    bfs : 불 퍼짐
    count : 불이 안퍼지는 갯수 세기 -> ans 갱신 필요

'''

from collections import deque
import sys

input = sys.stdin.readline


def combi(sidx, idx):  # 방화벽 설치 가능한 조합으로 bfs 돌릴 거임.
    global ans, grid

    if sidx == 3:  # 조합 끝
        grid_copy = [_[:] for _ in grid]

        q = deque(origin_q)  # 여기서 q = origin_q 해서 디버깅했음.. 깊은 복사 해줘야됨. 덱이라 슬라이싱은 안된다.

        for r, c in location_sel:  # 선택한 곳 방화벽 처리
            grid[r][c] = 1

        bfs(q)  # 불 확장

        ans = max(no_fire_count(grid), ans)  # 안전한 곳 갯수 세기

        grid = [_[:] for _ in grid_copy]  # 맵 원상 복구

        return

    if idx == len(location_arr):
        return

    location_sel[sidx] = location_arr[idx]
    combi(sidx + 1, idx + 1)
    combi(sidx, idx + 1)


def bfs(q):
    while q:
        r, c = q.popleft()

        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < m):
                continue

            if grid[nr][nc] == 0:  # 불 확장 가능하면
                grid[nr][nc] = 2  # 모두 퍼져나감
                q.append((nr, nc))  # visited 굳이 필요 없을듯 -> 그래서 썼다가 안썼음


def no_fire_count(grid):  # 안전구역 갯수 세주는 함수
    no_fire = 0

    for _ in grid:
        no_fire += _.count(0)  # 간단히..

    # for i in range(n):
    #     for j in range(m):
    #         if grid[i][j] == 0:
    #             no_fire += 1

    return no_fire


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

location_arr = []  # 벽을 세울 수 있는 전체 좌표 = 즉 0인 좌표를 모두 담을 것임
location_sel = [0] * 3  # 벽 3개만 고를거임

origin_q = deque()  # 모든 경우의 수에서 q에 담지 않게 미리 2인 값(==불) 담아주기
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:  # 벽을 세울 수 있는 곳 모두 담기
            location_arr.append((i, j))
        elif grid[i][j] == 2:  # 불을 q에 미리 담기
            origin_q.append((i, j))

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

ans = 0
combi(0, 0)
print(ans)
