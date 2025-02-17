import heapq

n = int(input())

arr = [int(input()) for i in range(n)]
q = []
for num in arr:
    if(num ==0):
        if(not q):
            print(0)
        else:
            print(-heapq.heappop(q))

    else:
        heapq.heappush(q,-num)