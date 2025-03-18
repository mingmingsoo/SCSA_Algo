def find():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "I":
                return i, j


n, m = map(int, input().split())
grid = [list(input()) for i in range(n)]

r, c = find()
d_list = list(input())
for i in range(len(d_list)):
    d_list[i] = int(d_list[i]) - 1
row = [1, 1, 1, 0, 0, 0, -1, -1, -1]
col = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
time = 0
end = False
for dd in range(1, len(d_list) + 1):
    # 1. 미친 아두이노 리스트로 담기
    crazy_list = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "R":
                crazy_list.append((i, j))
    # 2. 종수 이동
    d = d_list[dd - 1]
    nr = r + row[d]
    nc = c + col[d]
    if grid[nr][nc] == "R": # 미친 아두이노 만나면 break
        time = dd
        end = True
        break
    if d != 4: # 이동 반영 (4는 제자리)
        grid[nr][nc] = "I"
        grid[r][c] = "."
    r = nr # 종수 이동 갱신
    c = nc

    # 3. 미친 아두이노 겹치는 애들은 폭발!
    # 이걸 count 세주고 1인 애들만 살아남게 해줄 거임
    check = [[0] * m for i in range(n)]
    for i in range(len(crazy_list)):
        cr, cc = crazy_list[i]
        grid[cr][cc] = "."
        min_d = abs(r - cr) + abs(c - cc)
        d = -1
        for k in range(9):
            ncr = cr + row[k]
            ncc = cc + col[k]
            new_d = abs(r - ncr) + abs(c - ncc)
            if new_d < min_d: # 최대한 종수한테 가까이 이동
                min_d = new_d
                d = k
        if (cr + row[d], cc + col[d]) == (r, c): # 종수 만날 수 있는 미친 아두이노면 종료
            time = dd
            end = True
            break
        check[cr + row[d]][cc + col[d]] += 1 # 카운트 반영
    if end:
        break
    for i in range(n): # 살아남은 애들만 표시
        for j in range(m):
            if check[i][j] == 1:
                grid[i][j] = "R"
if end:
    print(f"kraj {time}")
else:
    for _ in grid:
        print("".join(_))
