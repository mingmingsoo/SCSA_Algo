'''
문제
    한수는 왼쪽아래에서 오른쪽 위를 목표로 간다.
    T인 곳은 가지 못한다.
    집까지 갈 수 있는 길중에 거리가 K인 총 경우의 수
입력
    .과 T로만 이루어진 맵
구상
    dfs로 뚜까패
'''
import sys
input = sys.stdin.readline
n, m, d = map(int, input().split())
grid = [list(input()) for i in range(n)]
visited = [[False] * m for i in range(n)]
# print(grid)
ans = 0

row = [1, -1, 0, 0]
col = [0, 0, 1, -1]


def dfs(r, c, er, ec, dist):
    global ans
    if(dist>d): # 백트래킹 추가, 길이가 더 길어지면 볼 필요도 없음
        return

    if r == er and c == ec: # 도착점에 다 왔고
        if (dist == d): # 거리가 지정 거리와 같다면
            ans += 1 # 경우의 수 추가.
        return

    visited[r][c] = True # 왔다고 표시 했다가
    for k in range(4):
        nr = r + row[k]
        nc = c + col[k]

        if not (0 <= nr < n and 0 <= nc < m):
            continue

        if (not visited[nr][nc] and grid[nr][nc] != "T"):
            dfs(nr, nc, er, ec, dist + 1)
    visited[r][c] = False # 총 경우의 수이므로 다시 방문 해제


dfs(n - 1, 0, 0, m - 1, 1)  # 시작점(왼쪽밑), 끝점(오른쪽위), 지금까지 이동거리

print(ans)
