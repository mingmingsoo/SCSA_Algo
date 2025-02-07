
'''

bfs 풀이
틀렸던 이유:
visited = [False]* 1000000 라고 했다
배열은 0 부터 시작하는 것을 망각했다.
그래서 1000001 일때 인덱스 에러가 났을 거다

'''
from collections import deque

F,S,G,U,D = map(int, input().split())
ans = -1
# s->G
def bfs(start, end):
    global ans
    q = deque([(start,0)])
    visited = [False]* 1000001
    visited[start] = True


    while q:
        cur, cnt = q.popleft()
        if(cur == end):
            ans = cnt
            return
        if(cur-D>=1 and not visited[cur-D]):
            q.append((cur-D,cnt+1))
            visited[cur-D] = True
        if(cur+U<=F and not visited[cur+U]):
            q.append((cur+U,cnt+1))
            visited[cur+U] = True

bfs(S,G)
if(ans ==-1):
    print("use the stairs")
else:
    print(ans)