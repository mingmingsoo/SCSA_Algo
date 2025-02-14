'''
문제설명
    운석이 떨어지면 용암이 분출
    용암이 분출되면 상하좌우 인접한 화산지대도 1일 후 용암이 분출
    운석이 떨어진 좌표를 주고
    분출이 완료될 때 까지의 기간과 분출하지 않은 화산지대의 면적 출력

입력
    행 열 운석갯수
    운석위치

구성
    운석이 떨어진 곳이 용암이면 q에 담는다
    그리고 퍼진다. 토마토와 유사하게

주의사항
    운석이 화산지대로 떨어진다는 조건이 없음. 평지로 떨어지면 아무일도 안일어남
    -> 잘 보고 q에 담아야한당...

반례
1
4 4 2
2 1
0 3
0 0 0 0
0 1 0 1
1 1 0 0
0 1 1 1

정답은 4 1
운석처리 안했으면 4 0 이 출력될 것
'''

def bfs():
    global ans
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]

    while q:
        r, c, cnt = q.popleft()
        ans = max(ans, cnt)
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if (not (0 <= nr < n and 0 <= nc < m)):
                continue
            if (not visited[nr][nc] and grid[nr][nc] == 1):
                visited[nr][nc] = True
                q.append((nr, nc, cnt + 1))

T = int(input())
for tc in range(T):
    from collections import deque

    star_list = []
    n, m, s = map(int, input().split())
    for i in range(s):
        r, c = map(int, input().split())
        star_list.append((r, c)) # 운석의 정보들
    grid = [list(map(int, input().split())) for i in range(n)]
    q = deque()
    visited = [[False] * m for i in range(n)]
    for r, c in star_list:
        if (grid[r][c] == 1): # 운석이 떨어진 곳이 화산이면!
            q.append((r, c, 1))
            visited[r][c] = True
    ans = 0

    bfs()
    not_bomb = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]: # 화산인데 터지지 않았으면
                not_bomb += 1

    print(f"#{tc+1} {ans} {not_bomb}")