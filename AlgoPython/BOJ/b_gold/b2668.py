
n = int(input())
arr = list(range(1,n+1))
arr2=[0]*n
for i in range(n):
    arr2[i]=int(input())

# 양방향인 애들을 찾는다.?
adj = [[] for i in range(n+1)]

for i in range(n):
    adj[arr2[i]].append(arr[i])

ans = set()

# 싸이클이면 넣어준다.
def dfs(i, start):
    visited[i] = True
    for node in adj[i]:
        if(node == start):
            # 싸이클 발견
            ans.add(start)
            ans.add(i)
            return
        if(not visited[node]):
            dfs(node,start)
for i in range(1,n+1):
    visited = [False] * (n + 1)
    dfs(i,i)
    print(ans)
ans = sorted(list(ans))
print(len(ans))
for x in ans:
    print(x)
