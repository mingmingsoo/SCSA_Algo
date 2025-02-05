'''
1처럼 바로 return 하면 안되고..
q를 다 돌리되
백트래킹 조건은 넣어줄 수 있음
'''
from collections import deque

start, end= map(int, input().split())
max_size = 100_001
ans = max_size
total = 0


def bfs(start):
    global total
    global ans
    q = deque([(start,0)])
    visited = [[False]*3 for i in range(max_size)]
    visited[start][0] = True
    visited[start][1] = True
    visited[start][2] = True

    while q:
        cur, cnt = q.popleft()
        if(ans<cnt):
            continue

        if(cur==end):
            if(ans>cnt):
                ans = cnt
                total +=1
            else:
                total+=1

        if(0<=cur-1 and not visited[cur-1][0]):
            visited[cur][0] = True
            q.append((cur-1,cnt+1))
        if(cur+1<max_size and not visited[cur+1][1]):
            visited[cur][1] = True
            q.append((cur+1,cnt+1))
        if(cur*2<max_size and not visited[cur*2][2]):
            visited[cur][2] = True
            q.append((cur*2,cnt+1))

bfs(start)

print(ans)
print(total)