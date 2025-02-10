import sys
input = sys.stdin.readline


n,m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

sum_grid = [[0]*(n+1) for i in range(n+1)]
sum_grid[0][0] = grid[0][0]

# 누적합 구하기
for i in range(1,n):
    sum_grid[i][0] = grid[i][0]+sum_grid[i-1][0]
for j in range(1,n):
    sum_grid[0][j] = grid[0][j]+sum_grid[0][j-1]
for i in range(1,n):
    for j in range(1,n):
        sum_grid[i][j] = sum_grid[i-1][j] + sum_grid[i][j-1] - sum_grid[i-1][j-1]+grid[i][j]

# 큰사각형 - 작은사각형1-작은사각형2 +겹치는 사각형
for i in range(m):
    x1,y1,x2,y2 = map(lambda x: int(x)-1, input().split())
    ans = sum_grid[x2][y2] - sum_grid[x1-1][y2] - sum_grid[x2][y1-1] +sum_grid[x1-1][y1-1]
    print(ans)
