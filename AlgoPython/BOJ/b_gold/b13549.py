from collections import deque

start, end = map(int,input().split())
isBfs = True
ans = float("inf")
if(start>end):
    isBfs = False
    ans = start - end
if(isBfs):

    visited = [[0]*3 for i in range(100001)]
    q = deque([(start,0)])

    # print(q)
    while q:
        cur, time = q.popleft()
        # print(cur, time)
        if(cur == end):
            ans = min(ans, time)
            continue
        if(time>=ans):
            continue
        if(cur >= end and time> ans):
            continue
        if(cur+1<=100000 and visited[cur+1][0] ==0):
            visited[cur][0] = 1
            q.append([cur+1, time+1])
        if(cur-1>= 0 and visited[cur-1][1] ==0):
            visited[cur][1] = 1
            q.append([cur-1, time+1])
        if(cur*2<=100000 and visited[cur*2][2] ==0):
            visited[cur][2] = 1
            q.append([cur*2, time])
print(ans)