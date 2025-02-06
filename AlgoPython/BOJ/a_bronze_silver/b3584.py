'''
반례
2
16
1 14
8 5
10 16
5 9
4 6
8 4
4 10
1 13
6 15
10 11
6 7
10 2
16 3
8 1
16 12
5 8

즉 최고조상과 자식일때 (8)이 최고조상
'''
import sys
sys.setrecursionlimit(10**5)
T = int(input())
for tc in range(T):
    V = int(input())
    adj = [[] for i in range(V + 1)]
    for i in range(V - 1):
        p, c = map(int, input().split())
        adj[c].append(p)
    child1, child2 = map(int, input().split())
    for i in range(V+1):
        if(len(adj[i])==0):
            best_parent = i

    if(child1 == best_parent or child2 == best_parent):
        print(best_parent)
        continue

    ans = 0
    visited = [False] * (V + 1)

    best_parent = -1

    def dfs(child, parents):
        global ans
        visited[child] = True
        for parent in adj[child]:
            if (visited[parent]):
                ans = parent
                return
            parents.append(parent)
            dfs(parent, parents)


    parents1 = []
    parents2 = []

    dfs(child1, parents1)
    dfs(child2, parents2)

    print(ans)