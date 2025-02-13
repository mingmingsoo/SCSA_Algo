'''
[문제 설명]
    X를 연산해서 1을 만드는데 최소 연산 횟수를 구하여라.
[구상]
    bfs로도 풀어보고, dp로도 풀어보기
'''
from collections import deque

n = int(input())

visited = [False]*(n+1)
def bfs(start):
    q = deque([(start,0)])
    visited[start] = True # 다시 돌아올 일은 없지만...

    while q:
        cur, cnt = q.popleft()
        if(cur == 1):
            print(cnt)
            return

        if(cur%3==0 and not visited[cur//3]):
            q.append((cur//3,cnt+1))
            visited[cur//3] = True
        if (cur % 2 == 0 and not visited[cur // 2]):
            q.append((cur // 2, cnt + 1))
            visited[cur // 2] = True
        if(cur-1>=1 and not visited[cur-1]):
            q.append((cur -1, cnt + 1))
            visited[cur-1] = True

bfs(n)