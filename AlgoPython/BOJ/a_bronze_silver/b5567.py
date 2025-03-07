from collections import deque

V = int(input())
E = int(input())
adj = [[] for i in range(V + 1)]
for e in range(E):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

friend = 0
visited = [False] * (V + 1)
visited[1] = True
q = deque([(1, 0)])
while q:
    cur, depth = q.popleft() # pop으로 되어있었음;
    # print(cur)
    if depth > 1:
        break
    for next in adj[cur]:
        if not visited[next]:
            visited[next] = True
            friend += 1
            q.append((next, depth + 1))
print(friend)
