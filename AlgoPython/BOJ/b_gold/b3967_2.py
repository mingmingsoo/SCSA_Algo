'''
백트래킹 하겠습니다.
사전순이니까 .. 그냥 포문 돌면서
발견하면 바로 탈출하면 될듯?

-> 잘 안돼서 순열로 풀었습니다....
-> 가지치기 추가했습니다.

'''
N = 5
M = 9
grid = [list(input()) for i in range(N)]
tmp = [True]*13
sel_ro = [] # 좌표를 담음

for i in range(N):
    for j in range(M):
        if "A"<=grid[i][j]<="Z":
            grid[i][j] = ord(grid[i][j])-64
            tmp[grid[i][j]] = False
        elif(grid[i][j]=="x"):
            sel_ro.append((i,j))
            grid[i][j]=0
        else:
            grid[i][j]=0
n = len(sel_ro)

arr_num = [] # 가능한 숫자를 담는 배열
for i in range(1,13):
    if tmp[i]:
        arr_num.append(i)

find = False
visited = [False]*n
sel_num = [0]*n # 어떤 숫자를 담을지 고른 배열

def isok(sel_num,idx):
    global grid
    grid_origin = [_[:] for _ in grid]

    for i in range(idx):
        r, c = sel_ro[i]
        num = sel_num[i]
        grid[r][c] = num

    if(grid[0][4]*grid[1][3]*grid[2][2]*grid[3][1]!=0 and
            grid[0][4]+grid[1][3]+grid[2][2]+grid[3][1]!=26):
        grid = [_[:] for _ in grid_origin]
        return False
    if(grid[3][1]*grid[3][3]*grid[3][5]*grid[3][7]!=0 and
        grid[3][1]+grid[3][3]+grid[3][5]+grid[3][7]!=26):
        grid = [_[:] for _ in grid_origin]
        return False
    if(grid[0][4]*grid[1][5]*grid[2][6]*grid[3][7]!=0 and
        grid[0][4]+grid[1][5]+grid[2][6]+grid[3][7]!=26):
        grid = [_[:] for _ in grid_origin]
        return False
    if(grid[1][1]*grid[2][2]*grid[3][3]*grid[4][4]!=0 and
        grid[1][1]+grid[2][2]+grid[3][3]+grid[4][4]!=26):
        grid = [_[:] for _ in grid_origin]
        return False
    if(grid[1][7]*grid[2][6]*grid[3][5]*grid[4][4]!=0 and
        grid[1][7]+grid[2][6]+grid[3][5]+grid[4][4]!=26):
        grid = [_[:] for _ in grid_origin]
        return False
    if(grid[1][1]*grid[1][3]*grid[1][5]*grid[1][7]!=0 and
            grid[1][1]+grid[1][3]+grid[1][5]+grid[1][7]!=26):
        grid = [_[:] for _ in grid_origin]
        return False

    grid = [_[:] for _ in grid_origin]

    return True

def btk(idx):

    global find

    if(not isok(sel_num,idx)):
        return
    if find:
        return
    if(idx == n):
        for i in range(n):
            r,c = sel_ro[i]
            num = sel_num[i]
            grid[r][c] = num


        find = True
        for i in range(N):
            for j in range(M):
                if grid[i][j] >0:
                    print(chr(grid[i][j] + 64), end="")
                else:
                    print(".", end="")
            print()
        return

    for i in range(n):
        if not visited[i]:
            visited[i]= True
            sel_num[idx] = arr_num[i]
            btk(idx+1)
            visited[i]= False

btk(0)

