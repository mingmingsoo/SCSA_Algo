size = 1001
grid = [[0]*size for i in range(size)]

n = int(input())
for nn in range(n):
    x,y,r,c = map(int, input().split())
    for i in range(x,x+r):
        for j in range(y, y+c):
            grid[i][j] = (nn+1)
# print(grid)
for i in range(n):
    sum = 0
    for r in range(size):
        for c in range(size):
            if(grid[r][c]==(i+1)):
                sum+=1
    print(sum)
