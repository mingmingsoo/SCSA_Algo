n = 5
grid =[[0]*(n+1) for i in range(n)]
grid[0][2] =1
grid[4][3] =1
grid[1][5] =1
for _ in grid:
    print(_)
print("===========")
# 회전
# 뒤에서부터 댕기기
for j in range(n + 1):
    grid[n - 1][j] = grid[n - 1][j - 1]

for i in range(n - 1, -1, -1):
    grid[i][n] = grid[i - 1][n]

for j in range(n, 1, -1):
    grid[0][j] = grid[0][j - 1]
for _ in grid:
    print(_)