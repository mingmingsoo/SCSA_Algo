'''
깨ㅏ아아ㅏ 내가 좋아하는 유형의 문제엥에에~~~
구현문제인데 시간초과나는건 제가 안일했다는 것이죠...

풀이시간 30분
구상
    에어컨에서 시작해서 방향대로 쭉쭉쭉 True 처리
    visited가 필요하겠네요.
    시간초과나서 3차원 visited 쓰겠음
'''
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

air = [[0] * m for i in range(n)]  # 에어컨 공기 표시
visited = [[[False] * 4 for i in range(m)] for i in range(n)]

air_list = []

for i in range(n):
    for j in range(m):
        if grid[i][j] == 9:
            air_list.append((i, j))
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]


def wind(r, c, k):
    sr, sc = r, c

    while True:
        if visited[r][c][k]:  # 이미 같은 위치, 같은 방향이면 갈 필요가 없음
            break
        visited[r][c][k] = True
        air[r][c] = 1  # 에어컨 표시

        nr = r + row[k]
        nc = c + col[k]

        # 탈출조건
        if not (0 <= nr < n and 0 <= nc < m):
            break
        if (nr == sr and nc == sc):
            break  # 다시 돌아왔다면 == 사이클이라면 탈출

        if grid[nr][nc] == 1:
            air[nr][nc] = 1
            if k == 1 or k == 3:  # 벽이면 어차피..
                break
        elif grid[nr][nc] == 2:
            air[nr][nc] = 1
            if k == 0 or k == 2:  # 벽이면 어차피..
                break
        elif grid[nr][nc] == 3:
            if k == 0 or k == 1:
                k = 1 - k
            elif k == 2 or k == 3:
                k = 5 - k
        elif grid[nr][nc] == 4:
                k = 3 - k
        r = nr
        c = nc


for r, c in air_list:
    for k in range(4):  # 에어컨이 있는 자리에서 4방 탐색
        wind(r, c, k)

ans = 0
for _ in air:
    ans += _.count(1)  # 에어컨 바람부는 자리 갯수 세주기
print(ans)
