from collections import deque

grid = [list(input()) for i in range(10)]
# print(grid)

q = deque()

for i in range(10):
    for j in range(10):
        if(grid[i][j]=='X'):
            q.append((i,j))

# print(q)
row = [-1,1,0,0,1,1,-1,-1]
col = [0,0,1,-1,1,-1,1,-1]


def check(r, c):
    for k in range(8):
        omok = True
        for l in range(0,5):
            nr = r+row[k]*l
            nc = c+col[k]*l
            if(nr<0 or nr>=10 or nc<0 or nc>= 10):
                omok = False
                break
            if(0<=nr<10 and 0<=nc<10 and grid[nr][nc]!="X"):
                omok = False
                break
        if(omok == False):
            continue
        if(omok):
            return True
    return False


def isOmok(r, c):
    grid[r][c] = "X"
    for i in range(10):
        for j in range(10):
            if(grid[i][j]=='X'):
                if(check(i,j)):
                    # print(i,j ,"여기서 오목 발생")
                    return True
    grid[r][c] = "."
    return False


def bfs():
    while q:
        r, c = q.popleft()
        # print(r,c)
        for k in range(8):
            nr = r + row[k]
            nc = c + col[k]

            if (0<=nr<10 and 0<=nc<10 and grid[nr][nc]=='.' and isOmok(nr, nc)):
                # print(r,c,nr,nc)
                return 1
    return 0


ans = bfs()
print(ans)