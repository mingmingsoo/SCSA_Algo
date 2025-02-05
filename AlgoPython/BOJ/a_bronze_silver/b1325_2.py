'''
하나의 정점으로 여러 노드 방문하고 싶음
최댓값을 가지는 정점들을 오름차순으로 출력

단방향

A가 B를 신뢰하면 B를 해킹시 A도 해킹 가능

넣어본 엣지케이스
5 4
3 1
3 2
3 4
3 5

1 2 4 5 출력

원형큐일 때 재귀 오류남... 이럴 수 가 잇나?
순환하는걸 확인해 줘야하나?

싸이클 확인해서 싸이클이면 그 갯수를 visited에 넣어주는 과정 필요

'''
import sys
sys.setrecursionlimit(10**5)
input= sys.stdin.readline

V, E = map(int, input().split())
adj = [[] for i in range(V+1)]
for i in range(E):
    end, start = map(int, input().split())
    adj[start].append(end)

def dfs(cur,start,end):
    global isCycle
    if(start ==end):
        isCycle = True
        return
    for node in adj[cur]:
        if(visited[node]>1):
            visited[cur] += visited[node]
            return
        dfs(node,start,node)
        if(not isCycle):
            visited[cur]+= visited[node]
        if(isCycle):
            visited[cur] += 1
            visited[node] += 1

visited = [1]*(V+1)
for v in range(1, V+1):
    isCycle = False
    if(visited[v]==1):
        dfs(v,v,0)

maxNum = max(visited)
for i in range(1,V+1):
    if(maxNum == visited[i]):
        print(i, end= " ")
# print(visited)