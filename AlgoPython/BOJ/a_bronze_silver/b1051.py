n, m = map(int, input().split())

grid =[list(map(int, input())) for i in range(n)]
# print(grid)

maxLen = min(n,m)

# 정사각형 크기는 1~ m or n
maxSize = 0
for i in range(0,n):
    for j in range(0,m):
        dot = grid[i][j]
        # 정사각형의 크기
        for size in range(1,maxLen):
            if(i+size>=n or j+size>=m):
                break
            if(size<=maxSize):
                continue
            if(grid[i+size][j]==dot and
            grid[i][j+size]==dot and
            grid[i+size][j+size]==dot):
                maxSize = max(maxSize, size)
maxSize+=1
print(maxSize**2)
