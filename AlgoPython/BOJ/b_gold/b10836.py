n, time = map(int, input().split())
tmp = [list(map(int, input().split())) for i in range(time)]
time_info = [0] * (2 * n - 1) # 0 몇개 1 몇개 2 몇개 -> 1차원 배열로 나열

for i in range(time):
    tmptmp = [0] * tmp[i][0] + [1] * tmp[i][1] + [2] * tmp[i][2] # 각 시간마다 0 몇개 1 몇개 2 몇개
    for j in range(2 * n - 1): # 더해버리기
        time_info[j] += tmptmp[j]

idx = 0
grid = [[1] * n for i in range(n)]
for i in range(n - 1, -1, -1): # 가생이 한번에 더하기
    for j in range(n):
        if i == 0 or j == 0:
            grid[i][j] += time_info[idx]
            idx += 1

for i in range(1, n): # 나머지 더하기
    for j in range(1, n):
        maxi = max(grid[i][j - 1] - 1, grid[i - 1][j] - 1, grid[i - 1][j - 1] - 1)
        grid[i][j] += maxi

for _ in grid:
    print(*_)
