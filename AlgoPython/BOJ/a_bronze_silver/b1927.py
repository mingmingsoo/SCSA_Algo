import sys
import heapq
pq = []
n = int(sys.stdin.readline())
for i in range(n):
    num = int(sys.stdin.readline())
    if(num!=0):
        heapq.heappush(pq,num)
    else:
        if(len(pq)==0):
            print(0)
        else:
            print(heapq.heappop(pq))