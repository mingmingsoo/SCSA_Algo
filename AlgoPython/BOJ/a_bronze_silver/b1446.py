import heapq
from collections import deque

E, end = map(int, input().split())
size = 10_000+1
adj = [[] for i in range(size)]

for i in range(end):
    adj[i].append((i+1,1))

for i in range(E):
    s, e, weight = map(int, input().split())
    adj[s].append((e, weight))
d = [end+1]*(size+1)

def dijk(start):
    q = [(start,0)]
    while q:
        cur, dist = heapq.heappop(q)
        if dist > d[cur]:
            continue

        for node in adj[cur]:
            next, next_dist = node
            if(d[next] > next_dist+dist):
                d[next] = next_dist+dist
                heapq.heappush(q, (next,next_dist+dist))

dijk(0)
print(d[end])
