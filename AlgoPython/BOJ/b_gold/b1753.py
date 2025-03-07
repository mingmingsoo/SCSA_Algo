'''
방향그래프
'''
import heapq

V, E = map(int, input().split())
start = int(input())
adj = [[] for i in range(V+1)]
for i in range(E):
    s,e,cost = map(int, input().split())

    adj[s].append((cost,e))

d = [int(1e9)] *(V+1)
d[start] = 0

def dijk():
    q = []
    heapq.heappush(q,(0,start))

    while q:
        cost, cur = heapq.heappop(q)
        if cost > d[cur]:
            continue

        for next_cost, next in adj[cur]:
            if d[next] > next_cost+cost:
                d[next] = next_cost+cost
                heapq.heappush(q,(next_cost+cost,next))
dijk()

for i in range(1,V+1):
    if d[i] != int(1e9):
        print(d[i])
    else:
        print("INF")