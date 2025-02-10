import heapq
import sys

input = sys.stdin.readline
n = int(input())
pq = []
for i in range(n):
    order = int(input())
    if(order!=0):
        heapq.heappush(pq, (abs(order),order))
    else:
        if(not pq):
            print(0)
            continue
        absNum, origin = heapq.heappop(pq)
        print(origin)