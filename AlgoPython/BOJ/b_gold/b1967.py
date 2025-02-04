'''
트리의 지름 이론을 알아야 풀 수 있는 문제였다..
트리의 지름 = 말단노드 점들 중 두 점의 길이가 가장 긴 것이 지름이 된다.

임의의 점에서 모든 점들까지의 거리를 계산하고,
그 중 가장 긴 점이 지름 중 한 점이된다.

그 점에서 또 dfs를 돌려서 가장 긴 거리가 나머지 끝점이 된다.

def dfs(idx, dist):
    for node, d in adj[idx]:
        if(visited[node]==-1): # 방문한적이 없으면
            visited[node]=dist+d # 과거까지의 거리에 현재 점의 거리를 더해줌
            dfs(node, dist+d)
'''
import  sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input())
adj = [[] for i in range(V+1)]

for i in range(V):
    tmp = list(map(int, input().split()))
    start = tmp[0]
    for i in range(1,len(tmp)-1,2):
        end = tmp[i]
        length = tmp[i+1]
        adj[start].append((end, length))


# 임의의 점에서 말단 점 찾기.(거리가 가장 긴)
visited = [-1]*(V+1) # visited에 거리도 담아줄거임.
visited[1] = 0 # 시작점 설정


def dfs(idx, dist):
    for node, d in adj[idx]:
        if(visited[node]==-1): # 방문한적이 없으면
            visited[node]=dist+d
            dfs(node, dist+d)
    return

dfs(1,0) # 좌표와 현재까지의 길이
# print(visited)

node, maxLen = -1, -1
for i in range(1, V+1):
    if(maxLen<visited[i]):
        node = i
        maxLen = visited[i]

# 말단점에서 또다른 말단점 찾기
visited = [-1]*(V+1) # visited에 거리도 담아줄거임.

for i in range(1, V+1):
    visited[i] = -1
visited[node] = 0 # 시작점 설정

dfs(node,0)

# print(visited)
print(max(visited))
