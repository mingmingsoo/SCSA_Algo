'''
맵 크기를 어떻게 할 것인가?
k가 300 이므로 1000씩 하면 될 것 같고
가운데 위치로 잡기.

마지막 출력을 위해선 전체 배열을 탐색하는 로직이 필요하기는 함.
bfs에 들고다닐수는 없음

'''
from collections import deque

size = 10
n,m,k = map(int, input().split())
grid = [[0]*size for i in range(size)]
startX = size//2 - n//2
startY = size // 2 - m// 2
endX = size//2 + n//2
endY = size // 2 + m // 2
if(n%2==1):
    endX+=1
if(m%2==1):
    endY+=1
q = deque()
for i in range(startX,endX):
    tmp = list(map(int, input().split()))
    for j in range(startY, endY):
        grid[i][j] = tmp[j-startY]
        if(grid[i][j]>0):
            q.append((i,j,grid[i][j],0))
row = [-1,1,0,0]
col = [0,0,1,-1]
limit = 0
while q:
    if (limit >= k):
        break
    qSize = len(q)
    for s in range(qSize):
        node = q.popleft()
        r = node[0]
        c = node[1]
        time = node[2]
        curTime = node[3]

        if(curTime<time):
            q.append((r,c,time,curTime+1)) # 시간이 안지났으면 대기
        elif(curTime==time): # 시간이 지났으면 확장 가능
            # 확장하는 로직
            for d in range(4):
                grid[r][c] = -1
                nr = r+row[d]
                nc = c+col[d]
                if(nr<0 or nr>=size or nc<0 or nc>=size):
                    continue
                elif(grid[nr][nc]==0):
                    q.append((nr,nc,time,0))
                    grid[nr][nc] = time
                # elif (grid[nr][nc] > 0):
                #     if(time>grid[nr][nc]):
                #         q.append((nr, nc, time, 0))
                #         grid[nr][nc] = time
                elif(grid[nr][nc]==-1):
                    continue
    limit+=1
    print("----------")
    for ele in grid:
        print(" ".join(f"{num:2}" for num in ele))
sum = 0
for i in range(size):
    for j in range(size):
        if(grid[i][j]>0):
            sum+=1
print(sum)