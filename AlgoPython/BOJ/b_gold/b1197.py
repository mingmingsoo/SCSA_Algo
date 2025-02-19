'''
b1197

최소스패닝트리 구현
'''
import heapq

V, E = map(int, input().split())
adj = [[] for i in range(V+1)]

for e in range(E):
    s,e,w = map(int, input().split())
    adj[s].append((w,e))
    adj[e].append((w,s))

visited = [False]*(V+1)
visited[1] = True # 초깃값 설정
ans, pick = 0,1
pq = []
for next_cost, next in adj[1]:
    heapq.heappush(pq, (next_cost, next))

while pick != V:
    cost, cur = heapq.heappop(pq)

    if visited[cur] : continue

    ans += cost
    pick += 1
    visited[cur] = True

    for next_cost, next in adj[cur]:
        heapq.heappush(pq, (next_cost,next))

print(ans)