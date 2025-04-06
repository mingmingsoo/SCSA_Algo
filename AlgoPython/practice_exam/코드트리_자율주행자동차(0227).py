'''
52/16
21:16
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
# 코드트리 자율주행자동차 (백준 14503 로봇청소기 )
2025.03.28.금
두번째 풀이(이지만 예전에 풀어봤어서 3번째 풀이)

문제 풀고 나서 기록
    제출 횟수 1회
    문제 시작 20:28
    문제 종료 20:39
    총 풀이시간 11분
        28~32   : 문제 이해 및 초기 주석(4)
        32~36   : 주석 기반 설계(4)
        36~39   : 테케 답 안나와서 디버깅(3)
               1. 움직이지 못했을 때만 후진하는 걸로 수정!
               2.  후진은 갔던 곳은 갈 수 있구나 방문 체크 확인하는거 제외!!

    메모리 17 KB
    시간 57 ms

    회고
        1. 조건 꼼꼼히!!!!! 맹심!

문제 풀면서의 기록
문제 설명
    1. 현재 d 기준 왼쪽 회전으로 간 적 없으면 인도일 경우 간다
        - 만약 인도거나 이미 간 곳이면 다시 좌회전
        - 4바퀴 다 돌았는데 못가면 방향 유지한 채 후진
    2. 다시 1번
        - 후진까지 못하면 끝.

입력
    맵 크기 n,m
    초기 r,c,d (0123 북동남서)
    맵 정보
        인도는 1
        테투리는 모두 1
        -> 범위 검사 안한다.
'''

n, m = map(int, input().split())
r, c, d = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

visited = [[False] * m for i in range(n)]
visited[r][c] = True
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
while True:
    # 1. 현재 d 기준 왼쪽 회전으로 간 적 없으면 인도일 경우 간다
    #     - 만약 인도거나 이미 간 곳이면 다시 좌회전
    move = False
    for k in range(4):
        d = (d + 3) % 4
        nr = r + row[d]
        nc = c + col[d]
        if not visited[nr][nc] and grid[nr][nc] == 0:
            move = True
            visited[nr][nc] = True
            r = nr
            c = nc
            break
    #     - 4바퀴 다 돌았는데 못가면 방향 유지한 채 후진
    if not move:
        back = False
        if not move:
            nr = r - row[d]
            nc = c - col[d]
            if grid[nr][nc] == 0:
                visited[nr][nc] = True
                back = True
                r = nr
                c = nc
        if not back:
            break

print(sum(map(sum, visited)))

'''
# 코드트리 자율주행자동차 (백준 14503 로봇청소기 )

# 두번째 풀이
    불필요한 visited True 주석처리, input, 범위 체크안해도됨 1로 패딩되어있다.


# 문제 풀고 나서 기록

    문제 시작 15:00
    문제 종료 15:26
    총 풀이시간 26분
        0~3분    : 문제 이해(3)
        3~7분    : 문제 구상 및 초기 주석(4)
        7~9분    : 탑다운 설계(주석 1,2,3,4 대로)(2)
        9~14분   : 코드 작성 완료(5)
        14~21분  : 1차 디버깅(7)
                    -> 무한 루프 도는 거 확인 -> 이동하고 나서 visited True 코드 추가
                    그래도 무한 루프 -> print로 r,c,d 확인 마지막 위치에서 헛돌음
                    cnt가 while 안에서 선언했었는데,  그거때문에 cnt 증가가 안돼서 헛도는 것 같아서
                    cnt 선언을 while 밖으로 뻈음
        21~25분  : 2차 디버깅(4)
                    visited 배열에 인도인 곳도 True 처리 되는 거 확인
                    -> 후진하는 로직에서 도로로만 가는 조건 빼먹은 거 확인
                    -> 그래도 안되서 다시 보니까 1번 이동때 cnt = 0으로 해주는게 없어서 추가했음
        25~26분  : 테케 확인, 범위 확인, 문제 조건과 내 코드가 맞는지 확인.(1)
        제출

    메모리 109544 KB
    시간 92 ms
    제출횟수 1회

    회고
    26분 중 디버깅을 11분했다.
    나름 주석대로 잘 짰다고 생각했는데 계획에 없던 cnt 변수를 사용하면서 놓친 부분이 있었던 듯
    visited True 는 왜 맨날 놓치니?^..^
    cnt를 쓰면서 어디,어디서 초기화 해줄건지 구상했었어야 했는데 생각이 부족했다.
    이런 시뮬레이션 그 잡채인 문제들은 조건을 잘 생각하자....!!!!!!!!!!!! 조건 조건 조건!!!
    
    아 백준하고 문제설명이 약~간 달라서 백준으로 푼 친구들과 코드가 조금 다르다.
    다음 복습(??) 때는 백준에서 풀면 될듯

문제설명
    1. 현재 방향 기준으로 왼쪽 방향으로 간 적 없으면 좌회전해서 1칸 간다
    2. 1번에서 이미 방문했거나 도로가 아니면 좌회전하고 1번으로 돌아감
    3. 4방향 모두 전진하지 못하면 후진(방향 유지)
    4. 후진 못하면 끝

입력
    맵 크기
    초기 위치, 방향
    맵 (도로 0, 인도 1)
출력
    총 면적 (visited가 True 인 애들의 갯수)

구상
    조건 잘 따져야...
'''
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
visited = [[False] * m for i in range(n)]
visited[r][c] = True
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
cnt = 0  # 헛도는거 확인용

while True:
    # 1. 현재 방향 기준으로 왼쪽 방향으로 간 적 없으면 좌회전해서 1칸 간다 -> 이게 근데 현재방향이 유지 되는건가?ㅠㅠ 아니라고 가정하고 풀자
    # 방향이 바뀌는게 맞았음. yeah!
    nr = r + row[(d + 3) % 4]
    nc = c + col[(d + 3) % 4]
    if not visited[nr][nc] and grid[nr][nc] == 0:
        # 이러면 갈 수 있다.
        cnt = 0  # 갔으니까 헛도는거 초기화
        visited[nr][nc] = True
        d = (d + 3) % 4
        r = nr
        c = nc
    else:
        # 2. 1번에서 이미 방문했거나 도로가 아니면 좌회전하고 1번으로 돌아감
        d = (d + 3) % 4  # 방향만 바꾸기
        cnt += 1  # 한바퀴 돌았다.
    if cnt > 3:  # 3. 4방향 모두 전진하지 못하면 == 나 한 자리에서 4번 돌았다.
        nr = r - row[d]
        nc = c - col[d]
        if grid[nr][nc] == 0:  # 후진할 수 있으면
            # 여기서 중요한건 visited를 따지지 않는 것
            # visited[nr][nc] = True # 이건 없어도 됨... 어차피 후진이니까
            r = nr
            c = nc
            cnt = 0  # 갔으니까 헛도는거 초기화
        # 4. 후진 못하면 끝
        else:
            break

ans = 0
for _ in visited:
    ans += _.count(True)
print(ans)
