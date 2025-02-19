'''
프림 연습
1. adj 배열 받기 <- heapq 사용할거니까 가중치 먼저 넣어주기
2. visited 배열 생성 -> 와본 길은 안 갈 것임
    2-1. 시작점 방문체크
3. pq 생성
    3-1. 시작점에 연결된 애들을 넣어주기
4. pick = 1, total_cost = 0 설정
5. while pick != V
    5-1. 만약 와본 길이면 continue 굳이 안봐줘도됨. 왜냐하면 힙큐라 전에 와본길이 더 짧은 길일 것임
    5-2. 그게 아니라면 (1)비용 추가해주고, (2)점 하나 더본거 표시해주고, (3)방문체크해주고, (4)다음 노드 pq에 넣어줌
'''
import heapq

T = int(input())
for tc in range(T):

    V, E = map(int, input().split())
    adj = [[] for i in range(V + 1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((w, e))
        adj[e].append((w, s))

    visited = [False] * (V + 1)  # 한번 본 길은 두번다신 보지 않는다. 왜냐하면 힙큐가 알아서 작은 가중치만 빼주니까
    visited[0] = True  # 시작점 설정
    pq = []

    ans = 0
    pick = 1  # 하나 골랐어 (시작점)
    # 시작점에서의 연결된 점은 일단 pq에 넣어준다.
    for next_cost, next in adj[0]:  # 다음 점 일단 넣어줘
        heapq.heappush(pq, (next_cost, next))

    while pick != V + 1:  # 점 다 보면 안봐도 된다.
        dist, cur = heapq.heappop(pq)

        if visited[cur]:  # 이미 와본길이면 넘어가
            continue

        ans += dist  # 비용 추가
        visited[cur] = True
        pick += 1  # 점 하나 추가요

        for next_cost, next in adj[cur]:  # 다음 점 탐색
            heapq.heappush(pq, (next_cost, next))

    print(f"#{tc + 1} {ans}")



'''
크루스칼 연습
간선 위주로 가되, 부모가 같으면 탐색하지 않는다.
'''
def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x,y):
    p[find(y)] = find(x)

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())

    p = [n for n in range(0,V+1)]

    edges = [0] * E # 간선 정보로 담기!
    for i in range(E):
        s,e,w = map(int, input().split())
        edges[i] = (s,e,w)

    edges.sort(key= lambda x: x[2]) # 가중치 기준으로 오름차순
    ans = 0
    pick = 0

    for i in range(E):
        px = find(edges[i][0]) # 부모를 찾아라!
        py = find(edges[i][1])
        if(px!=py): # 부모가 다르면 합쳐주고
            union(px,py)
            ans += edges[i][2] # 가중치 더해주기
            pick+=1
        if(pick == V): # 최소 간선 갯수는 V(원래는 V-1)
            break

    print(f"#{tc+1} {ans}")