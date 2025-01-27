n,m = map(int, input().split())

# M+1만큼 되야 안보임.

grid = [[0]*101 for i in range(101)]
# print(grid)

for i in range(n):
    x1,y1,x2,y2 = map(int, input().split())
    for r in range(y1, y2+1):
        for c in range(x1, x2+1):
            grid[r][c] += 1
ans = 0
for i in range(101):
    for j in range(101):
        if(grid[i][j]>m):
            ans += 1
print(ans)
