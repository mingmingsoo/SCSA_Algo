'''
크루스칼로 풀기
'''
import sys
sys.setrecursionlimit(10**5)

V, E = map(int, input().split())
edges = []
for i in range(E):
    s,e,w = map(int, input().split())
    edges.append((s,e,w))

edges.sort(key=lambda x:x[2])

p = [v for v in range(V+1)]
pick = 1
ans = 0

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]
def union(x,y):
    p[find(y)] = find(x)

for i in range(E):
    px = edges[i][0]
    py = edges[i][1]

    if(find(px)!= find(py)):
        # 우리의 대왕 부모가 다르면
        union(px, py) # 다음을 탐색을 위해 부모 합쳐준다.
        ans += edges[i][2] # 그리고 거리 더한다.
        pick+=1

    if pick == V: # 최소 간선을 다 선택했다.
        break
print(ans)