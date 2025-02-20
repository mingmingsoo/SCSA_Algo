import heapq
from collections import deque

n,m = map(int, input().split())

'''
예전에 풀었떤 방식이 틀리고
기억이 안나서
다익스트라로 다시 풀어보겠습니다.!!!!!!!!!
'''
size = 100_001
d = [100_001] * 100_001
def bfs():

   d[n] = 0
   q = []
   heapq.heappush(q,(0,n))

   while q:
       cost, cur = heapq.heappop(q)
       if(cur ==m):
           print(cost)
           return

       if (cost > d[cur]):continue


       if cur-1>=0 and d[cur-1] > cost+1:
           d[cur-1] = cost+1
           heapq.heappush(q,(cost+1,cur-1))

       if cur+1<size and d[cur+1] > cost+1:
           d[cur+1] = cost+1
           heapq.heappush(q,(cost+1,cur+1))

       if cur*2<size and d[cur*2] > cost:
           d[cur*2] = cost
           heapq.heappush(q, (cost, cur*2))
if(n>m):
    print(n-m)
else:
    bfs()