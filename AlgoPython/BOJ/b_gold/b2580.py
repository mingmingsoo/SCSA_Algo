'''
[문제 설명]
    스도쿠에 빈칸이 뚫려있는데, 그것을 스도쿠에 규칙에 맞게 채워서 출력해봐라.
[구상]
    0인 칸을 배열에 담는다.
    백트래킹을 돌린다.
[알아볼 것]
exit 안쓰고 어떻게 탈출하지...
다 담는 수밖에 없나?ㅜㅜ
'''
N = 9
grid = [list(map(int,input())) for i in range(N)]
empty_list = []

for i in range(N):
    for j in range(N):
        if(grid[i][j]==0):
            empty_list.append((i,j))

def isKaro(r, c):
    # 일단 넣고 생각.
    count_list = [0]*9
    for j in range(N):
        if(grid[r][j]==0):
            continue
        count_list[grid[r][j]-1]+=1
        if(count_list[grid[r][j]-1]>1):
            grid[r][c] = 0
            return False
    return True

def isSero(r, c):
    # 일단 넣고 생각.
    count_list = [0]*9
    for i in range(N):
        if(grid[i][c]==0):
            continue
        count_list[grid[i][c]-1]+=1
        if (count_list[grid[i][c] - 1] > 1):
            grid[r][c] = 0
            return False
    return True


def isX(r, c):
    # 일단 넣고 생각. # 여기가 좀 빡쎄네 어떻게 하면 3*3이되는지
    count_list = [0]*9
    if(r<3):
        start_r = 0
    elif (r<6):
        start_r = 3
    else:
        start_r=6

    if(c<3):
        start_c = 0
    elif (c<6):
        start_c = 3
    else:
        start_c=6

    for i in range(start_r,start_r+3):
        for j in range(start_c,start_c+3):
            if(grid[i][j]==0):
                continue
            count_list[grid[i][j]-1] += 1
            if (count_list[grid[i][j] - 1] > 1):
                grid[r][c] = 0
                return False
    return True
def btk(idx):
    global cnt
    if(cnt>0):
        return
    if(idx==len(empty_list)):
        cnt+=1
        for row in grid:
            print("".join(map(str,row)))
        return
    r, c = empty_list[idx]
    # 가로 세로 3*3 가능한 숫자만 넣기..
    for i in range(1,10):
        grid[r][c] = i
        if(isKaro(r,c) and isSero(r,c) and isX(r,c)):
            btk(idx+1)
            grid[r][c] = 0

cnt = 0
btk(0)