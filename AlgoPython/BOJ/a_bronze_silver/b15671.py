n = int(input())

grid = [[0] * 6 for i in range(6)]
# 1 백 2 흑
grid[2][2] = 1
grid[3][3] = 1
grid[2][3] = 2
grid[3][2] = 2

row = [-1, 1, 0, 0, 1, 1, -1, -1]
col = [0, 0, 1, -1, 1, -1, 1, -1]


def change(r, c, color):

    for k in range(8):
        visited = set()
        mycolor = False
        l = 1
        while True:
            nr = r+row[k]*l
            nc = c+col[k]*l
            if not(0<=nr<6 and 0<=nc<6):
                break
            if grid[nr][nc] == color:
                mycolor = True
                break
            elif grid[nr][nc] ==0:
                break
            else:
                visited.add((nr,nc))
                l+=1

        if(mycolor):
            for ir, ic in visited:
                grid[ir][ic] = color


for i in range(n):
    # 흑돌 선
    r, c = map(lambda x:int(x)-1, input().split())
    if (i % 2 == 0):
        grid[r][c] = 2
    else:
        grid[r][c] = 1

    change(r, c, grid[r][c])

b = 0
w = 0
for i in range(6):
    for j in range(6):
        if grid[i][j] == 1:
            w += 1
        elif grid[i][j] == 2:
            b += 1
for i in range(6):
    for j in range(6):
        if(grid[i][j]==1):
            print("W",end = "")
        elif(grid[i][j]==2):
            print("B",end = "")
        else:
            print(".", end = "")
    print()
if (w > b):
    print("White")
else:
    print("Black")
