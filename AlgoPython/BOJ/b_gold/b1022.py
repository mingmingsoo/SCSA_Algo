'''
50 50 소용돌이 만든다
숫자 조정한다
'''
size = 50
grid = [[0]* size for i in range(size)]

num = size*size

col = [1,0,-1,0]
row = [0,1,0,-1]

r,c,d = 0, 0,0

while num>0:
    grid[r][c] = num
    if not (0<=r+row[d]<size and 0<=c+col[d]<size) or grid[r+row[d]][c+col[d]] !=0:
        d = (d+1)%4

    nr = r+row[d]
    nc = c+col[d]
    r = nr
    c = nc

    num -=1

for _ in grid:
    print(*_)