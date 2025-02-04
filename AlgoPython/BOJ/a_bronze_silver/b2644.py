'''
촌수계산은 즉
두 정점사이의 최소거리를 구하라는 것
고로 bfs
deque 써보기
'''
from collections import deque

V = int(input())
adj = [[] for i in range(V+1)]

start, end = map(int,input().split())

E = int(input())
for i in range(E):
    s, e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)


def bfs(start, end):
    v = [False] * (V+1)
    v[start] = True
    q = deque([(start, 0)])

    while q:
        cur, cnt = q.popleft()
        if(cur== end):
            print(cnt)
            return
        for node in adj[cur]:
            if(not v[node]):
                q.append((node, cnt+1))
                v[node]= True
    print(-1) # 촌수 없으면 -1 출력

bfs(start, end)
