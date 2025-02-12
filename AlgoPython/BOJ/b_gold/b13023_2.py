'''
문제 설명
    친구 1 에서 시작해서 친구5 까지 갈 수 있으면 1 출력
    = 즉 1에서 쭉~ 연결되서 본인 제외 정점 4개 갈 수 있냐/
    친구 번호는 0번부터!
입력
    V, E
    간선 정보

출력
    가능하면 1 불가능하면 0
구상
   백트래킹으로 타타타탙타고들어가서
   마지막애가 친구가 있기만 하면 된다.

틀린이유
    길을 가다가 돌아오려면 visited False로 길을 다시 열어줘야하는데 길을 안열어줘서
    가능해도 불가능하다고 출력함


'''
from collections import deque
import sys
sys.setrecursionlimit(10**5)

V, E = map(int, input().split())
adj = [[] for i in range(V)] # 0번 부터라 V+1 아님
for e in range(E):
    s,e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s)

def dfs(idx,cnt):
    if(cnt>=4): # 볼필요도 없어! 돌아가!
        print(1)
        exit()
    visited[idx] = True
    for node in adj[idx]:
        if(not visited[node]):
            dfs(node,cnt+1)
    visited[idx] = False # 이거 추가!
visited = [False] * V
for i in range(V):
    cnt = 0
    dfs(i,0)
print(0)
