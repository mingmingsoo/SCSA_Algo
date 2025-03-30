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
            grid[i][j] = -1 # 택시 넘버링해줄거라 못가는 곳은 -1처리
r, c = map(lambda x: int(x) - 1, input().split())
end_info = {}
for mm in range(m):
    sr, sc, er, ec = map(lambda x: int(x) - 1, input().split())
    end_info[mm + 1] = (er, ec) # 도착지 정보 기록해두기
    grid[sr][sc] = mm + 1 # 맵에 넘버링 해주기


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
        if user: # 손님 태울 수 있었으면 데리러 간다
            used_power, next_r, next_c, next_numbering = heapq.heappop(user)
        else: # 손님이 있는데 못데리러 가면 종료 (손님이 벽에 둘러 쌓인 경우가 될 거임.)
            power = -1
            break
        if used_power > power: # 근데 가는길에 연료 바닥났었으면 불가함 종료
            power = -1
            break

    grid[next_r][next_c] = 0 # 태웠으니까 맵에 0처리
    power -= used_power # 연료 소모 반영
    r, c = next_r, next_c # 택시 위치 반영

    # [2] 손님 데려다주기(bfs)
    er, ec = end_info[next_numbering] # 목적지
    used_power = 0

    visited = [[False] * n for i in range(n)]
    visited[r][c] = True
    q = deque([(r, c, 0)])
    end = False # 못데려다줬으면 납치이므로 -1 처리 해줄거임 그래서 필요한 플래그
    while q:
        r, c, dist = q.popleft()
        if r == er and c == ec:
            used_power = dist
            end = True # 데려다줬습니다!
            break
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc] or grid[nr][nc] == -1:
                continue
            visited[nr][nc] = True
            q.append((nr, nc, dist + 1))
    if used_power > power: # 연료바닥났으면.. 미션 실패
        power = -1
        break
    if not end: # 납치 했어도 미션 실패 ..
        power = -1
        break
    # 연료 반영
    power -= used_power
    power += used_power * 2
    # 택시 위치 반영
    r, c = er, ec
print(power)
