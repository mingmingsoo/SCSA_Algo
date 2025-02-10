'''
다익스트라 연습
양방향...
'''
from collections import deque
size = float("inf")
start, end = map(int, input().split())
V,E = map(int, input().split())
adj = [[] for i in range(V+1)]
for i in range(E):
    s,e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

dist = [size] *(V+1)
dist[start] = 0
def dijk(start):
    q = deque([(start,0)])
    while q:
        cur, cnt = q.popleft()
        if(cnt>dist[cur]):
            continue

        for node in adj[cur]:
            if(dist[node] > cnt+1):
                dist[node] = cnt+1
                q.append((node,cnt+1))

dijk(start)
if(dist[end]==size):
    print(-1)
else:
    print(dist[end])
# print(dist)
