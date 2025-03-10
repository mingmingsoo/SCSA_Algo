# visited 3차원 -> 몇개 청소했는지 담는다
# 만약 위치,방향,먹은 갯수가 동일하면 싸이클.
# 틀린이유
# 처음에는 싸이클이 위치, 방향만 동일하면 발생하는 줄 알았는데
# 가희처럼 먹기만 하면 와리가리를 칠 수 있기에
# visited에 먹은 갯수도 추가해줌

n, m = map(int, input().split())
r, c, d = map(int, input().split())
grid1 = [list(map(int, input())) for i in range(n)]
grid2 = [list(map(int, input())) for i in range(n)]

visited = [[[-1] * 4 for _ in range(m)] for _ in range(n)]
clean = [[False] * m for i in range(n)]
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
empty = 0
time = 0
eat = 0
while True:
    # print(r,c,d,eat)
    if not clean[r][c]:
        eat += 1
        empty = 0
        clean[r][c] = True
        d = (d + grid1[r][c]) % 4
        nr = r + row[d]
        nc = c + col[d]
        if not (0 <= nr < n and 0 <= nc < m):
            time += 1
            break
        r = nr
        c = nc
    else:
        if visited[r][c][d] != eat:
            empty += 1
            visited[r][c][d] = eat
            d = (d + grid2[r][c]) % 4
            nr = r + row[d]
            nc = c + col[d]
            if not (0 <= nr < n and 0 <= nc < m):
                time += 1
                break
            r = nr
            c = nc
        else:
            break
    time += 1
print(time - empty)
