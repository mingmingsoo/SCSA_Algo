V = int(input())
E = int(input())

adj = [[] for i in range(V + 1)]

for i in range(E):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

visited = [False] * (V + 1)
ans = 0


def dfs(start):
    global ans

    visited[start] = True
    for node in adj[start]:
        if (not visited[node]):
            ans += 1
            dfs(node)


dfs(1)
print(ans)
