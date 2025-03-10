# 달팽이 중앙에서부터 가보기
n = int(input())
target = int(input())

grid = [[0] * n for i in range(n)]

r = c = n // 2
d = two = cnt = 0
num = 1
row = [-1, 0, 1, 0]
col = [0, 1, 0, -1]
mark = 1
ar,ac = -1,-1
while not (r == c == 0):
    if mark == target:
        ar,ac = r+1, c+1
        # break
    grid[r][c] = mark
    nr = r + row[d]
    nc = c + col[d]
    r = nr
    c = nc
    mark += 1
    cnt += 1
    if cnt == num:
        cnt = 0
        two += 1
        d = (d + 1) % 4
    if two == 2:
        num += 1
        two = 0
grid[0][0] = n*n
for _ in grid:
    print(*_)
if ar == ac == -1:
    print(1,1)
else:
    print(ar,ac)
