from collections import deque

start, end = map(int,input().split())
visited = [0]*100001

visited[start] = 1
q = deque([(start,0)])
# print(q)
ans = float("inf")
while q:
    cur, time = q.popleft()
    print(cur, time)
    if(cur == end):
        ans = min(ans, time)
    if(cur+1<100000 and visited[cur+1] ==0):
        visited[cur+1] = 1
        q.append([cur+1, time+1])
    if(cur-1>= 0 and visited[cur-1] ==0):
        visited[cur-1] = 1
        q.append([cur-1, time+1])
    if(cur*2<100000 and visited[cur*2] ==0):
        visited[cur*2] = 1
        q.append([cur*2, time])
print(ans)