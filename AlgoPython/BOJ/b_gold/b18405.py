'''
13:30~13:42

문제 설명
    바이러스가 퍼지는데 우선순위는 낮은 숫자임
입력
    맵 크기, 바이러스 갯수 K
    맵
    시간 S, 위치
구상
    q를 리스트로하고 입력받고나서 sort 해주면 알아서 우선순위에 맞게 퍼진다.
'''

n, num = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
time, x, y = map(int, input().split())

q = []  # 정렬위해 리스트로
for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            q.append((grid[i][j], i, j, 0))
q.sort(key=lambda x: x[0])


def bfs():
    # visited 는 맵을 바꿔줄 것이기 때문에 필요 없음.
    row = [-1, 1, 0, 0]
    col = [0, 0, 1, -1]
    while q:
        numbering, r, c, t = q.pop(0)
        if (t >= time):
            return
        for k in range(4):
            nr = r + row[k]
            nc = c + col[k]
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if grid[nr][nc] == 0:
                grid[nr][nc] = numbering
                q.append((grid[nr][nc], nr, nc, t + 1))


bfs()

print(grid[x - 1][y - 1])
