from collections import deque
mod = 10000
start, end = map(int, input().split())

q = deque((start,end))
visited = [0]*mod
visited[start] = 1

while q:
    now = q.popleft()
    strNow = f"{str(now):4}"
    

    if(visited[(2*now)%10000]==0):
        q.append((2*now)%10000)
    if(visited[(now-1)%10000]==0):
        q.append((now-1)%10000)
    if (True):
        q.append((2 * now) % 10000)
    if (True):
        q.append((2 * now) % 10000)