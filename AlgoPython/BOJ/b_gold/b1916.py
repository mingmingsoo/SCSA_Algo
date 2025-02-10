'''
방향 그래프가 주어질 때
최소거리를 계산해라
'''
import heapq

V = int(input())
E = int(input())
adj = [[] for i in range(V+1)]

for i in range(E):
    s, e , w = map(int, input().split())
    adj[s].append((w,e))
start, end = map(int, input().split())

d = [100_000*1_000+1] *(V+1)
d[start] = 0


def dijk(start):
    q = [(0,start)]
    while q:
        dist, cur = heapq.heappop(q)

        if(dist > d[cur]):
            continue

        for next_dist, next in adj[cur]:
            if(d[next] > dist+next_dist):
                d[next] = dist+next_dist
                heapq.heappush(q,(d[next], next))

dijk(start)
print(d[end])
