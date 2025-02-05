'''
풀었던 문제
최소값 출력이므로 bfs -> 도달 가능하면 return 후 종료
숫자는 계속 커지기만 한다 -> visited가 필요하지 않다.

'''
from collections import deque

start, end = map(int, input().split())
ans = -1

def bfs(start, end):
    global ans
    q = deque([(start, 1)]) # 시작점과 숫자와 거리
    while q:
        cur, cnt = q.popleft()
        if(cur == end):
            ans = cnt
            return
        if(cur*2<=1000000000):
            q.append((cur*2,cnt+1))
        if (cur * 2 <= 1000000000):
            q.append((cur*10+1,cnt+1))

bfs(start, end)

print(ans)