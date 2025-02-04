T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    adj = [[] for i in range(V + 1)]
    for i in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)
    for row in adj:
        row.sort()
    print(f"#{tc+1}", end = " ")

    def bfs(idx):
        q = [idx]
        visited = [False] * (V + 1)
        visited[idx] = True

        while q:
            cur = q.pop(0)
            print(cur, end = " ")

            for node in adj[cur]:
                if (not visited[node]):
                    q.append(node)
                    visited[node] = True


    bfs(1)
    print()