import math

T = int(input())
for tc in range(T):
    M, N, x, y = map(int, input().split())


    ans = 0
    isFound = False
    startX = 0
    startY = 0
    for i in range(1, math.lcm(M,N)+1):
        startX = (startX+1)%M
        startY = (startY+1)%N
        if(startX == 0):
            startX = M
        if(startY ==0):
            startY = N
        # print(startX, startY)
        if(startX == x and startY == y):
            ans = i
            break
    if(ans == 0):
        print(-1)
    else:
       print(ans)
