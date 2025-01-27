from collections import deque

n , m = map(int, input().split())


def bfs(start,end, time):
    size = 100001
    visited = [0]*size
    q = deque()
    q.append((start,time))
    visited[start] =1

    while q:
        next, nowTime = q.popleft()

        if(next ==end):
            return nowTime

        if(next+1<size and visited[next+1] == 0):
            q.append((next+1, nowTime+1))
            visited[next+1] = 1
        if(next-1>=0 and visited[next-1] == 0):
            q.append((next-1, nowTime+1))
            visited[next-1] = 1
        if(next*2<size and visited[next*2] == 0):
            q.append((next*2, nowTime+1))
            visited[next*2] = 1

ans = bfs(n,m,0)
print(ans)