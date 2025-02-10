'''
분할정복
size//2

'''

size = int(input())
grid = [list(map(int, input())) for i in range(size)]

ans = []

def valid(size, sr, sc):
    start_num = grid[sr][sc]
    for i in range(sr,sr+size):
        for j in range(sc,sc+size):
            if(grid[i][j]!=start_num):
                return 2
    else:
        return start_num
def mypow(size, sr, sc):
    num = valid(size,sr,sc)
    if(num==2):
        ans.append("(")
        mypow(size//2,sr,sc)
        mypow(size//2,sr,sc+size//2)
        mypow(size//2,sr+size//2,sc)
        mypow(size//2,sr+size//2,sc+size//2)
        ans.append(")")
    else:
        ans.append(num)


mypow(size,0,0) # size, start, end

print("".join(map(str,ans)))