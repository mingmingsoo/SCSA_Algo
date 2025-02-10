import heapq
from collections import deque

V,E,K,start = map(int,input().split())
adj = [[] for i in range(V+1)]

for i in range(E):
    s, e= map(int,input().split())
    adj[s].append(e)
size = float("inf")
dist = [size] *(V+1)
dist[start] = 0

def dijk(start):
    pq = [(0,start)]
    while pq:
        cur_dist, cur = heapq.heappop(pq)

        if cur_dist> dist[cur]: # 이미 더 짧은 경로로 온적이 있으면 현재 경로 무시.
            continue

        for node in adj[cur]:
            if(dist[node]> cur_dist+1):
                dist[node] = cur_dist+1
                heapq.heappush(pq,(cur_dist+1, node))

dijk(start)
ans = []
for i in range(1,V+1):
    if(dist[i] == K):
        ans.append(i)
if(not ans):
    print(-1)
else:
    for x in ans:
        print(x)
