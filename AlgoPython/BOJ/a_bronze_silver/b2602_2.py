'''
양방향

넣어본 테케
7
5
1 2
2 3
1 5
5 2
5 6

dfs(4) 일때 0이 잘 뜨는지 확인했음
'''
V = int(input())
E = int(input())
adj = [[] for i in range(V+1)]
for i in range(E):
    s, e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)

num = 0
visited = [0] * (V+1)
def dfs(cur):
    global num
    num+=1

    visited[cur] = 1
    for next in adj[cur]:
        if(visited[next] ==0):
            dfs(next)

dfs(1)
print(num-1)