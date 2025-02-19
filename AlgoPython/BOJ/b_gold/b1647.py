'''
MST 연습
문제는 길지만 결국 MST를 구하고 그 중 가장 긴 간선을 빼라는 것.
마을을 두개로 나누는데 나누려면 가장 긴 간선을 제거하는 것이 최소 거리가 되기 때문.

'''
import heapq

V, E = map(int,input().split())
adj = [[] for i in range(V+1)]
for e in range(E):
    s,e,w =map(int,input().split())
    adj[s].append((w,e))
    adj[e].append((w,s))

visited = [False]*(V+1)
visited[1] = True
pick = 1
ans = 0
max_cost = 0
pq = []
for next_cost, next in adj[1]:
    heapq.heappush(pq, (next_cost,next))

while pick != V:
    cost, cur = heapq.heappop(pq)
    if(visited[cur]):
        continue
    max_cost = max(max_cost, cost)
    visited[cur] = True
    ans+=cost
    pick+=1

    for next_cost, next in adj[cur]:
        heapq.heappush(pq, (next_cost, next))
print(ans-max_cost)