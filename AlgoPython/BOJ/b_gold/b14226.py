'''
b14226
이게 먼서릴깡?
분할정복? 이분탐색?
* 2하거나 -1 하거나 bfs?
'''
from collections import deque

end = int(input())
start = 1

q = deque([(1,0, 0)]) # 현재화면, 클립보드, 횟수

visited = [[False]*1001 for i in range(1001)]
visited[1][0] = True

while q:
    cur, clipboard, cnt = q.popleft()

    if cur == end:
        print(cnt)
        break
    if 0<=cur<1001 and not visited[cur][cur]:
        q.append((cur,cur,cnt+1)) # 클립보드
        visited[cur][cur] = True
    if 0<=cur+clipboard<1001 and clipboard>0 and not visited[cur+clipboard][clipboard]:
        q.append((cur+clipboard, clipboard,cnt+1))
        visited[cur+ clipboard][clipboard] = True
    if cur-1>=0 and not visited[cur-1][clipboard]:
        q.append((cur-1,clipboard,cnt+1))
        visited[cur-1][clipboard] = True
