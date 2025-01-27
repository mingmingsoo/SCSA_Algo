from collections import deque

upNum , downNum = map(int, input().split())
up = []
down = []
for i in range(upNum):
    up.append(list(map(int, input().split())))
for i in range(downNum):
    down.append(list(map(int, input().split())))


def bfs(start):
    visited = [False]*101
    visited[start] = True
    q = deque([(start,0)])
    while q:
        next, cnt = q.popleft()
        if(next == 100):
            return cnt
        for i in range(upNum):
            if(up[i][0]==next):
                next = up[i][1]
                break

        for i in range(downNum):
            if(down[i][0]==next):
                next = down[i][1]
                break

        for i in range(1,7):
            if(next+i <=100 and visited[next+i]==False):
                q.append((next+i,cnt+1))
                visited[next+i]= True

ans = bfs(1)
print(ans)