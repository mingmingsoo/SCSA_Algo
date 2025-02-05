'''
풀었던 문제
작은 순으로 출력
'''
from collections import deque

V, E, sidx = map(int, input().split())
adj = [[] for i in range(V+1)]
for i in range(E):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for node in adj:
    node.sort()
ansDFS = []
ansBFS = []


def dfs(cur):
    visited[cur] = True
    ansDFS.append(cur)
    for node in adj[cur]:
        if(not visited[node]):
            dfs(node)
def bfs(start):
    global visited
    visited = [False] * (V + 1)
    visited[start] = True
    q = deque([start])

    while q:
        cur = q.popleft()
        ansBFS.append(cur)
        for node in adj[cur]:
            if(not visited[node]):
                q.append(node)
                visited[node] = True


visited = [False] *(V+1)
dfs(sidx)
bfs(sidx)
print(*ansDFS)
print(*ansBFS)