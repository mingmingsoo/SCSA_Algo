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
    endR = size-1
    # print(endR, endC)

    while endR > 0:
        # 현재 위치에서 일단 위로가
        if (grid[endR - 1][endC] == 1):
            endR -= 1
        if (endR == 0):
            break
        # print(endR, endC)

        # 왼쪽으로 갈 수 있으면 가
        if(endC-1 >= 0 and grid[endR][endC-1]==1):
            while (endC-1 >= 0 and grid[endR][endC-1]==1):
                endC -=1

        # 오른쪽 검사
        elif(endC+1 < size and grid[endR][endC+1]==1):
            while (endC+1 < size and grid[endR][endC+1]==1):
                endC +=1


    print(f"#{tnum} {endC}")