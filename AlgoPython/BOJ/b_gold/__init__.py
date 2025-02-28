'''
2593
문제설명
    수빈이 비슷한 문제
    bfs
입력
    N, M = 최대 N층, 엘레베이터 M대
    엘베 수열
    시작점 목적지

    부모 달고다니기.
'''
from collections import deque

N, M = map(int, input().split())
dong_adj = [[] for i in range(M+1)]
floor_adj = [[] for i in range(N+1)]
for m in range(M):
    start, bins = map(int, input().split())
    for i in range(start,N+1,bins):
        dong_adj[m+1].append(i)
        floor_adj[i].append(m+1)

print(dong_adj)
print(floor_adj)
start, end = map(int ,input().split())
q = deque()

visited = set() # 안되면 2차원 배열로
for i in range(1,M+1): # 여기 오타있었음 m 으로
    if start in dong_adj[i]:
        q.append((i,start,0,[i]))
        visited.add((i,start)) # dong, floor
print(visited)
ans = -1



def bfs():
    while q:

        dong,floor,cnt,path = q.popleft()
        if floor == end:
            print(cnt)
            for d in path:
                print(d)
            return


         # 층별 이동
        for next_dong in dong_adj[floor]:
            if (next_dong,floor) not in visited:
                q.append((next_dong,floor,cnt,path[:]+[next_dong]))
                visited.add((next_dong,floor))

        for next_floor in floor_adj[dong]:
            if (dong,next_floor) not in visited:
                q.append((dong,next_floor,cnt+1,path[:]))
                visited.add((dong,next_floor))


bfs()