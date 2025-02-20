'''
일단 달팽이 만든다 10001*10001 - 뒤에서 부터 채운다.
범위만큼 출력한다.(범위값 조정 필요)
https://leveloper.tistory.com/80
'''

r1,c1,r2,c2 = map(int, input().split())
grid = [[0]*(c2-c1+1) for i in range(r2-r1+1)]

for row in grid:
    print(row)

x, y, dir = 0, 0,0
num, dnum, cnt = 1,1,0
row = [0,-1,0,1]
col = [1,0,-1,0]
def isFinish():
    return grid[0][0] != 0 and grid[r2-r1][0] !=0 and grid[0][c2-c1] !=0 and grid[r2-r1][c2-c1]!=0
while not isFinish():
    if(x>=r1 and x<=r2 and y>=c1 and y<=c2):
        grid[x-r1][y-c1] = num
    num+=1
    cnt +=1
    x = x+row[dir]
    y = y+col[dir]

    if cnt == dnum:
        cnt = 0
        if dir ==1 or dir ==3:
            dnum+=1
        dir = (dir+1)%4
mx = num-1

for _ in grid:
    print(*_)