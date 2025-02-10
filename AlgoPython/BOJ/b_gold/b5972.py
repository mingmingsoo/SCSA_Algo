'''
문제 설명
1 -> N 까지 최소거리로 방문
다익스트라. 거리를 어떻게 저장하지
'''
import heapq

V, E = map(int, input().split())
adj = [[] for i in range(V+1)]
for i in range(E):
    s,e,w = map(int, input().split()) # start, end, weight
    adj[s].append((w,e)) # tuple로 넣기 순서 헷갈리지 말기!
    adj[e].append((w,s)) # tuple로 넣기 q랑 통일해서 순서 넣기

d = [50_000_001]*(V+1)
d[1] = 0 # 시작점 설정

def dijk(start):
    q = [(0,start)]
    while q:
        dist, cur = heapq.heappop(q)
        if(dist> d[cur]):
            continue

        for next_dist, next in adj[cur]:
            # print(next_dist,next)
            if(d[next] > dist+next_dist):
                d[next] = dist+next_dist
                heapq.heappush(q,(d[next], next))


dijk(1)
# print(d)
print(d[V]) # 도착지까지의 거리는?