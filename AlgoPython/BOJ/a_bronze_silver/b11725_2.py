from collections import deque

V = int(input())

adj = [[] for i in range(V+1)]

for i in range(V-1):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

# print(adj)
q = deque([1]) # 대왕조상부터 내려가기
parents = [False] * (V+1)
while q:
    size = len(q)
    for s in range(size):
        parent = q.popleft()

        for child in adj[parent]:
            if(parents[child]==0):
                parents[child] = parent
                q.append(child)

parents.pop(0)
parents.pop(0)
for x in parents:
    print(x)
