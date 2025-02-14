'''
[문제 설명]
    어떤 칸을 클릭했을 때 지뢰가 있는 칸을 제외한 모든 칸들의 숫자가 표시되려면 최소 몇번 클릭해야하는가?
[구상]
    1. 먼저 지뢰가 아닌 곳에 근방에 지뢰가 몇개 있는지 담는 배열을 만든다.(지뢰면 -1)
    2. 근데 무조건 0먼저 눌러야 장땡아닌가?
    3. 그래서 무조건 0먼저 누르게 하겠다.
    4. bfs로 풀겠다
'''
from collections import deque


def count_pang(r, c):  # 주변에 몇개의 지뢰가 있는지 세주는 함수
    pang = 0
    for k in range(8):
        nr = r + row[k]
        nc = c + col[k]
        if (not (0 <= nr < n and 0 <= nc < n)):
            continue
        if (grid[nr][nc] == "*"):
            pang += 1
    return pang


def bfs(i, j):
    global cnt
    q = deque([(i, j)])

    while q:
        cnt+=1
        r, c = q.popleft()
        for k in range(8):
            nr = r + row[k]
            nc = c + col[k]
            if (not (0 <= nr < n and 0 <= nc < n)):
                continue
            if (info[nr][nc] == 0):
                info[nr][nc] = -1
                q.append((nr, nc))
            if(info[nr][nc] != -1):
                info[nr][nc] = -1

T = int(input())
for tc in range(T):

    n = int(input())
    grid = [list(input()) for i in range(n)]
    info = [[0] * n for i in range(n)]
    row = [1, -1, 0, 0, 1, 1, -1, -1]
    col = [0, 0, 1, -1, 1, -1, 1, -1]

    ans = 0
    for i in range(n):
        for j in range(n):
            if (grid[i][j] == "*"):
                info[i][j] = -1
            else:
                info[i][j] = count_pang(i, j)
    cnt= 0
    for i in range(n):
        for j in range(n):
            if (info[i][j] == 0):  # 0인 애들만 담는다.
                info[i][j] = -1
                bfs(i, j)  # info를 다 -1 로 만들어버려
                ans += 1

    # info 가 -1이 아닌애들 세주기 (== 0에 의해 못터진 애들)
    for i in range(n):
        for j in range(n):
            if info[i][j] != -1:
                ans += 1

    print(f"#{tc + 1} {ans}")
    print(cnt)
