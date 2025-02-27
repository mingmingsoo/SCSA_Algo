'''
문제 설명
    최소 거리로 가기 위해서 어디를 들려야하는가?;;;;ㅠㅠ
    다익스트라 응용
'''
import sys
import heapq
input = sys.stdin.readline
V, E = map(int, input().rstrip().split())
grid = [["-"]*(V+1) for i in range(V+1)]
adj = [[] for i in range(V+1)]
for i in range(E):
    s,e,cost = map(int, input().rstrip().split())
    adj[s].append((cost,e))
    adj[e].append((cost,s))

def dijk(idx):
    d[i] = 0 # 초깃값.
    q = []
    heapq.heappush(q, (0,idx,0,0))

    while q:
        cost, cur,depth,first = heapq.heappop(q)

        if cost> d[cur]:
            continue

        for next_cost, next in adj[cur]:
            if d[next] > cost+next_cost:
                d[next] = cost+next_cost
                if(depth==0):
                    grid[idx][next] = next
                    first = next
                else:
                    grid[idx][next] = first
                heapq.heappush(q,(cost+next_cost, next, depth+1, first))

for i in range(1,V+1):
    d = [1000*V+1]*(V+1)
    dijk(i)

for i in range(1,V+1):
    for j in range(1,V+1):
        print(grid[i][j], end = " ")
    print()
