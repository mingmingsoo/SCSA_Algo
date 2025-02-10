'''
양방향 다익스트라
갈 수 있는 길이 정해져있음
0이면 갈 수 있고, 1이면 갈 수없음
맨 처음 무조건 0이고
마지막은 무조건 1인데
마지막은 1이여도 무조건 갈 수 있음.

입력조건: 정점이 0부터 시작함. V+1이 아닌 V로 한다.
'''
import heapq

V, E = map(int, input().split())
is_go = list(map(int, input().split()))
is_go[V-1] = 0 # 1이여도 마지막은 갈 수 있음

adj = [[] for i in range(V)]
for i in range(E):
    s, e ,w = map(int, input().split())
    adj[s].append((w,e))
    adj[e].append((w,s))
size = 100_000*100_000+1
d = [size]*(V)
d[0] = 0

def dijk(start):
    q = [(0, start)]
    while q:
        dist, cur = heapq.heappop(q)
        # print(dist,cur)
        if(dist>d[cur]): # 지금 루트가 아까 전에 온 루트보다 길면 볼 필요도 없다.
            continue
        for next_dist, next in adj[cur]:
            if(is_go[next]==1):
                continue # 어차피 시야에 보여서 못간다.
            elif(d[next]>next_dist+dist): # 최솟값을 갱신해준다.
                d[next] = next_dist+dist
                heapq.heappush(q,(next_dist+dist,next))


dijk(0)
if(d[V-1]==size):
    print(-1)
else:
    print(d[V-1])