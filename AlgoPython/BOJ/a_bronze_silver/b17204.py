'''
단방향 dfs
'''
V, target = map(int, input().split())
adj = [0] * V

for v in range(V):
    adj[v] = int(input())

ans = -1

visited = [False] * V


def dfs(idx, cnt):
    global ans
    if idx == target:
        ans = cnt
        return
    visited[idx] = True
    next = adj[idx]
    if not visited[next]:
        dfs(next, cnt + 1)


dfs(0, 0)
print(ans)
