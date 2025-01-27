from collections import deque
size = 100
T = 10
for i in range(T):
    tnum = int(input())

    grid = [list(map(int, input().split())) for i in range(size)]
    endC = -1
    for j in range(size):
        if(grid[size-1][j]==2):
            endC = j
            break

    # print(endC)
    def search(r, c):
        visited = set([(r,c)])
        d = 0
        while r >0:
            # print(r, c, d)
            if( d ==0 ): # 위
                r -=1
                # print("증명", r, c, d)
                # print(grid[r][c-1], (r,c-1) not in visited)
                if(c+1 < size and grid[r][c+1] == 1 and (r,c+1) not in visited):
                    c+=1
                    visited.add((r,c))
                    d = 1
                elif(c-1 >= 0 and grid[r][c-1] == 1 and (r,c-1) not in visited):
                    c-=1
                    visited.add((r,c))
                    d = 2
            elif( d ==1): # 오른쪽
                if(grid[r-1][c]==1 and r-1 ==0):
                    return c
                if(c>=size):
                    d= 0
                    return c
                c += 1
                if(r-1 >0 and grid[r-1][c] == 1 and (r-1,c) not in visited):
                    # r-=1
                    visited.add((r,c))
                    d = 0
            elif( d ==2): # 왼쪽
                if(grid[r-1][c]==1 and r-1 ==0):
                    return c
                if(c<=0):
                    d= 0
                    return c
                c -= 1
                if(r-1 >0  and grid[r-1][c] == 1 and (r-1,c) not in visited):
                    # r-=1 이거 안지워서 답 출력 안됐었ㄹ음
                    visited.add((r,c))
                    d = 0

        return c
    ans = search(size-1,endC)
    print(f"#{tnum} {ans}")