'''
땅의 높이를 모두 동일하게 만들고 싶음
높이를 깎아서 인벤토리에 넣고(2h)
인벤토리에서 꺼내서 0,0에 가까운 곳에 높이를 올린다.(1h)
'''
from collections import deque

N,M,B = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(N)]


maxHeight = -1
minHeight = 257
for row in grid:
    maxHeight = max(maxHeight, max(row))
    minHeight = min(minHeight, min(row))

time = float('inf')
height = -1
def findtime():
    global time, height
    for h in range(minHeight, maxHeight + 1):  # 목표로 하는 값임.
        b = B
        add = 0
        remove = 0
        for i in range(N):
            for j in range(M):
                diff = grid[i][j] - h
                if(diff>0):
                    remove += diff
                elif(diff<0):
                    add += abs(diff)
        b += remove
        if(add>b):
            continue
        eachTime = remove * 2+ add
        if(eachTime<=time): # 이것 때문에 틀렸음 동일한 최소 시간이 있다면 높이가 가장 큰 경우를 출력 그래서 <= 표시가 필요함
            time = eachTime
            height =h
        # print(eachTime, h)
findtime()

print(time, height)