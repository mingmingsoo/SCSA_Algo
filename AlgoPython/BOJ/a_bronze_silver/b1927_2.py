import heapq
import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
q = []
for num in arr:
   if num != 0:
       heapq.heappush(q,num)
   else:
       if not q:
           print(0)
       else:
           print(heapq.heappop(q))
