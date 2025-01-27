'''
행이 H 열이 W
모든 구름은 1분이 지날 때 오른쪽으로 1칸 이동
몇 분 뒤에 구름이 오는가?

'''

n,m = map(int, input().split())

grid = [list(input()) for i in range(n)]


ansGrid = [[0]*m for i in range(n)]

for j in range(m-1, -1, -1):
    for i in range(0,n):
        if(grid[i][j]=='c'):
            continue
        else:
            isCloud = False
            for jj in range(j-1,-1,-1):
                if(grid[i][jj]=='c'):
                    ansGrid[i][j] = j-jj
                    isCloud = True
                    break
            if(isCloud==False):
                ansGrid[i][j] = -1

for row in ansGrid:
    for x in row:
        print(x, end= " ")
    print()


