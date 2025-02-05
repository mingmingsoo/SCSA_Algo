'''
- 하나의 정점으로 여러 노드 방문하고 싶음
- 최댓값을 가지는 정점들을 오름차순으로 출력(for문 필요)
- 단방향
- A가 B를 신뢰하면 B를 해킹시 A도 해킹 가능 -> start, end 가 뒤집혀서 들어옴

넣어본 엣지케이스
5 4
3 1
3 2
3 4
3 5

1 2 4 5 출력

8 8
2 1
3 2
4 3
5 4
6 5
3 6
7 3
8 7

1 출력 [0, 8, 7, 6, 6, 6, 6, 2, 1] 해킹 횟수

6 5
1 2
2 3
3 1
5 4
6 4
1 2 3 4 출력

문제 해결
- bfs로 완전 탐색
- 매 정점마다 visited 초기화 필요
- depth가 아닌 몇번 방문했냐? 계산이 필요 = ele

회고
기본적인 bfs인데 dfs+dp로 풀어야한다 라고 생각해서 헤맸다.
bfs로 시작하고도 싹 지우고 했으면 visted 설정 오타가 안났을텐데
지우고 쓰고를 반복해서 visited에서 오류가 발생했다.
(visited = [0] 이런식으로 해놓고 True/ False 로 값을 바궜음)
맞고 나니까 왜틀렸는지 모르겠음 에휴 ㅠ


'''
import sys
from collections import deque

V, E = map(int, input().split())
adj = [[] for i in range(V+1)]
for i in range(E):
    end, start = map(int, input().split())
    adj[start].append(end)

# print(adj)

def bfs(start):
    ele = 1
    q = deque([start])
    while q:
        cur= q.popleft()
        for node in adj[cur]:
            if(not visited[node]):
                visited[node] = True
                q.append((node))
                ele+=1
    return ele

ans = [0]*(V+1)
for v in range(1, V+1):
    # bfs로 완전탐색.
    visited = [False] * (V + 1)
    visited[v] = True # 초기값 방문처리 필요
    ans[v] = bfs(v)

maxNum = max(ans)
for i in range(1,V+1):
    if(maxNum == ans[i]):
        print(i,end= " ")
# print(ans)