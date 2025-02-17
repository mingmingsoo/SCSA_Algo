import heapq

n = int(input())
arr = [int(input()) for i in range(n)]

q = []
for num in arr:
    if(num!=0):
        heapq.heappush(q, (abs(num),num))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])