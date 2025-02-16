'''
[문제 설명]
    뿌요는 떨어진다
    뿌요가 4개이상 상하좌우 연결되어있으면 뿌요가 없어진다 = 1연쇄
    뿌요가 소멸되면 위에 뿌요들이 떨어진다
    뿌요가 또 연쇄가 되면 또 터진다.
    4뿌요가 여러개 있으면 동시에 터진다.
[입력]
    12*6 배열
    . 빈공간 / 나머지는 색깔
[출력]
    연쇄 횟수
[구상]
    1. "."인 아닌 점들은 bfs를 돌리고 그 좌표를 모두 pang_set에 담는다.
    2. 만약 군집의 크기가 4개 이상인 애들이였으면 pang_set에 담긴 좌표들은 "."으로 바꿔준다
    -> 이때 pang+=1
    3. pong이 1개 이상 있었으면 (즉 군집이 4개이상인 애들이 하나라도 있었으면)
        떨어뜨리는 함수를 실행해준다.
    4. 만약 pang이 없으면 while을 탈출하면된다.
[필요한 메서드]
    bfs : 군집 갯수 세고 터뜨려준다.
    isDown : 떨어뜨려준다
[필요한 변수]
    ele_pang: bfs에서 연결된애들의 총 갯수
    pang: 4개이상의 뿌요들의 총 갯수
    pang_set : 4개이상의 뿌요들의 좌표를 담는 set
    ans : 게임의 진행 횟수, 즉 연쇄 횟수
    down: 떨어질 수 있는 칸의 총 갯수

'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(sr, sc, color):
    global pang
    visited[i][j] = True
    q = deque([(sr, sc)])
    pang_set = set()
    pang_set.add((sr, sc))
    ele_pang = 1  # 몇개의 뿌요가 있는가?
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if (not (0 <= nr < n and 0 <= nc < m)):
                continue
            if not visited[nr][nc] and grid[nr][nc] == color:
                ele_pang += 1
                visited[nr][nc] = True
                q.append((nr, nc))
                pang_set.add((nr, nc))
    if (ele_pang >= 4):  # 뿌요가 4개 이상이였으면
        pang += 1  # 여기 4연속 뿌요 하나 추가요
        while pang_set:
            r,c = pang_set.pop()
            grid[r][c] = "."


def isDown():
    # pang_grid 가 . 인 애들을 내려줘야함...
    for j in range(m):
        while True:
            down = 0  # 떨어뜨릴 수 있는 애들이 있는지 확인하기 위해 갯수를 세줌
            for i in range(n - 1, 0, -1):  # 뒤에서부터 떨어뜨려야 잘 떨어짐
                if (grid[i][j] == "." and grid[i - 1][j] != "."):
                    down += 1  # 여기 하나 떨어졌어요
                    grid[i][j], grid[i - 1][j] = grid[i - 1][j], grid[i][j]
            if (down == 0):  # 만약 떨어진 애들이 없으면 다음 열 검사
                break


n, m = 12, 6
grid = [list(input()) for i in range(n)]
ans = 0
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

while True:
    visited = [[False] * m for i in range(n)]
    pang = 0  # 4개이상 연속된 뿌요의 갯수

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] != ".":
                bfs(i, j, grid[i][j])

    if (pang == 0):  # 연속된 뿌요가 없으면 종료
        break

    ans += 1  # 있었으면 1 연쇄 증가

    isDown()  # 그리고 떨어뜨려주는 함수 실행

    # print("-----------")
    # for _ in grid:
    #     print(_)
print(ans)
