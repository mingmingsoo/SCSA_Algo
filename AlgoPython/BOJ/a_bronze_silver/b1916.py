'''
A->B의 최소 비용
단방향
다익스트라 알고리즘
'''
import heapq

V = int(input())
E = int(input())

adj = [[] for i in range(V+1)]
for i in range(E):
    s,e,cost = map(int,input().split())
    adj[s].append((cost,e))

s,e = map(int, input().split())
d = [100_000*100_000+1]*(V+1) # 큰 값
d[s] = 0 # 초기값 세팅. 나에서 나는 비용 0임

def dijk(start):
    q = []
    heapq.heappush(q, (0,start)) # 초기값 넣어주기
    while q:
        cost, cur = heapq.heappop(q)
        if(cost>d[cur]): # 니가 지금 온 길이 내가 아까 계산한 길보다 크면 볼 필요도 없어
            continue

        for next_cost, next in adj[cur]:
            if(d[next] > next_cost+cost): # 내가 더 짧은 길을 아는데
                d[next] = next_cost+cost # 그 길로 와..
                heapq.heappush(q, (next_cost+cost, next))
dijk(s)
print(d[e])
