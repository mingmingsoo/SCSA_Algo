'''
# 코드트리 자율주행 전기차
2025.04.01.월
두번째 풀이

# 문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 20:42
    문제 종료 21:16

    총 풀이시간 34분
        42~50 : 문제 이해 및 초기 주석(8)
        50~52 : 입력 받기(2)
        52~58 : 탑다운 설계(6)
        58~03 : bfs_in 함수 작성(5)
        03~06 : bfs_in 함수 확인(3)
        06~07 : bfs_out 함수 작성(1)
        07~10 : bfs_out 함수 확인(3)
                -> 택시 위치 갱신 안해줘서 수정!
        10~16 : 검증(6)
                (1) 문제 예시랑 같은 택시 이동인지 확인
                (2) 못데려다 줄때, 못 태우러 갈때 -1 출력되는지 확인
                (3) 택시 위치가 손님 위치일 때 확인

  메모리 16 MB
  시간 52 ms

    회고
        1. 검증 하면 좋은 것 밖에 없다. 검증 필수

# 문제 풀면서 기록
처음보는 문제라 생각하자
문제 설명이 좀 정신 없는데
    1. 내 위치에서 최단 거리 승객 태운다 (위.왼)
    2. 목적지 까지 데려다준다
        - > 이동한 거리만큼 베터리 충전
        -> 가는 길에 엔꼬나면 -1 출력
    3. 베터리 충전은 태우고 나서의 거리만큼 * 2 충전된다 풀 거리가 아니다.
입력
    맵 크기 N, 승객 수 M, 처음 연료
    맵 정보
    손님 정보

필요한 변수
    end_dict : 출발지는 모두 다르기에 목적지를 딕셔너리로 담는다.
필요한 함수
    bfs

5 3 10
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
1 1 0 0 0
0 0 0 0 0
1 1
5 1 5 2
5 2 5 3
5 3 5 4

손님 못태워

5 1 10
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
1 1 0 0 0
0 0 0 0 0
1 1
1 2 5 5

3 1 10
0 0 0
0 0 0
0 0 0
1 1
1 1 3 3
내 위치가 손님위치

'''
from collections import deque

n, sonim_num, power = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
sonim_grid = [[0] * n for i in range(n)]
r, c = map(lambda x: int(x) - 1, input().split())  # 택시 위치
end_dict = {}
for s in range(sonim_num):
    sr, sc, er, ec = map(lambda x: int(x) - 1, input().split())
    end_dict[s + 1] = (er, ec)
    sonim_grid[sr][sc] = (s + 1)  # 넘버링

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]


def bfs_in(tr, tc):  # 택쉬
    visited = [[False] * n for i in range(n)]
    visited[tr][tc] = True
    q = deque([(tr, tc, 0)])
    while q:
        for qs in range(len(q)):
            tr, tc, dist = q.popleft()
            if sonim_grid[tr][tc]:
                close_lst.append((dist, (tr, tc)))

            for k in range(4):
                nr = tr + row[k]
                nc = tc + col[k]
                if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or grid[nr][nc]:
                    continue
                visited[nr][nc] = True
                q.append((nr, nc, dist + 1))
        if close_lst:
            return


def bfs_out(sr, sc, er, ec):
    visited = [[False] * n for i in range(n)]
    visited[sr][sc] = True
    q = deque([(sr, sc, 0)])
    while q:
        for qs in range(len(q)):
            r, c, dist = q.popleft()
            if (r, c) == (er, ec):
                return dist
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or grid[nr][nc]:
                    continue
                visited[nr][nc] = True
                q.append((nr, nc, dist + 1))
    return -1


for sonim in range(sonim_num):  # 손님 수 만큼만 돌겠죵
    close_lst = []  # 가까운 손님들 담기 (거리, (좌표))
    bfs_in(r, c)
    if not close_lst:
        power = -1  # 손님 못태웠슈!!!!
        break
    close_lst.sort()
    dist, sr, sc = close_lst[0][0], close_lst[0][1][0], close_lst[0][1][1]

    power -= dist
    if power <= 0:
        power = -1  # 엥꼬낫슈
        break

    (er, ec) = end_dict[sonim_grid[sr][sc]]
    sonim_grid[sr][sc] = 0
    dist = bfs_out(sr, sc, er, ec)
    r, c = er, ec

    if dist == -1:
        power = -1  # 못데려다줫슈
        break
    power -= dist
    if power < 0:  # = 아니여도 되는지
        power = -1  # 엥꼬낫슈
        break

    power += dist * 2
print(power)

'''
# 19238 백준 스타트 택시
# 체감난이도 골2

# 문제 풀고 나서 기록

    문제 시작 14:00
    1차 제출 14:44
    문제 종료 14:55
    총 풀이시간 55분
        00~06   : 문제 이해(4)
        04~10   : 문제 구상 및 초기 주석(6)
        10~14   : 입력 받기(4)
                    원래 1인곳 -1 처리,
                    시작위치(2차원 배열), 목적지(딕셔너리) 각각 다르게 기록
        14~16   : 탑다운 설계(2)
        16~26   : 손님 데러러 가는 로직 설계(10)
                    2번 손님 잘 태우는지 확인
        26~30   : 손님 데려다 주는 로직 설계(4)
        30~38   : 1번 테케 14가 아닌 15가 나와서 디버깅 시작(8)
                    (1) 손님 태우고 맵에 0으로 안바꿔줘서 계속 2번 손님만 태우는 거 확인
                        grid[r][c] = 0 수정 완료
                    (2) 1번 손님 아닌 3번 먼저 태워서 힙큐를 while 문 밖으로 위치시켜서 수정
        38~40   : 3번 테케 인덱스 에러나서 확인(2)
                    손님을 못데리러 갈 경우 next_r, next_c이 -1,-1 이여서 오류가났음!
                    -> 손님을 못태울 경우, 손님을 못데려다줄 경우 실패하는 로직으로 수정
                    (end 플래그 사용)
        40~44   : 택시 시작위치가 손님이 있는 곳일 때 반례가 생각나서 반례 만들어봄(4)
                    visited[r][c] = True 만 주석처리 하면 된다고 생각했음
                    그리고 1차 제출 -> 틀렸습니다
        44~55   : 만든 반례에서 답이 19인데 17 나온 거확인(11)
                   visited[r][c] = True 를 해버리면 dist가 무조건 2가 되기에 생기는 오류 확인
                   로직 수정!

    메모리 115720 KB
    시간 216 ms

    회고
        1. 아 반례까지 만들어놓고 -1 안나온다고 내버린거 바보같음.. 계산은 해봤어야지 이사람아
        2. 시간 줄이는 거 고려해보기

# 문제 풀면서의 기록
문제설명
    1. 최단경로에 있는 승객 태우는데 행, 열 우선순위
    2. 승객태우고~ 도착까지 사용된 연료*2 를 목적지에 도달하면 채워짐(갈 때가 아니라)
    3. 이동 중 바닥나면 실패 업무끝 -1
    4. 모든 손님 이동할수 없으면 -1
구상
    bfs 힙큐 쓰고 다 돌아도 괜찮을듯?
    2차원 배열에 시작위치에만 손님 표시하고(인덱스 넘버링)
    인덱스와 도착위치를 담은 딕셔너리 생성
입력
    맵 크기, 손님 수, 처음 연료
    맵 정보
    택시 시작위치
    승객 위치

반례
6 1 15
0 0 1 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
5 5
5 5 0 0
정답 -1

6 1 15
0 0 1 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
5 5
5 5 3 3
19
택시 시작 위치가 승객일 때

'''
import heapq
from collections import deque

n, m, power = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            grid[i][j] = -1  # 택시 넘버링해줄거라 못가는 곳은 -1처리
r, c = map(lambda x: int(x) - 1, input().split())
end_info = {}
for mm in range(m):
    sr, sc, er, ec = map(lambda x: int(x) - 1, input().split())
    end_info[mm + 1] = (er, ec)  # 도착지 정보 기록해두기
    grid[sr][sc] = mm + 1  # 맵에 넘버링 해주기

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

ans = -1
for mm in range(m):
    used_power, next_r, next_c, next_numbering = -1, -1, -1, -1
    # [1-1] 혹시 내 위치가 손님 위치..?
    if grid[r][c] != 0 and grid[r][c] != -1:
        used_power = 0
        next_r = r
        next_c = c
        next_numbering = grid[r][c]
    # [1-2] 아니라면 최단경로 손님 찾기(bfs) -> 힙큐에 후보 담아줌
    else:
        user = []
        visited = [[False] * n for i in range(n)]
        visited[r][c] = True
        q = deque([(r, c, 0)])
        used_power, next_r, next_c, next_numbering = -1, -1, -1, -1
        while q:
            r, c, dist = q.popleft()
            for k in range(4):
                nr = r + row[k]
                nc = c + col[k]
                if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or grid[nr][nc] == -1:
                    continue
                if grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    q.append((nr, nc, dist + 1))
                elif grid[nr][nc] != 0:
                    visited[nr][nc] = True
                    q.append((nr, nc, dist + 1))
                    heapq.heappush(user, (dist + 1, nr, nc, grid[nr][nc]))
        if user:  # 손님 태울 수 있었으면 데리러 간다
            used_power, next_r, next_c, next_numbering = heapq.heappop(user)
        else:  # 손님이 있는데 못데리러 가면 종료 (손님이 벽에 둘러 쌓인 경우가 될 거임.)
            power = -1
            break
        if used_power > power:  # 근데 가는길에 연료 바닥났었으면 불가함 종료
            power = -1
            break

    grid[next_r][next_c] = 0  # 태웠으니까 맵에 0처리
    power -= used_power  # 연료 소모 반영
    r, c = next_r, next_c  # 택시 위치 반영

    # [2] 손님 데려다주기(bfs)
    er, ec = end_info[next_numbering]  # 목적지
    used_power = 0

    visited = [[False] * n for i in range(n)]
    visited[r][c] = True
    q = deque([(r, c, 0)])
    end = False  # 못데려다줬으면 납치이므로 -1 처리 해줄거임 그래서 필요한 플래그
    while q:
        r, c, dist = q.popleft()
        if r == er and c == ec:
            used_power = dist
            end = True  # 데려다줬습니다!
            break
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or grid[nr][nc] == -1:
                continue
            visited[nr][nc] = True
            q.append((nr, nc, dist + 1))
    if used_power > power:  # 연료바닥났으면.. 미션 실패
        power = -1
        break
    if not end:  # 납치 했어도 미션 실패 ..
        power = -1
        break
    # 연료 반영
    power -= used_power
    power += used_power * 2
    # 택시 위치 반영
    r, c = er, ec
print(power)
