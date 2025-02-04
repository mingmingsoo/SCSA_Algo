import heapq
import sys
class num:
    def __init__(self, n):
        self.n = n
    def __lt__(self, other):
        if(abs(self.n)==abs(other.n)):
            return self.n<other.n
        else:
            return abs(self.n)<abs(other.n)
input = sys.stdin.readline
n = int(input())
pq = []
for i in range(n):
    order = int(input())
    if(order!=0):
        heapq.heappush(pq, num(order))
    else:
        if(not pq):
            print(0)
            continue
        print(heapq.heappop(pq).n)
